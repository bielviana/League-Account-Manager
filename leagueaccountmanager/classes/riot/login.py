from classes.riot.lcu import *
from requests import put as r_put



class Login():
    def __init__(self, username, password):
        lcu_info = LcuInfo()
        lcu_port = lcu_info.access_port
        lcu_endpoint = f'https://127.0.0.1:{lcu_port}/rso-auth/v1/session/credentials'
        lcu_password = lcu_info.remoting_auth_token
        lcu_user = 'riot'

        self.username = username
        self.password = password

        payload = {
            'username': self.username,
            'password': self.password,
            'persistLogin': False
        }
        response = r_put(lcu_endpoint, json=payload, verify=False, auth=(lcu_user, lcu_password))
        response_data = response.json()
        self.error = ''
        try:
            self.error = response_data['error']
        except:
            self.error = ''

        print(response_data)
        print(f"\nStatus code: {str(response.status_code)}")
        if response.status_code == 404:
            print(f'Error code: {response.status_code} | Connection error!')
            self.error = 'connection'
        elif response.status_code == 200 or response.status_code == 201:
            self.error = ''

    def check_error(self):
        return self.error
