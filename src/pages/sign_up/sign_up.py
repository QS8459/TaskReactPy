from reactpy import use_state, html, component, event;
from src.components.inputs.InputComponent import InputComp,InputProps;
from src.components.loading.loading import Loading;
from src.components.error_pages.smt_went_worng_toast import ErrorProps, ErrorToast;

from time import sleep;
from src.main import client;
import json;


local_style = html.style(
    """
    body {
        background: linear-gradient(235deg, rgba(158,57,201,1) 0%, rgba(209,81,81,1) 96%);
        height: 100%;
        # display: flex;
        # justify-content: center;
        # align-items: center;
    }
    .transparent-box {
        background: rgba(255, 255, 255, 0.2);
        padding: 2rem;
        border-radius: 10px;
    }
    """
)


@component
def SignUpScene():
    payload, set_payload = use_state({"email":"","password":""});
    is_loading, set_loading = use_state(False);
    ver, set_ver = use_state(False);
    error, set_error = use_state({"type":None,"message":"","display":False});

    return SignInForm(
        payload, set_payload,
        ver, set_ver,
        is_loading, set_loading,
        error, set_error
    )


@component
def SignInForm(
        payload, set_payload,
        ver, set_ver,
        is_loading, set_loading,
        error, set_error
):
    def button_loading(e):
        try:
            if payload.get("username") == '' or payload.get('password') == '':
                set_loading(False)
            else:
                set_loading(True);
        except ConnectionError:
            set_loading(False);


    @event(prevent_default=True)
    def sign_up(e):
        try:
            print(payload);
            request = client.post_r(
                url = f"{client.url_v1}/account/signup/",
                payload = json.dumps(payload)
            );
            sleep(5);
            if request.status_code in [200,201]:
                setattr(client, "email", payload.get('email'))
                set_ver(True);
            else:
                if request.as_dict.get('detail') is not None:
                    set_error({**error,"type":f"{request.status_code}", "message":request.as_dict.get('detail')[0].get('msg'), "display":True}),
                set_error({**error,"type":f"{request.status_code}", "message":"Something Went Wrong", "display":True}),
            set_loading(False);
            set_payload({"email":"","password":""})
        except Exception as e:
            set_loading(False);
            set_error({**error,
                       "type": None,
                       "message": "Something Went Wrong",
                       "display": True}),
            set_payload({"email": "", "password": ""})
            raise e



    layout = html._(
        local_style,
        html.div(
        {'class':"d-flex justify-content-center align-items-center vh-100"},
        html.script("window.location.href = '/verify_email';") if ver else
        html.div(
            {'class':"w-50 p-4 border rounded shadow transparent-box"},
            html.h2(
                {'class': "text-center mb-4"},
                "Sign Up"
            ),
        html.form(
                {
                    "on_submit":sign_up,
                },
                InputComp(
                    InputProps(
                        name = 'email',
                        value = payload.get('email'),
                        on_change = lambda e: set_payload({**payload, "email": e['target']['value']}),
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
                        on_change=lambda e: set_payload({**payload, "password": e['target']['value']}),
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
        ),

    ))
    return layout;