class Secrets:

    @staticmethod
    def get_secrets() -> dict:
        # CI/CD build using file replacement
        # secrets = dict()
        # secrets['TEST_USER'] = {TEST_USER}
        # secrets['TEST_PWD'] = {TEST_PWD}
        # return secrets

        # local testing
        secrets = dict()
        secrets['TEST_USER'] = 'someuser'
        secrets['TEST_PWD'] = 'somepass'
        return secrets