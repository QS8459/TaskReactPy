from reactpy import html, component, use_state, use_effect, event;
from pydantic.dataclasses import dataclass;
from src.main import client;


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
        padding: 1rem;
        border-radius: 10px;
    }
    .custom-table {
        background: rgba(255, 255, 255, 0.2); /* Transparent background */
        width: 100%;
    }
    .custom-table th, .custom-table td {
        padding: 10px;
        border: 0.5px solid rgba(255, 255, 255, 0.2);
        background-color: rgba(255, 255, 255, 0.2);
        text-align: center;
    }
    """
)




@dataclass
class ListProps():
    request_url:str;


@component
def List(props: ListProps):
    clk_id, set_clk_id = use_state(None);
    items, set_items = use_state([{}]);
    @event
    def on_click(id):
        set_clk_id(id);
        print("This is just clk_id",clk_id);
        setattr(client,"clk_id",clk_id);
        print("This is client clk_id",client.clk_id);

    @use_effect
    def request():
        try:
            set_items(client.get_r(
                url = f'{client.url_v1}/{props.request_url}'
            ).as_dict);

        except Exception:
            pass
    layout = html._(
        local_style,
        html.div(
        {'class':"d-flex justify-content-center align-items-start w-100 mt-5"},
        html.table(
            {'class':"table custom-table"},
            html.thead(
                {'class':"thead-dark"},
                html.tr(
                    html.th({'scope':"col"}, 'id'),
                    [html.th({'scope':"col"},j.capitalize()) for j in [k for (k,v) in items[0].items() if not isinstance(v,dict) and k != "id"]]
                )
            ),
            html.tbody(

                [
                    html.tr(
                        html.td(html.a(
                            {
                                "onclick": lambda _: set_clk_id(i.get('id')),
                                'href':"#"
                             },
                            i.get('id')
                        )),
                        [html.td(v) for (k, v) in i.items() if not isinstance(v, dict) and k != 'id']
                    )
                    for i in items
                ]
                # [html.tr(html.td(i.get('id'))) for i in items],
                # [html.tr(html.td(v) for(k,v) in i.items() if not isinstance(v,dict) and k !='id') for i in items]
            )
        )
    ))
    print(clk_id);
    return layout;

