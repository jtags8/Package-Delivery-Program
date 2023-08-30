class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [] * self.size

    def get_hash(self, key):
        hash = 0
        for i in key:
            hash += key
        return hash % self.size

    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for kv_pair in self.map[key_hash]:
                if kv_pair[0] == key:
                    kv_pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        return True
    def remove(self, key):
        return True