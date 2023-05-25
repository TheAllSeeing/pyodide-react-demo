import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from models import Movie, SerializedMovie

app = FastAPI()

app.mount('', StaticFiles(directory='static/client', follow_symlink=True), name='static')



@app.get('/movies')
def get_movie_list() -> list[Movie]:
    return [
        Movie(name='Chef', watched=False),
        SerializedMovie(name='Harry Potter & The Philosopher\'s Stone', watched=True,
                        series='Harry Potter', index=1),
        SerializedMovie(name='Harry Potter & The Order of the Phoenix', watched=True,
                        series='Harry Potter', index=5)
    ]


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port='8080',
                reload=True, reload_includes='*')
