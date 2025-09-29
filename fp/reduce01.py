import functools


def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    else:
        sentence_list = sentences[0:n]
        joined = functools.reduce(join, sentence_list)
        return joined + "."
