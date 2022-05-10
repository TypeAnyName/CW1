class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.used_subwords = []

    def __repr__(self):
        return self.player_name

    def correct_subwords(self, word):
        self.used_subwords.append(word)

    def has_used(self, word):
        if word in self.used_subwords:
            return True

    def lenght_of_used_list(self):
        return len(self.used_subwords)
