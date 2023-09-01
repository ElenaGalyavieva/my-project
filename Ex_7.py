import requests
from json.decoder import JSONDecodeError

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("1. http-запрос без параметра method выдает:", response1.text)

payload1 = {"method": "HEAD"}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = payload1)
print("2. http-запрос не из списка выдает:", response2.text)

payload2 = {"method": "GET"}
response3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = payload2)
print("3. Запрос с правильным значением method выдает:", response3.text)

parameters_methods = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]
m = 0
print("4. Ответ на 4 вопрос:")
while m < 4:
    result = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=parameters_methods[m])
    print(f"Метод GET с params={parameters_methods[m]} возвращает {result} со статус кодом {result.status_code}")
    result = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=parameters_methods[m])
    print(f"Метод POST с data={parameters_methods[m]} возвращает {result} со статус кодом {result.status_code}")
    result = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=parameters_methods[m])
    print(f"Метод PUT с data={parameters_methods[m]} возвращает {result} со статус кодом {result.status_code}")
    result = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=parameters_methods[m])
    print(f"Метод DELETE с data={parameters_methods[m]} возвращает {result} со статус кодом {result.status_code}")
    m += 1
