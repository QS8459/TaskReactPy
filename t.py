import os;
import json;

if __name__ == "__main__":
    with open(f'{os.getcwd()}/src/utils/bootstrap/bootstrap.json', 'r') as f:
        file = json.load(f);

    BOOTSTRAP_CSS = file.get('link');
    BOOTSTRAP_SCRIPT = file.get('script');
    print(BOOTSTRAP_CSS);
    print();
    print(BOOTSTRAP_SCRIPT);