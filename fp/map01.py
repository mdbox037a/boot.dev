def change_bullet_style(document):
    line_list = document.split("\n")
    fixed_lines = map(convert_line, line_list)
    return "\n".join(fixed_lines)


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
