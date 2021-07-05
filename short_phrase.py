class ShortPhrase:
    def test_check_phrase(self):
        phrase = input("Set a phrase: ")
        phrase_len = len(phrase)
        if phrase_len < 15:
            assert len(phrase) < 15, f"The phrase = {phrase} is 15 symbols length or more."
