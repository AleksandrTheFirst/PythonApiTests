import requests

method = ["GET", "POST", "PUT", "DELETE", "HEAD"]

for i in method:
    if i == "GET":
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=i)
        print(response.status_code)
        print(response.text)
    elif i == "POST":
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
        print(response.status_code)
        print(response.text)
    elif i == "PUT":
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
        print(response.status_code)
        print(response.text)
    elif i == "HEAD":
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
        print(response.status_code)
        print(response.text)
    elif i == "DELETE":
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
        print(response.status_code)
        print(response.text)
    else:
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
        print(response.status_code)
        print(response.text)

