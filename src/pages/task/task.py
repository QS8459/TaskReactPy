from src.components.inputs.InputComponent import InputComp, InputProps;
from src.components.navbar.navbar import NavBar, NavBarProps;
from src.components.loading.loading import Loading;
from reactpy import use_state, html, component, event;
from src.components.utils import check_auth;
from src.main import client;

import json;
from time import sleep;

@component
def TaskAdd():
    auth, set_auth = use_state(False);

    if check_auth():
        set_auth(True);
    else:
        set_auth(False);

    payload, set_payload = use_state({"title": "", "summary": "", "status": ""});
    request_s, set_request_s = use_state(False);
    is_loading, set_loading = use_state(False);

    @event(stop_propagation=True)
    def click_btn(e):
        try:
            if payload.get('title') == '' or payload.get('summary') == '' or payload.get('status') == '':
                set_loading(False);
            else:
                set_loading(True)
        except:
            set_loading(False);

    @event(prevent_default=True)
    def request(e):
        try:
            sleep(5);
            request = client.post_r(
                url=f'{client.url_v1}/task/add/',
                payload=json.dumps(payload)
            );
            set_loading(False);
            set_payload({"title": "", "summary": "", "status": ""});
            set_request_s(True);
        except ConnectionError:
            set_request_s(False);
            set_loading(False);

    layout = html._(
        NavBar(
            [
                NavBarProps(title="Add Task", url="/task"),
                NavBarProps(title="About", url="/about")
            ]
        ),
        html.div(
        {'class': "container d-flex justify-content-center align-items-center w-25 vh-100 bg-success text-white bg-opacity-"},
        html.script('window.location.href = "/home"') if request_s else
        html.form(
            {
                "on_submit": request,
                "class": "mx-auto"
            },
            InputComp(
                InputProps(
                    name='title',
                    lable='title',
                    on_change=lambda e: set_payload({**payload, "title": e['target']['value']}),
                    value=payload['title'],
                    required=True,
                    label="Title"

                )
            ),

            InputComp(
                InputProps(
                    name='summary',
                    lable='summary',
                    on_change=lambda e: set_payload({**payload, "summary": e['target']['value']}),
                    value=payload['summary'],
                    required=True,
                    label="Summary"

                )
            ),
            html.div(
                html.label(
                    {
                        'for': "option",
                        'class': "form-label"
                    },
                    "Status"
                ),
                html.select(
                    {
                        'id': "option",
                        'value': payload["status"],
                        "on_change": lambda e: set_payload({**payload, "status": e['target']['value']}),
                        'class': 'form-select',

                    },
                    html.option({'value': "ONGOING"}, "Ongoing"),
                    html.option({'value': "DONE"}, "Done"),
                )
            ),
            html.button(
                {
                    "class": "btn btn-primary w-100",
                    'on_click': click_btn
                },
                "Submit"
            ) if not is_loading else Loading()
        )

    )
    )
    return layout;
