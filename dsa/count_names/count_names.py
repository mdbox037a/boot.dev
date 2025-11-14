def count_names(list_of_lists, target_name):
    count = 0
    combined = []
    for names_list in list_of_lists:
        combined.extend(names_list)
    for i in combined:
        if i == target_name:
            count += 1
    return count
