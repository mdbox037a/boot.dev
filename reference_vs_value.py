def add_format(default_formats, new_format):
    my_dictionary = default_formats.copy()
    my_dictionary[new_format] = True
    return my_dictionary


def remove_format(default_formats, old_format):
    my_dictionary = default_formats.copy()
    my_dictionary[old_format] = False
    return my_dictionary
