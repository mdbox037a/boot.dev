def find_longest_word(document, longest_word=""):
    new_longest_word = longest_word
    working_document = document.split(maxsplit=1)
    if len(working_document) == 2:
        if len(working_document[0]) > len(new_longest_word):
            new_longest_word = working_document[0]
        return find_longest_word(working_document[1], new_longest_word)
    elif len(working_document) == 1:
        if len(working_document[0]) > len(new_longest_word):
            new_longest_word = working_document[0]
        return new_longest_word
    else:
        return ""
