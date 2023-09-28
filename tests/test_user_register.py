import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):
    exclude_parameter = [
        ('no_password'),
        ('no_username'),
        ('no_firstName'),
        ('no_lastName'),
        ('no_email')
    ]

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = requests.post("https://playground.learnqa.ru/api/user/",
                                 data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = requests.post("https://playground.learnqa.ru/api/user/",
                                 data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_incorrect_email(self):
        data = self.prepare_registration_data_without()

        response = requests.post("https://playground.learnqa.ru/api/user/",
                                 data=data)
        assert response.content.decode("utf-8") == "Invalid email format", f"Unexpected response content {response.content}"
        Assertions.assert_code_status(response, 400)

    @pytest.mark.parametrize('param', exclude_parameter)
    def test_has_no_one_parameter(self, param):
        register_data = self.prepare_registration_data()
        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        username = register_data['username']
        last_name = register_data['lastName']
        if param == 'no_password':
            data1 = {'username': username,
                     'firstName': first_name,
                     'lastName': last_name,
                     'email': email}
            response1 = requests.post("https://playground.learnqa.ru/api/user/",
                                     data=data1)
            Assertions.assert_code_status(response1, 400)
        elif param == 'no_username':
            data2 = {'password': password,
                     'firstName': first_name,
                     'lastName': last_name,
                     'email': email}
            response2 = requests.post("https://playground.learnqa.ru/api/user/",
                                     data=data2)
            Assertions.assert_code_status(response2, 400)
        elif param == 'no_firstName':
            data3 = {'username': username,
                     'password': password,
                     'lastName': last_name,
                     'email': email}
            response3 = requests.post("https://playground.learnqa.ru/api/user/",
                                     data=data3)
            Assertions.assert_code_status(response3, 400)
        elif param == 'no_lastName':
            data4 = {'username': username,
                     'password': password,
                     'firstName': first_name,
                     'email': email}
            response4 = requests.post("https://playground.learnqa.ru/api/user/",
                                     data=data4)
            Assertions.assert_code_status(response4, 400)
        elif param == 'no_email':
            data5 = {'username': username,
                     'password': password,
                     'firstName': first_name,
                     'lastName': last_name}
            response5 = requests.post("https://playground.learnqa.ru/api/user/",
                                     data=data5)
            Assertions.assert_code_status(response5, 400)

    def test_short_pass(self):
        data = self.prepare_registration_short_username()
        response6 = requests.post(
            "https://playground.learnqa.ru/api/user/",
            data=data)
        Assertions.assert_code_status(response6, 400)

    def test_long_username(self):
        data = self.prepare_registration_long_username()
        response7 = requests.post(
            "https://playground.learnqa.ru/api/user/",
            data=data)
        print(response7.status_code)
        Assertions.assert_code_status(response7, 200)