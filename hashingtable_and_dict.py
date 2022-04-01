my_dict = {
    'Satyam': '8983517226',
    'Smritu': '881882995',
    'Meow': '7720001926',
    'Pappa': '9834510723'
}

print(my_dict)
print(my_dict['Satyam'])

# Python dicts are form by hash table.

# Create a hash table
data_list = [None] * 4084


# every element in dict is hashed to get the corresponding key value pair and save it in data
# Lets make a hash

def getindex(get_list, word):
    result = 0
    for letter in word:
        result += ord(letter)  # this returns a hash for alphabet.

    list_index = result % len(get_list)
    return list_index


# setting an element
key, value = 'Aakash', '7878787878'
idx = getindex(data_list, 'Aakash')
data_list[idx] = (key, value)

# or
key, value = 'Satyam', '8983517226'
data_list[getindex(data_list, key)] = (key, value)

# getting element from
key, value = (data_list[getindex(data_list, 'Aakash')])
print(f"get_element = {value}")

list = [x[0] for x in data_list if x is not None]
print(list)


class BasicHastTable:
    def __init__(self, max_size=4084):
        self.data_list = [None] * max_size

    def insert(self, key, value):
        self.data_list[getindex(self.data_list, key)] = key, value

    def find(self, key):

        idx = getindex(self.data_list, key)
        kv = data_list[idx]
        if kv is not None:
            key, value = kv
            return value
        else:
            return None

    def list_all(self):
        return [x[0] for x in self.data_list if x is not None]


hashtable1 = BasicHastTable()
hashtable1.insert('Satyam', '8983517226')
hashtable1.insert('Satyam', '7226')
hashtable1.insert('Smritu', '881882995')
hashtable1.insert('Meow', '7720001926')
hashtable1.insert('Pappa', '7722007399')

print(hashtable1.find('maytaS'))
print(hashtable1.list_all())


# but if we store key as it and ti it will be hashed same and value will be overwritter to avoide this we use Linear Probing method
# in this method we shift the idx until we get an empty location or location where the key is same.
print("\n\nPrevent overwritiong by Linear probing")

def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = getindex(data_list, key)

    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]

        # If it is None, return the index
        if kv is None:
            return idx

        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx

        # Move to the next index
        idx += 1

        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0


def find_valid_index(data_list, key):
    idx = getindex(data_list, key)

    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]
        # If it is None, return the index
        # If the stored key matches the given key, return the index
        if kv is None:
            return None
        k, v = kv
        if k == key:
            return idx

        # Move to the next index
        idx += 1

        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0


class CollisionHandelingHastTable:
    def __init__(self, max_size=4084):
        self.data_list = [None] * max_size

    def insert(self, key, value):
        self.data_list[get_valid_index(self.data_list, key)] = key, value
        # print(get_valid_index(self.data_list, key))

    def find(self, key):
        idx = get_valid_index(self.data_list, key)
        kv = self.data_list[idx]
        if kv is not None:
            key, value = kv
            return value
        else:
            return None

    def list_all(self):
        return [x[0] for x in self.data_list if x is not None]


hashtable2 = CollisionHandelingHastTable()
hashtable2.insert('abc', '8983517226')
hashtable2.insert('cab', '7226')
hashtable2.insert('bca', '7226')

print(hashtable2.find('abc'))
print(hashtable2.find('cab'))
print(hashtable2.find('bca'))

print(hashtable2.list_all())
