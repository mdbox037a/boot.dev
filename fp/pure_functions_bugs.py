default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line


def add_custom_command(commands, new_command, function):
    updated_commands = commands.copy()
    updated_commands[new_command] = function
    return updated_commands


def add_format(formats, format):
    updated_formats = formats.copy()
    updated_formats.append(format)
    return updated_formats


def save_document(docs, file_name, doc):
    updated_docs = docs.copy()
    updated_docs[file_name] = doc
    return updated_docs


def add_line_break(line):
    return line + "\n\n"
