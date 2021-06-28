import requests

method = ["GET", "POST", "PUT", "DELETE"]

for i in method:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=i)
    print(f"This is GET request with parameter = {i}")
    print(response.status_code)
    print(response.text)
    print("\n")

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(f"This is POST request with parameter = {i}")
    print(response.status_code)
    print(response.text)
    print("\n")

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(f"This is PUT request with parameter = {i}")
    print(response.status_code)
    print(response.text)
    print("\n")

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(f"This is DELETE request with parameter = {i}")
    print(response.status_code)
    print(response.text)
    print("\n")

    response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(f"This is HEAD request with parameter = {i}")
    print(response.status_code)
    print(response.text)
    print("\n")

response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("This is PUT request without parameters.")
print(response.status_code)
print(response.text)


