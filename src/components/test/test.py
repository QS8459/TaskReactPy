from reactpy import component, html, use_state, use_effect;
from src.components.error_pages.smt_went_worng_toast import ErrorProps,ErrorToast;
from src.components.navbar.navbar import NavBar, NavItemProps
from time import sleep
@component
def Test():
    error, set_error = use_state({"type":None,"display":False,"message":""});

    layout = html._(
        NavBar([NavItemProps(label= "Task", path = "/task", is_active = True)]),
        html.button(
            {"on_click":lambda e : set_error({"type":"404", "message":"Test Error Message", "display":True})}, "Button"
        ),
        ErrorToast(
            ErrorProps(type=error.get("type"), message=error.get('message'), display=error.get('display'), callback = lambda e: set_error({**error,"display":False}))
        )
    )
    return layout;