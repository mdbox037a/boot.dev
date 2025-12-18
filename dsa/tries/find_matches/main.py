class Trie:
    def find_matches(self, document):
        matches = set()
        for outer_index in range(len(document)):
            current_level = self.root
            for inner_index in range(outer_index, len(document)):
                if document[inner_index] not in current_level:
                    break
                else:
                    current_level = current_level[document[inner_index]]

                if self.end_symbol in current_level:
                    matches.add(document[outer_index : inner_index + 1])
        return matches

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
