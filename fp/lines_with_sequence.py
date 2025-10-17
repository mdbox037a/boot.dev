def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            count = 0
            lines = doc.split()
            for line in lines:
                if sequence in line:
                    count += 1
            return count

        return with_length

    return with_char
