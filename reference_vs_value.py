def add_format(default_formats, new_format):
    new_dictionary = default_formats.copy()
    new_dictionary[new_format] = True
    return new_dictionary


def remove_format(default_formats, old_format):
    new_dictionary = default_formats.copy()
    new_dictionary[old_format] = False
    return new_dictionary
