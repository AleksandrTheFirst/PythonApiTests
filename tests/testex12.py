import requests


class TestEx12:
    def test_ex_12(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        obj = dict(response.headers)
        print("\n")
        print(obj)
        key = "x-secret-homework-header"
        obj = obj.get(key)
        assert obj is not None, f"There is no key with name = {key}"
        assert obj == "Some secret value", f"Header {key} with value {obj} not found."
