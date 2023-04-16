def get_index(data_list, a_string):
        result = 0

        for a_character in a_string:
            a_number = ord(a_character)
            result += a_number

        list_index = result % len(data_list)
        return list_index

class BasicHashTable:
    def __init__(self, max_size):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size

    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list,key)

        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key,value

    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list,key)

        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list,key)

        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key, value

    def list_all(self):
        # 1. Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]

basic_table = BasicHashTable(max_size=1024)
print(len(basic_table.data_list))
# Insert some values
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')

# Find a value
print(basic_table.find('Hemanth'))

# Update a value
basic_table.update('Aakash', '7777777777')

# Check the updated value
print(basic_table.find('Aakash'))

# Get the list of keys
print(basic_table.list_all())