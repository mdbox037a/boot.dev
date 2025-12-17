class Trie:
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for letter in sorted(dict.keys(current_level)):
            if letter != self.end_symbol:
                self.search_level(current_level[letter], current_prefix + letter, words)
        return words

    def words_with_prefix(self, prefix):
        matches = []
        current_level = self.root
        for char in prefix:
            if char not in current_level:
                return []
            current_level = current_level[char]
        return self.search_level(current_level, prefix, matches)

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True
