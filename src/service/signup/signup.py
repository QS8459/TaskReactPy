import json;
from src.service.base import BaseRService;



class Signup(BaseRService):
    def __init__(self):
        super().__init__();

    def signupR(self):
        return self.post_r(url = f"{self.url_v1}/account/signup/", payload = json.dump(self.payload))
