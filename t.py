from random import randint, seed;
from src.service import TaskAPI
from src.requester import S;
import json;

from time import time;
client = TaskAPI();

seed(time());

def randomizer():
    summary = str(chr(randint(65,122)) + chr(randint(65,122)) + chr(randint(65,122)) + chr(randint(65,122)) + chr(randint(65,122)) + chr(randint(65,122)));
    title = str(chr(randint(65,122)) + chr(randint(65,122)) + chr(randint(65,122)) + chr(randint(65,122)) + chr(randint(65,122)) + chr(randint(65,122)));
    status = "ONGOING"
    return {
        'title': title,
        'summary': summary,
        'status': status
    };

def login():
    client.payload = {
        'username':"q.sardorbek8459@gmail.com",
        "password":"Sample_1!"
    }
    request = client.post_r(
        url = f"{client.url_v1}/account/login/",
        payload = client.payload
    );
    try:
        S.headers.update({"Authorization":f"Bearer {request.as_dict.get('token')}"});
        return True
    except ValueError:
        S.headers.update({"Authorization":"Bearer"});
    return False;

if __name__ == "__main__":
    print(login());


    request = client.get_r(
        url = f'{client.url_v1}/task/all/',
        param = {
            'perPage': 10,
            'page':1,
        }
    );
    print(request.as_dict);
    # print(request.as_dict.get('results'));

    #   for i in range(0,50):
    #     client.payload = randomizer();
    #     request = client.post_r(
    #         url = f"{client.url_v1}/task/add/",
    #         payload = json.dumps(client.payload)
    #     );
    #     print(request.as_dict);
    #     print(request.status_code);
