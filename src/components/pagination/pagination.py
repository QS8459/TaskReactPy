from reactpy import html, component, use_state;
from pydantic.dataclasses import dataclass;
from typing import Any;

@dataclass
class PaginationProps:
    page: int;
    set_page: Any;
    totalPages:int;


@component
def Pagination(props: PaginationProps):
    def handle_click(new_page):
        props.set_page(new_page);

    layout = html.div(
        {'class': 'd-flex justify-content-center mt-3'},
        html.button({"on_click": lambda e: handle_click(props.page-1), "disabled":props.page == 1, 'class': 'btn btn-primary me-2'}, "Previous"),
        html.span(f"Page {props.page} of {props.totalPages} "),
        html.button({"on_click":lambda e: handle_click(props.page +  1), "disabled":props.page == props.totalPages, 'class': 'btn btn-primary'}, " Next")
    );
    return layout;