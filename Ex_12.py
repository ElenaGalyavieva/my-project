import requests

class TestEx12:
    def test_ex12(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        some_header = response.headers
        print(some_header)

        assert response.status_code == 200, "Wrong response code"
        print(f'x-secret-homework-header: {some_header.get("x-secret-homework-header")}')
        assert "x-secret-homework-header" in some_header, "There is no field 'x-secret-homework-header' in the response"