def remove_emphasis_from_word(word):
    return word.strip("*")


def remove_emphasis_from_line(line):
    words = line.split()
    clean_words = map(remove_emphasis_from_word, words)
    return " ".join(clean_words)


def remove_emphasis(doc_content):
    lines = doc_content.split("\n")
    return "\n".join(map(remove_emphasis_from_line, lines))
