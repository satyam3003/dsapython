class HashTable:
    def __init__(self):
        self.table = [None] * 100000

    def store(self, string):
        hash_value = self.calc_hashvalue(string)
        if hash_value != -1:
            if self.table[hash_value] is None:
                self.table[hash_value] = [string]
            else:
                self.table[hash_value].append(string)

    def lookup(self, string):
        hash_value = self.calc_hashvalue(string)
        if hash_value != -1:
            if self.table[hash_value] is not None:
                return self.table[hash_value]
        return -1

    def calc_hashvalue(self, string):
        value = ord(string[0]) * 100 + ord(string[1])
        return value


hashtable = HashTable()

print(hashtable.calc_hashvalue('sat'))
print(hashtable.lookup('sat'))