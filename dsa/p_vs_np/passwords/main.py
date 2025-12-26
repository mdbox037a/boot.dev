def get_num_guesses(length):
    char_set_size = 26
    counter = 1
    num_guesses = 0
    while counter < (length + 1):
        num_guesses += char_set_size**counter
        counter += 1
    return num_guesses
