class TestEx10:
    def test_ex10(self):
        phrase = input("Set a phrase: ")
        count = 0
        for n in phrase:
            count += 1
        assert count < 15