from src.service.base import BaseRService;
import json

class Task(BaseRService):
    def __init__(self):
        super().__init__();

    def readTasks(self):
        return self.get_r(
            url = f"{self.url_v1}/task/all",
        );

