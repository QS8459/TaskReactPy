from reactpy import html, component;

custom_css = html.style("""


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
    .nav-text {
        color: rgba(255, 223, 0, 0.76);
    }
    
    .welcome-text {
        background: linear-gradient(to right, rgba(255, 215, 0, 0.8), rgba(218, 165, 32, 0.8));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
     .social-media {
        position: absolute;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
    }
    
    .header, .header a {
        color: white;
    }
    .header {
        background: rgba(0, 0, 0, 0.5);
        padding: 1rem;
        border-radius: 10px;
    }
"""
)
icons = html.link(
    {"rel":"stylesheet","href":"https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.4.1/font/bootstrap-icons.min.css"}
)


@component
def Index():

    layout = html._(
        custom_css,
        icons,
        html.div(
        {
            "class": "background",
        },
        [
            html.div(
                {
                    "class": "container mt-0",
                },

                    html.div(
                        {
                            "class": "d-flex justify-content-center align-items-center vh-100",
                        },
                        [
                            html.div(
                                {
                                    "class": "text-center transparent-box",
                                },
                                    html.h1({"class": "welcome-text"}, "Welcome to TaskAPI"),
                                    html.p({"class": "welcome-text"}, "Manage your tasks efficiently with TaskAPI."),
                                    html.div(
                                        {
                                            "class": "mt-4",
                                        },
                                        [
                                            html.a(
                                                {
                                                    "href": "/signup",
                                                    "class": "btn btn-primary me-2",
                                                },
                                                "Sign Up"
                                            ),
                                            html.a(
                                                {
                                                    "href": "/login",
                                                    "class": "btn btn-success",
                                                },
                                                "Sign In"
                                            ),
                                        ],
                                    ),
                                html.div(
                                    {"class": "social-media",},

                                    html.a(
                                        {
                                            "href": "https://github.com",
                                            'class': "me-2"
                                        },
                                        html.i({"class": "bi bi-github"}),
                                    ),
                                    html.a(
                                        {
                                            "href": "https://linkedin.com",
                                            'class': "me-2"

                                        },
                                        html.i({"class": "bi bi-linkedin"}),
                                    ),
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        )
    )
    return layout;