from pydantic.dataclasses import dataclass;
from typing import Any, Callable, Literal;
from reactpy import component, html;
@dataclass
class InputProps():
    name:str | None = None;
    value:Any = None;
    on_change: Callable | None = None;
    label: str | None = None;
    placeholder:str | None = None;
    required: bool | None = False;
    type: Literal["text", 'password','email'] = 'text';
@component
def InputComp(props:InputProps):
    return html.div(
        {'class':'mb-3'},
        html.label(
            {'for':props.name,'class':'form-label'},
            props.label
        ),
        html.input(
            {
                'id': props.name,
                'value':props.value,
                'type': props.type,
                'name':props.name,
                'on_change': props.on_change,
                'placeholder': props.placeholder,
                'required': props.required,
                'class': "form-control"
            }
        )
    )
