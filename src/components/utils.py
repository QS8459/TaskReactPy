from src.requester import S;

def check_auth():
    if S.headers.get('Authorization'):
        return True;

    return False;


if __name__  == "__main__":
    print(check_auth());