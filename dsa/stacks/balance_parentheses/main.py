from stack import Stack


def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char == "(":
            stack.push(char)
        elif char == ")" and stack.size() == 0:
            stack.push(char)
        elif char == ")":
            stack.pop()
    if stack.size() != 0:
        return False
    else:
        return True
