import math
import js
from react.components import div, p
from react.components.mui import List as ItemList, ListItem, ListItemText, IconButton, Icon, ListItemButton
from react import use_state
from react.decorator import component

from pyodide.http import pyfetch

from src.models import Movie
from typing import List
import json


@component
def UnwatchedIcon():
    return Icon['radio_button_unchecked']


@component
def WatchedIcon():
    return Icon['check_circle']


@component
def WatchIconButton(*, checked: bool, **button_props):
    return IconButton(**button_props)[
        WatchedIcon()() if checked else UnwatchedIcon()()
    ]


@component
def MovieItem(*, movie: Movie, key = None):
    watched, set_watched = use_state(False)

    def on_button_click(event):
      set_watched(not watched)

    return ListItem(
        key=key,
        secondary_action=WatchIconButton(checked=watched, edge='end', on_click=on_button_click)()
    )[
        ListItemText(primary=movie.name, secondary='Harry Potter' if True else None)()
    ]


@component
def MovieList(*movies: List[Movie]):
    return ItemList()(
        *[MovieItem(key=i, movie=movie)()
          for i, movie in enumerate(movies)],
    )
