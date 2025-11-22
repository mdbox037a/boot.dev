def power_set(input):
    empty_list = []
    if len(input) == 0:
        result = [empty_list]
        return result
    else:
        all_subsets = [empty_list]
        for i in input:
            new_subsets = []
            for subset in all_subsets:
                new_subset = subset + [i]
                new_subsets.append(new_subset)
            all_subsets.extend(new_subsets)
        return all_subsets
