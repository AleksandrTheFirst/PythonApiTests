from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):

    def setup(self):
        # REGISTER USER
        register_data = self.prepare_registration_data()
        response = MyRequests.post("/user", data=register_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        self.email = register_data['email']
        self.first_name = register_data['firstName']
        self.password = register_data['password']
        self.user_id = self.get_json_value(response, "id")

    def test_edit_just_created_user(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }

        response = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response, 'auth_sid')
        token = self.get_header(response, 'x-csrf-token')

        # EDIT USER
        new_name = "Changed Name"

        response1 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response1, 200)

    def test_edit_first_name_with_one_char(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response, 'auth_sid')
        token = self.get_header(response, 'x-csrf-token')

        # EDIT USER
        new_name = "C"

        response1 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response1, 400)
        Assertions.assert_json_has_key(response1, "error")
        response1_as_dict = response1.json()
        assert response1_as_dict['error'] == "Too short value for field firstName"

    def test_edit_email_for_created_user_negative(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response, 'auth_sid')
        token = self.get_header(response, 'x-csrf-token')

        # EDIT USER
        email = "Changed_email.ru"

        response1 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": email}
        )

        Assertions.assert_code_status(response1, 400)
        assert response1.content.decode("utf-8") == "Invalid email format"

        # GET USER
        response2 = MyRequests.get(
            f"/user/{self.user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}, )

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_value_by_email(
            response2,
            "email",
            self.email,
            "The email was changed!"
        )

    def test_edit_user_without_auth(self):
        # EDIT USER
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{self.user_id}",
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode(
            "utf-8") == f"Auth token not supplied", f"Unexpected response content {response3.content}"

    def test_edit_user1_with_user2_auth(self):
        # LOGIN BY CREATED USER 1
        login_data = {
            'email': self.email,
            'password': self.password
        }
        user1 = MyRequests.post("/user/login", data=login_data)
        Assertions.assert_code_status(user1, 200)

        # LOGIN BY USER 2
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response3 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response3, 'auth_sid')
        token = self.get_header(response3, 'x-csrf-token')

        user2 = MyRequests.get(f"/user/{self.user_id}")
        Assertions.assert_code_status(user2, 200)

        # EDIT USER 1 WITH USER 2 AUTH
        new_name = "Changed Name"

        response4 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response4, 400)
        assert response4.text == "Please, do not edit test users with ID 1, 2, 3, 4 or 5.", "There is another answer from last call in 'response4'."
