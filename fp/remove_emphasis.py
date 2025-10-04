def remove_emphasis_from_word(word):
    return word.strip("*")


def remove_emphasis_from_line(line):
    function_line = line
    words = function_line.split()
    clean_words = map(remove_emphasis_from_word, words)
    return " ".join(clean_words)


def remove_emphasis(doc_content):
    function_content = doc_content
    lines = function_content.split("\n")
    clean_doc = "\n".join(map(remove_emphasis_from_line, lines))
    return clean_doc
