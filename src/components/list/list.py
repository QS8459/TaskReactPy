from reactpy import html, component, use_state, use_effect, event;
from pydantic.dataclasses import dataclass;
from src.main import client;
from src.components.pagination.pagination import PaginationProps, Pagination;

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
    items, set_items = use_state([{}]);
    page, set_page = use_state(1);
    perPage = 10;
    total_items, set_total_items = use_state(0);
    total_pages, set_total_pages = use_state(0);


    @use_effect
    def request():
        nonlocal total_items, total_pages
        try:
            r = client.get_r(
                url = f'{client.url_v1}/{props.request_url}',
                param = {
                    'page':page,
                    'perPage':perPage
                }
            ).as_dict
            set_items(r.get('results'));
            set_total_items(r.get('count'));
            set_total_pages((total_items + perPage - 1) // perPage);
        except Exception as e:
            print("This is exception", e);
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
                        {
                            "onclick": lambda task_id=i['id']: print(task_id.keys()),
                            'cursor': 'pointer',
                        },
                        html.td(

                            i.get('id')
                        ),
                        [html.td(v) for (k, v) in i.items() if not isinstance(v, dict) and k != 'id']
                    )
                    for i in items
                ]
                # [html.tr(html.td(i.get('id'))) for i in items],
                # [html.tr(html.td(v) for(k,v) in i.items() if not isinstance(v,dict) and k !='id') for i in items]
                )
            ),
        ),
            Pagination(PaginationProps(page = page,set_page = set_page,totalPages = total_pages))
    )
    return layout;

