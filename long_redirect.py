import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
count = 0

for i in response.history:
    print(response.url)
    count += 1

print(f"There is {count} redirects")
