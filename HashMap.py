class HashMap:
    def __init__(self):
        self.size = 10
        self.map = []
        for i in range(self.size):
            self.map.append([])

    def get_hash(self, key):
        package_hash = int(key)
        return package_hash % self.size

    #Insert function that takes the package ID as input and inserts each of the data components of the package
    #into the hash table
    def insert(self, key, value):
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

    #Look-up function that takes the packageID as input and returns each of the package data components
    def lookup(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for kv_pair in self.map[key_hash]:
                if kv_pair[0] == key:
                    return kv_pair[1]
        return None

    def __str__(self) -> str:
        return "".join(str(item) for item in self.map)