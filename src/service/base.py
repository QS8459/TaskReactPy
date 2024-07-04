from src.requester import APIRequests;
from src.config import settings;

class BaseRService(APIRequests):
    def __init__(self):
        self.url_v1:str = settings.endpoint.get_secret_value();
        self.payload:dict = {};