import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

obj = response.json()

token = obj['token']
seconds = obj['seconds']
seconds_job_is_done = seconds + 1

time.sleep(seconds - 1)
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
obj = response.json()
status = obj['status']
print(status)

if status == "Job is NOT ready":
    time.sleep(2)
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
    obj = response.json()
    if obj['result'] == "42":
        if obj['status'] == "Job is ready":
            print(obj['status'])
else:
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
    obj = response.json()
    if obj['result'] == "42":
        if obj['status'] == "Job is ready":
            print(obj['status'])
        else:
            print("Job is NOT completed!")
    else:
        print("Result is NOT 42!")



