class MaybeParsed:
    pass


# don't touch above this line


class Parsed(MaybeParsed):
    def __init__(self, doc_name, text):
        pass


class ParseError(MaybeParsed):
    def __init__(self, doc_name, err):
        pass
