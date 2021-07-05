import requests


class TestEx11:
    def test_ex11(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(f"This is response: {response.cookies}")
        obj = dict(response.cookies)
        cookie_value = obj["HomeWork"]
        assert obj["HomeWork"] == cookie_value, "The cookie with name 'HomeWork' doesn't have value 'hw_value'!"
