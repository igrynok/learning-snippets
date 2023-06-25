class HashMap:

    def __init__(self, size):
        self.size = size
        self.array = [None] * self.size

    def hash_code(self, value):
        hash_value = 5381
        for char in value:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.size

    def put(self, key_value):
        hash_key = self.hash_code(key_value[0])
        if self.array[hash_key]:
            self.array[hash_key].append(key_value)
        else:
            self.array[hash_key] = [key_value]

    def get(self, key):
        pass

    def update(self, key):
        pass

    def count(self):
        return sum([len(item) for item in self.array if item])

    def print_hashmap(self):
        print(self.array)


if __name__ == '__main__':
    hashmap = HashMap(5)
    hashmap.put(('John', 12))
    hashmap.put(('Billy', 15))
    hashmap.put(('Emily', 18))
    hashmap.put(('Daisy', 23))
    hashmap.put(('Philipp', 84))
    hashmap.print_hashmap()
    print(hashmap.count())
