import os

import Secrets


def main(**kwargs):

    _user = kwargs.get("user")
    _password = kwargs.get("password")
    print('Secret User:', _user)
    print('Secret Password:', _password, end='\n\n')

    with open(os.path.join(os.getcwd(), 'files', 'test.txt')) as f:
        print('ipsum lorem with bacon, because bacon makes everything better', end='\n\n')
        ipsum_lorem_data = f.read()
        print(ipsum_lorem_data)


if __name__ == "__main__":

    secrets = Secrets.Secrets.get_secrets()

    _user = secrets.get("TEST_USER")
    _password = secrets.get("TEST_PWD")

    kwargs = {"user": _user, "password": _password}

    main(**kwargs)
