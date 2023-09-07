import pytest
import requests

class TestEx11:
    def test_ex11(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        some_cookie = response.cookies
        print(some_cookie)
        assert response.status_code == 200, "Wrong response code"

        assert "HomeWork" in some_cookie, "There is no field 'HomeWork' in the response"