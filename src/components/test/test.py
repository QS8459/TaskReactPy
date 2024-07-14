from reactpy import component, html, use_state, use_effect;

from src.components.error_pages.smt_went_worng_toast import ErrorProps,ErrorToast;
from src.components.navbar.navbar import NavBar, NavBarProps;


from pydantic.dataclasses import dataclass;
from typing import List;

local_style = html.style(
   """
    body {
        background: linear-gradient(235deg, rgba(158,57,201,1) 0%, rgba(209,81,81,1) 96%);
        height: 100%;
        # display: flex;
        # justify-content: center;
        # align-items: center;
    }
     .navbar-custom {
        background: rgba(0, 0, 0, 0.6); /* Transparent with darker shades */
        backdrop-filter: blur(10px); /* Blur effect for better readability */
    }
    .navbar-brand, .nav-link {
        color: rgba(255, 255, 255, 0.8); /* Slightly transparent white text */
    }
    .nav-link:hover {
        color: rgba(255, 255, 255, 1); /* Fully opaque white text on hover */
    }   
    """
)





@component
def Test(props:List[NavBarProps]):
    layout = html._(
        local_style,
        html.nav(
        {
            "class": "navbar navbar-expand-lg navbar-custom"
        },
        [
            html.div(
                {
                    "class": "container-fluid"
                },
                [
                    html.a(
                        {
                            "class": "navbar-brand",
                            "href": "#"
                        },
                        "TaskAPI"
                    ),
                    html.button(
                        {
                            "class": "navbar-toggler",
                            "type": "button",
                            "data-bs-toggle": "collapse",
                            "data-bs-target": "#navbarNav",
                            "aria-controls": "navbarNav",
                            "aria-expanded": "false",
                            "aria-label": "Toggle navigation"
                        },
                        html.span({"class": "navbar-toggler-icon"})
                    ),
                    html.div(
                        {
                            "class": "collapse navbar-collapse",
                            "id": "navbarNav"
                        },
                        html.ul(
                            {
                                "class": "navbar-nav ms-auto"
                            },
                            [
                                html.li(
                                    {"class": "nav-item"},
                                    html.a(
                                        {
                                            'class':"nav-link",
                                            'href':i.url
                                        },
                                        i.title
                                    )
                                ) for i in props
                            ],
                        )
                    )
                ]
            )
        ]
    ))
    return layout;

@component
def NavBar():
    return Test([
        NavBarProps(
            title = "Home",
            url = "/home"
        )
    ])

