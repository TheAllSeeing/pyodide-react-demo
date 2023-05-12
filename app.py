import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount('', StaticFiles(directory='static/client'), name='static')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port='8080', reload=True, reload_includes='*')
