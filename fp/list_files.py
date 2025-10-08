def list_files(parent_directory, current_filepath=""):
    print(parent_directory, current_filepath)
    paths = []
    for key in parent_directory:
        new_filepath = current_filepath + "/" + key
        if parent_directory[key] is None:
            paths.append(new_filepath)
        else:
            paths.extend(list_files(parent_directory[key], new_filepath))
    return paths
