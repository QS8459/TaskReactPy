from dataclasses import dataclass;
from requests import Session;
S = Session();

@dataclass
class APIResponse:
    status_code: int;
    as_dict: dict;
    url: str;
    text: str;
    session: Session;


class APIRequests:

    def post_r(self, url:str, payload:dict = {}, param:dict|None = None):
        request = S.post(url = url, data = payload, params = param);
        return self._object(request)

    def get_r(self, url:str, param:dict|None = None):
        return self._object(S.get(url = url, params = param ));
    @staticmethod
    def _object(r):

        status_code:int = r.status_code;
        url:str = r.url;
        try:

            as_dict:object= r.json();
        except ValueError:
            as_dict:dict = {}
        text = r.text;
        return APIResponse(status_code= status_code, url = url, as_dict=as_dict, session = r, text = text);


