import pytest
import requests

class TestEx13:
    device = [
        ("Android"),
        ("IOS"),
        ("Unknown")
    ]
    browser = [
        ("Chrome"),
        ("Firefox"),
        ("Unknown")
    ]
    platform = [
        ("Mobile"),
        ("Web"),
        ("Unknown")
    ]
    user_agent = [platform, browser, device]

    def test_ex13(self, user_agent):

