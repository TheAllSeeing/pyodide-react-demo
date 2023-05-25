import math

from react.components import div, p
from react.decorator import component

from pyodide.ffi import create_proxy
from random import randint

from src.movie_list import MovieList
from src.models import Movie


def get_movies():
    return [
        Movie(name=f'Harry Potter {randint(10, 23)}', watched=False),
        Movie(name=f'Harry Potter {randint(2, 8)}', watched=True)
    ]


@component
def App(*children, **props):
    return div[
        MovieList[
            Movie(name=f'Harry Potter {randint(10, 23)}', watched=False),
            Movie(name=f'Harry Potter {randint(2, 8)}', watched=True)
        ]
    ]
