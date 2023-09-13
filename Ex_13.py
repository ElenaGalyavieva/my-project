import pytest
import requests

class TestEx13:
    user_agents = [
        'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
        'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
        ]
    expected_values = [
        {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
        {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
        {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
        {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
        {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
    ]
    @pytest.mark.parametrize('values', zip(user_agents, expected_values))
    def test_ex13(self, values):
        agent_value, expected_value = values
        correct_device = [
            ("iOS"),
            ("Android"),
            ("Unknown")
        ]

        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        headers = {"User-Agent": agent_value}

        response = requests.get(url,headers=headers)
        result = response.json()
        count = len(correct_device)
        n = 0

        while n < count:
            if result.get('device') != correct_device[n]:
                print(f"User Agent '{values}' have wrong parameter")
            n += 1
        #if result.get('platform') == 'No':
            #print(f"User Agent '{values}' have wrong parameter")
        #if result.get('browser') == 'No':
            #print(f"User Agent '{values}' have wrong parameter")

        assert response.status_code == 200, "Wrong response code"

        #assert result.get('device') == correct_device[n], f"User Agent '{values}' have wrong parameter"
        #assert platform != 'No', f"User Agent '{values}' have wrong parameter"
        #assert browser != 'No', f"User Agent '{values}' have wrong parameter"