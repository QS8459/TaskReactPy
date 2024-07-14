from reactpy import component, html, use_state, use_effect;
from pydantic.dataclasses import dataclass;
from typing import Literal, Callable;
from time import sleep;


@dataclass
class ErrorProps:
    callback: Callable;
    display: bool = False
    message: str | None = None;
    type: Literal['401','404','500', '405','400', '503', '422'] | None = None;

    def set_display_false(self):
        self.display = False
        print(self.display);


@component
def ErrorToast(props: ErrorProps):
    display, set_display = use_state(props.display)
    # print(props.display);
    layout = html.div(
        {"class":"position-fixed bottom-0 end-0 p-3", "style":"z-index: 11"},
        html.div(
            {"class":"toast show"},
            html.div(
                {"class":"toast-header bg-danger text-white"},
                html.strong(
                    {"class":"me-auto"},
                    "Header"
                ),
                html.button(
                    {"type":"button","class":"btn-close", "data-bs-dismiss":"toast", "on_click": props.callback}
                )
            ),
            html.div(
                {"class":"toast-body"},
                html.p(props.message),
                f"Status Code\r", html.p(props.type)
            )
        )
    )
    # print(props.display);
    return layout if props.display else '';

