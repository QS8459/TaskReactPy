from src.requester import S;

def check_auth():
    if S.headers.get('Authorization'):
        return True;

    return False;

def logout():
    try:
        S.headers.pop("Authorization");
        return True;
    except Exception:
        return "Something went wrong while logout!";
    