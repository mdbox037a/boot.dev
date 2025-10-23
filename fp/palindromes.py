from functools import lru_cache


@lru_cache()
def is_palindrome(word):
    char_list = list(word)
    if len(char_list) == 0:
        return True
    elif (len(char_list) <= 2) and (char_list[0] == char_list[-1]):
        return True
    else:
        if char_list[0] == char_list[-1]:
            return is_palindrome("".join(char_list[1:-1]))
        else:
            return False
