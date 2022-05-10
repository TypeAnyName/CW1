class BasicWord:
    def __init__(self, original_word, sub_words):
        self.original_word = original_word
        self.sub_words = sub_words

    def check_subword(self,answer):
        if answer in self.sub_words:
            return True
        else:
            return False

    def subwords_count(self):
        return len(self.sub_words)

    def __repr__(self):
        return f"{self.original_word.upper()}"
