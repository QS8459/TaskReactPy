from pydantic_settings import BaseSettings;
from pydantic import SecretStr;

from reactpy import html;
class Settings(BaseSettings):
    endpoint: SecretStr;

    class Config:
        env_file = ".env",
        env_file_encoding = 'utf-8'

settings = Settings();



BOOTSTRAP_CSS = html.link(
    {
        'rel': 'stylesheet',
        'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css',
        'integrity': 'sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH',
        'crossorigin': 'anonymous'
    }
);
BOOTSTRAP_SCRIPT = html.script(
    # {   'rel': 'manifest',
    #     'src': "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js",
    #     'integrity': 'sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy',
    #     'crossorigin': 'anonymous'
    # },
    {
        "src":"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js",
        # "integrity":"sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r",
        "crossorigin":"anonymous"
    }
);

LOCAL_STYLE = html.link({
    "href":"/static/stylesheet.css",
    "rel":"stylesheet"
})