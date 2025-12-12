class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return
        elif self.current_load() < 0.05:
            return
        else:
            tmp = self.hashmap
            self.hashmap = [None] * (10 * len(tmp))
            for k in tmp:
                if k:
                    self.insert(k[0], k[1])

    def current_load(self):
        filled_buckets = 0
        for bucket in self.hashmap:
            if bucket:
                filled_buckets = filled_buckets + 1
        if len(self.hashmap) == 0:
            return 1
        else:
            return filled_buckets / len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
