import js
from js import ReactDOM
import micropip

await micropip.install("pyodide-importer")

from pyodide_importer import register_hook
register_hook('/')

from src import App

if __name__ == '__main__':
    dom_container = js.document.createElement('div')
    js.document.body.appendChild(dom_container)
    root = ReactDOM.createRoot(dom_container)
    root.render(App()())