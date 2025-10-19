def new_resizer(max_width, max_height):
    def set_min(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def resize(width, height):
            new_width = max(min(width, max_width), min_width)
            new_height = max(min(height, max_height), min_height)
            return new_width, new_height

        return resize

    return set_min
