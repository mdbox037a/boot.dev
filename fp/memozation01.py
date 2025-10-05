def word_count_memo(document, memos):
    updated_memos = memos.copy()
    if document in updated_memos:
        return updated_memos[document], updated_memos
    else:
        updated_memos[document] = word_count(document)
        return word_count(document), updated_memos


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
