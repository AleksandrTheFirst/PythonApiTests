import requests


class TestEx13:

    def test_env_ex13_1(self):
        env = {"platform": "Mobile", "browser": "No", "device": "Android"}
        user_agent = ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F)AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
        data = {'User-Agent': user_agent}
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=data)
        assert response.status_code == 200
        response = response.json()
        print("\n")
        print(response)
        assert response['platform'] == env['platform']
        assert response['browser'] == env['browser']
        assert response['device'] == env['device']

    def test_env_ex13_2(self):
        env = {"platform": "Mobile", "browser": "Chrome", "device": "iOS"}
        user_agent = ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1")
        data = {'User-Agent': user_agent}
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=data)
        assert response.status_code == 200
        response = response.json()
        print("\n")
        print(response)
        assert response['platform'] == env['platform']
        assert response['browser'] == env['browser']
        assert response['device'] == env['device']

    def test_env_ex13_3(self):
        env = {"platform": "Googlebot", "browser": "Unknown", "device": "Unknown"}
        user_agent = ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        data = {'User-Agent': user_agent}
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=data)
        assert response.status_code == 200
        response = response.json()
        print("\n")
        print(response)
        assert response['platform'] == env['platform']
        assert response['browser'] == env['browser']
        assert response['device'] == env['device']

    def test_env_ex13_4(self):
        env = {"platform": "Web", "browser": "Chrome", "device": "No"}
        user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0")
        data = {'User-Agent': user_agent}
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=data)
        assert response.status_code == 200
        response = response.json()
        print("\n")
        print(response)
        assert response['platform'] == env['platform']
        assert response['browser'] == env['browser']
        assert response['device'] == env['device']

    def test_env_ex13_5(self):
        env = {"platform": "Mobile", "browser": "No", "device": "iPhone"}
        user_agent = ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
        data = {'User-Agent': user_agent}
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=data)
        assert response.status_code == 200
        response = response.json()
        print("\n")
        print(response)
        assert response['platform'] == env['platform']
        assert response['browser'] == env['browser']
        assert response['device'] == env['device']
