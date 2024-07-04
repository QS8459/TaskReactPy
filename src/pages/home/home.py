from src.components.navbar.navbar import NavBar, NavItemProps;
from src.components.list.list import List, ListProps;
from reactpy import html, component, use_state;
from src.components.utils import check_auth;
from src.main import client;

@component
def Home():
    auth, set_auth = use_state(False);
    if check_auth():
        set_auth(True);
    else:
        set_auth(False);

    layout = html._(

        html._(NavBar(
            [
            NavItemProps(label="Add Task", path="/task", is_active=True),
            NavItemProps(label="About", path="/about", is_active=False)
            ]
        )),
        html._(
            List(props = ListProps(request_url = 'task/all/')),
        ),

    );
    return layout if auth else "Non Authenticated";
