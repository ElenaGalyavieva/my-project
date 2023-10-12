import string
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import random

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/",
            data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login",
            data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"
        response3 = MyRequests.put(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
            )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )

    def test_edit_not_authorisation_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response5 = MyRequests.post("/user/",
            data=register_data)

        Assertions.assert_code_status(response5, 200)
        Assertions.assert_json_has_key(response5, "id")

        user_id = self.get_json_value(response5, "id")

        # EDIT
        new_name = "New Name"
        response6 = MyRequests.put(f"/user/{user_id}",
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response6, 400)

    def test_edit_by_another_user(self):
        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response7 = MyRequests.post("/user/login",
            data=login_data)
        auth_sid = self.get_cookie(response7, "auth_sid")
        token = self.get_header(response7, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"
        response8 = MyRequests.put("/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response8, 400)

    def test_change_to_incorrect_email(self):
        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response9 = MyRequests.post("/user/login",
            data=login_data)
        auth_sid = self.get_cookie(response9, "auth_sid")
        token = self.get_header(response9, "x-csrf-token")

        # EDIT
        new_email = "vinkotov.example.com"
        response10 = MyRequests.put("/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email}
        )

        Assertions.assert_code_status(response10, 400)

    def test_edit_short_name(self):
        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response11 = MyRequests.post("/user/login",
            data=login_data)
        auth_sid = self.get_cookie(response11, "auth_sid")
        token = self.get_header(response11, "x-csrf-token")

        # EDIT
        new_name = ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase, 1))
        response12 = MyRequests.put("/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response12, 400)