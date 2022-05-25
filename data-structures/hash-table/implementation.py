from hashlib import new


class hash_table():
    def __init__(self, size):
        self.size = size
        self.data = [None]*size

    def __str__(self):
        return str(vars(self))

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size
        return hash

    def get(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for data in self.data[hash]:
                if data[0] == key:
                    return data[1]
        return None

    def set(self, key, value):
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = [[key, value]]
        else:
            self.data[hash].append([key, value])

    def keys(self):
        keys = []
        for block in self.data:
            if block:
                for data in block:
                    if data:
                        keys.append(data[0])
        return keys

    def values(self):
        values = []
        for block in self.data:
            if block:
                for data in block:
                    if data:
                        values.append(data[1])
        return values


new_hash = hash_table(10)
new_hash.set("name", "Anuj")
new_hash.set("naae", "as")
new_hash.set("nae", "as4")
print(new_hash.get("name"))
print(new_hash.keys())
print(new_hash.values())
print(new_hash)
