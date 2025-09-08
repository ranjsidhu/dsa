class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        return my_hash

    def print_table(self):
        print("\n")
        print("--------- Printing HT starts ---------")
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
        print("--------- Printing HT ends ---------")
        print("\n")

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        accessed_index = self.data_map[index]
        if accessed_index is not None:
            for pair in accessed_index:
                if pair[0] == key:
                    return pair[1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            accessed_index = self.data_map[i]
            if accessed_index is not None:
                for j in range(len(accessed_index)):
                    all_keys.append(accessed_index[j][0])

        return all_keys
