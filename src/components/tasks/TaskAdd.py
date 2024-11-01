from src.main import client;
from src.components.loading.loading import Loading
from reactpy import html, component, use_state, event;
from src.components.inputs.InputComponent import InputComp,InputProps;

from time import sleep;
import json;

@component
def Task():
    payload, set_payload = use_state({"title":"","summary":"","status":""});
    request_s, set_request_s = use_state(False);
    is_loading, set_loading = use_state(False);

    @event(stop_propagation = True)
    def click_btn(e):
        try:
            if payload.get('title') == '' or payload.get('summary') == '' or payload.get('status') == '':
                set_loading(False);
            else:
                set_loading(True)
        except:
            set_loading(False);

    @event(prevent_default = True)
    def request(e):
        try:
            sleep(5);
            request = client.post_r(
                url = f'{client.url_v1}/task/add/',
                payload = json.dumps(payload)
            );
            set_loading(False);
            set_payload({"title":"","summary":"","status":""});
            set_request_s(True);
        except ConnectionError:
            set_request_s(False);
            set_loading(False);

    return html.div(
        {'class':"container d-flex justify-content-center align-items-center w-25 vh-100 bg-success text-white bg-opacity-", "style":"{height: 50%}"},
        html.script('window.location.href = "/home"') if request_s else
        html.form(
            {
                "on_submit": request,
                "class":"mx-auto"
            },
            InputComp(
                InputProps(
                    name = 'title',
                    lable = 'title',
                    on_change = lambda e: set_payload({**payload,"title":e['target']['value']}),
                    value = payload['title'],
                    required = True,
                    label = "Title"

                )
            ),

            InputComp(
                InputProps(
                    name='summary',
                    lable='summary',
                    on_change=lambda e: set_payload({**payload, "summary": e['target']['value']}),
                    value=payload['summary'],
                    required = True,
                    label = "Summary"

                )
            ),
            html.div(
                html.label(
                    {
                        'for':"option",
                        'class':"form-label"
                    },
                    "Status"
                ),
                html.select(
                    {
                        'id':"option",
                        'value': payload["status"],
                        "on_change": lambda e: set_payload({**payload, "status": e['target']['value']}),
                        'class':'form-select',

                    },
                    html.option({'value':"ONGOING"},"Ongoing"),
                    html.option({'value':"DONE"},"Done"),
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