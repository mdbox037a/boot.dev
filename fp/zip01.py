valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(doc_names, doc_formats):
    # raw_pairs = list(zip(doc_names, doc_formats))
    # final_pairs = []
    # for pair in raw_pairs:
    #    if pair[1] in valid_formats:
    #        final_pairs.append(pair)
    # return final_pairs

    raw_pairs = list(zip(doc_names, doc_formats))
    return list(filter(lambda pair: pair[1] in valid_formats, raw_pairs))
