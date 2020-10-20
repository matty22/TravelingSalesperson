
# Define distances hashmap shape and methods
class DistancesHashMap:
    def __init__(self):
        self.size = 28
        self.map = [None] * self.size

    def __float__(self, string):
        if '.' in string:
            return float(string)
        else:
            return int(string)

    def __len__(self):
        return 28

    def getHash(self, key):
        hash = key
        return hash

    def __setitem__(self, key, address,  value):
        keyHash = self.getHash(key)

        if self.map[keyHash] is None:
            self.map[keyHash] = list([key, address, [value]])
            self.map[keyHash][2] = []
            return True
        else:
            self.map[keyHash][2].append(value)
            return True

    def __getitem__(self, item):
        keyHash = self.getHash(item)
        if self.map[keyHash] is not None:
            return self.map[item]
        return None

    def __iter__(self):
        self.num = 0
        return self

    def next(self):
        if self.num >= self.size:
            raise StopIteration
        self.num += 1
        return self.num

    def printDistancesHash(self):
        for item in self.map:
            if item is not None:
                print(str(item))

