from reactpy import html, component, use_state, use_effect;
from pydantic.dataclasses import dataclass;
from src.main import client;
@dataclass
class ListProps():
    request_url:str;


@component
def List(props: ListProps):
    items, set_items = use_state([{}]);
    @use_effect
    def request():
        try:
            set_items(client.get_r(
                url = f'{client.url_v1}/{props.request_url}'
            ).as_dict);

        except Exception:
            pass

    layout = html.div(
        {'class':"d-flex justify-content-center align-items-start w-100"},
        html.table(
            {'class':"table table-striped"},
            html.thead(
                html.tr(
                    [html.th({'scope':"col"},j.capitalize()) for j in [k for (k,v) in items[0].items() if not isinstance(v,dict)]]
                )
            ),
            html.tbody(
                [html.tr(html.td(v) for(k,v) in i.items() if not isinstance(v,dict)) for i in items]
            )
        )
    )
    return layout;

