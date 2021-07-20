from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserDelete(BaseCase):
    def test_cannot_delete_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = MyRequests.post("/user/login", data=data)
        id = self.get_json_value(response, "user_id")
        response1 = MyRequests.delete(f"/user/{id}")
        Assertions.assert_code_status(response1, 404)
        assert response1.content.decode("utf-8") == "This is 404 error!\n<a href='/'>Home</a>", "Expected response is different"

    def test_delete_user(self):
        data = self.prepare_registration_data()
        # CREATE USER
        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
        self.email = data['email']
        self.password = data['password']
        id = self.get_json_value(response, "id")

        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response1 = MyRequests.post("/user/login", data=login_data)
        Assertions.assert_code_status(response1, 200)
        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')

        # DELETE USER
        response2 = MyRequests.delete(f"/user/{id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )
        Assertions.assert_code_status(response2, 200)

        response3 = MyRequests.get(f"/user/{id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_code_status(response3, 404)
        assert response3.content.decode("utf-8") == "User not found", "It's seems user not deleted."

    def test_delete_user_by_another_user(self):
        # REGISTER USER 1
        register_data = self.prepare_registration_data()
        response = MyRequests.post("/user", data=register_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        self.email = register_data['email']
        self.first_name = register_data['firstName']
        self.password = register_data['password']
        user_id = self.get_json_value(response, "id")

        # LOGIN BY USER 2
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')

        # DELETE USER 1
        response2 = MyRequests.delete(f"/user/{user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )
        Assertions.assert_code_status(response2, 400)
        assert response2.text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5.", "The answer is different in response2"


