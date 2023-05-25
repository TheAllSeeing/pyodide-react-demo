import js
from js import ReactDOM
import micropip
from typing import TYPE_CHECKING, List


async def install_imports(at_path: str = '/'):
    await micropip.install("pyodide-importer")
    from pyodide_importer import register_hook
    register_hook(at_path)

async def install_dependencies(deps: List[str]):
    for dep in deps:
        await micropip.install(dep)

def install_react_modules():
    from react.components import load_module
    from js import MaterialUI
    print('loading mui...')
    load_module(MaterialUI, 'mui')


def render_app(app: str):
    module, object_ = app.split(':')
    app = getattr(__import__(module), object_)
    dom_container = js.document.createElement('div')
    js.document.body.appendChild(dom_container)
    root = ReactDOM.createRoot(dom_container)
    root.render(app()())


DEPS = ['pydantic']

if __name__ == '__main__':
    await install_dependencies(DEPS)
    from pydantic import BaseModel
    await install_imports()
    install_react_modules()
    render_app('src:App')