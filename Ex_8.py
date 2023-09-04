import requests
import time
import json

job_not_ready = 'Job is NOT ready'
job_ready = 'Job is ready'

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
result = response1.json()
token = result.get('token')
finish_time = result.get('seconds')

if finish_time > 0:
    response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'token':token})
    print(response2.json())
    if (response2.json().get('status') == job_not_ready):
        print('Status is right')
    else:
        print('Status is wrong')

time.sleep(finish_time)
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'token':token})
print(response3.json())
if (response3.json().get('status') == job_ready)&(response3.json().get('result') is not None):
    print('Status and result are right')
else:
    print('Status is wrong')