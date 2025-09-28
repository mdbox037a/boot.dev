def file_type_getter(file_extension_tuples):
    file_type_dictionary = {}
    for entry in file_extension_tuples:
        for extension in entry[1]:
            file_type_dictionary[extension] = entry[0]
    # print(file_type_dictionary)
    return lambda ext: file_type_dictionary.get(ext, "Unknown")
