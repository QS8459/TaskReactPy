from reactpy import component, html;
from pydantic.dataclasses import dataclass
from typing import Callable;
@dataclass
class ModalWindowDialogProps():
    title:str | None = "Example Modal Title";
    message:str | None = "Example Message";
    on_click: Callable | None = None;


@component
def ModalWindowDialog(props:ModalWindowDialogProps):
    layout = (
        html.div(
            {"class":"", 'tabindex':"-1"},
            html.script(
                """
                var myModal = document.getElementById('myModal')

                myModal.addEventListener('shown.bs.modal', function () {
                 myInput.focus()
                })
                """
            ),
            html.div(
            {'class':"modal-dialog"},
            html.div(
                {"class":"modal-content"},
                html.div(
                {   'class':"modal-header"},
                    html.h5(
                        {'class':"modal-title"},props.title
                    ),
                    html.button(
                        {'class':"btn-close", 'on_click':props.on_click, "data-mdb-ripple-init":True, "data-mdb-dismiss":"modal"}
                    )
                ),
                html.div(
                    {'class':"modal-body"},
                    html.p(
                        props.message
                    )
                ),
                html.footer(
                    {'class':"modal-footer"},
                    html.button(
                        {
                            'type':'button',
                            'class':"btn btn-secondary",  "data-mdb-ripple-init":True, "data-mdb-dismiss":"modal",
                            'on_click': props.on_click
                        },"Close"
                    ),
                    html.button(
                        {
                            'type':'button',
                            'class':"btn btn-primary", "data-mdb-ripple-init":True, "data-mdb-dismiss":"modal",
                            'on_click': props.on_click
                        },
                        "Got it"
                    )
                )
            )
        )
    )
    )

    return layout