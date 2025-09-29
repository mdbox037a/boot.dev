def remove_invalid_lines(document):
    lines_list = document.split("\n")
    filtered_list = filter(lambda line: not line.startswith("-"), lines_list)
    return "\n".join(filtered_list)
