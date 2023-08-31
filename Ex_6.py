import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
count = 0
for n in response.history:
    count += 1

print("Конечный url: ", response.url)
print("Количество редиректов:", count)