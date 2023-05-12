import math, js
from src.react.components import div, p, Button
from src.react import use_state
from src.react.decorator import component


@component
def App(*children, **props):
    k, set_k = use_state(1)
    n, set_n = use_state(1)
    disabled, set_disabled = use_state(True)

    def increase_k(event):
        set_k(k + 1)
        set_disabled(k + 1 >= n)

    def increase_n(event):
        set_n(n + 1)
        set_disabled(k >= n + 1)

    return div()(
        p(class_name="centered-label")[f"{n} choose {k} = {math.comb(n, k)}"],
        Button(on_click=increase_n, variant="contained", color="secondary")[
            'Increase N'
        ],
        Button(on_click=increase_k, variant="contained", disabled=disabled, color="primary")[
            'Increase K'
        ],
    )