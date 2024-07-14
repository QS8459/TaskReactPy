from reactpy import component, html;
from src.main import client;


@component
def VerifyYourEmail():
    try:
        email = client.email;
    except Exception:
        email = None;
    layout = html.div(
        {"class":"account-pages my-5 pt-sm-5"},
        html.div(
            {"class":"container"},
            html.div(
                {'class':"row"},
                html.div(
                    {"class":"col-lg-12"},
                    html.div(
                        {"class":"text-center mb-5 text-muted"}
                    )
                )
            ),
            html.div(
                {"class":"row justify-content-center"},
                html.div(
                    {"class":"col-md-8 col-lg-6 col-xl-5"},
                    html.div(
                        {"class":"card"},
                        html.div(
                            {'class':"card-body"},
                            html.div(
                                {'class':"p-2"},
                                html.div(
                                    {"class":"text-center"},
                                    html.div(
                                        {"class":"avatar-md mx-auto"},
                                        html.div(
                                            {'class':"avatar-title rounded-circle bg-light"},
                                            html.i(
                                                {"class":"bx bxs-envelope h1 mb-0 text-primary"},
                                                "Verify Email",
                                            )
                                        )
                                    ),
                                    html.div(
                                        {'class':"p-2 mt-4"},
                                        html.h4(
                                            "Verify Your Email"
                                        )
                                    ),
                                    html.p(
                                        f"We have sent to {email} verification email Please check it"
                                    ),
                                    html.div(
                                        {"class":"mt-4"},
                                        html.a(
                                            {"href":"/index"},
                                            "Verify Email"
                                        ),
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
    return layout;