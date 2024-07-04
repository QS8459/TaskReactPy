from reactpy import html, component;
from pydantic.dataclasses import dataclass;
from typing import Callable, List;

@dataclass
class NavItemProps():
    label: str;
    path: str;
    is_active: bool;

@component
def NavItem(props: NavItemProps):
    attribute = {'href': props.path};
    if props.is_active:
        attribute.update(
            {'class':'nav-link active', 'aria-current':'page'}
        );
    else:
        attribute.update(
            {'class':'nav-link'}
        );
    return html.li(
            {'class', 'nav-item'},
            html.a(attribute, props.label)
        );


@component
def NavBar(nav_attr: List[NavItemProps]):
    layout = html.nav(
        {'class':"navbar navbar-expand-lg navbar-dark bg-dark","aria-label":"Tenth navbar example"},
        html.div(
            {"class":"container-fluid", },
            html.a(
                {"class":"navbar-brand", "href":"/home"},
                "TaskAPI"
            ),
            html.div(
                {'class':"collapse navbar-collapse justify-content-md-center", "id":"navbarsExample08"},
                html.ul(
                    {"class":"navbar-nav"},
                    map(NavItem,nav_attr),
                )
            )
        )
    )
    return layout;
