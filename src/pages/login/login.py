from src.main import client;
from src.requester import S;
from reactpy import html, component, event, use_state;
from src.components.inputs.InputComponent import InputProps,InputComp;
from src.components.loading.loading import Loading;
from src.components.error_pages.smt_went_worng_toast import ErrorProps, ErrorToast;

import time;


@component
def Login():
    payload,setPayload = use_state({"username":"","password":""});
    error, set_error = use_state({"type": None, "display": False, "message": ""})
    page_state, setPageState = use_state(False);
    is_loading, set_loading = use_state(False);
    def button_loading(e):
        try:
            if payload.get("username") == '' or payload.get('password') == '':
                set_loading(False)
            else:
                set_loading(True);
        except ConnectionError:
            set_loading(False);


    @event(prevent_default=True)
    def login_request(e):
        try:
            request = client.post_r(
                url = f'{client.url_v1}/account/login/',
                payload = payload
            )
            time.sleep(5)
            print(request.as_dict.get('token'));
            setPageState(True);
            if request.as_dict.get("token"):
                S.headers.update({"Authorization":f"Bearer {request.as_dict.get('token')}"})
            else:
                setPageState(False);
                set_loading(False);
                setPayload({'username':"","password":''})
                set_error(
                   {
                     "message":request.text,
                     "display":True,
                     "type":str(request.status_code)
                    },
                )
        except Exception as e:
            setPageState(False);
            set_loading(False);
            set_error(
                {**error,
                 "message": e,
                 "display": True,
                 "type": "500"
                 },
            )

    return html.div(

        {'class':"d-flex justify-content-center align-items-center vh-100"},

        html.script("window.location.href = '/home';") if page_state else '',
        html.div(
            {'class':"w-50 p-4 border rounded shadow"},
            html.h2(
                {'class':"text-center mb-4"},
                "Login"
            ),
            html.form(
                {
                    "on_submit":login_request,
                },
                InputComp(
                    InputProps(
                        name = 'email',
                        value = payload.get('username'),
                        on_change = lambda e: setPayload({**payload, "username": e['target']['value']}),
                        placeholder = None,
                        required = True,
                        type = 'email',
                        label = 'Email'
                    )
                ),
                InputComp(
                    InputProps(
                        name='password',
                        value=payload.get('password'),
                        on_change=lambda e: setPayload({**payload, "password": e['target']['value']}),
                        placeholder=None,
                        required=True,
                        type='password',
                        label='Password'
                    )
                ),
                html.button(
                    {"class":"btn btn-primary w-100",
                     "on_click": button_loading},
                    "Submit"
                ) if not is_loading else Loading(),
            ),
        ),
        ErrorToast(
            ErrorProps(type=error.get("type"), message=error.get('message'), display=error.get('display'),
                       callback=lambda e: set_error({**error, "display": False}))
        )
    )


