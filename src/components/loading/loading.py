from reactpy import html, component;
@component
def Loading():
    return html.div(
        {'class':"d-flex justify-content-center"},
        html.div(
            {"class":"spinner-border mx-auto", 'role': 'status'},
            html.span(
                {"class":"visually-hidden"},"Loading"
            )
        )
    )