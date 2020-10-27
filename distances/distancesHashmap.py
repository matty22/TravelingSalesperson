
# Define distances hashmap shape and methods
# --------------------------
class DistancesHashMap:
    # Init hash map
    # Space complexity: O(n)
    # Time complexity: O(1)
    def __init__(self):
        self.size = 28
        self.array = [None] * self.size

    # Converts strings to floats or ints
    # Space complexity: O(1)
    # Time complexity: O(1)
    def __float__(self, string):
        if '.' in string:
            return float(string)
        else:
            return int(string)

    # Return length of hash map
    # Space complexity: O(1)
    # Time complexity: O(1)
    def __len__(self):
        return len(self.array)

    # Create hash key
    # Space complexity: O(1)
    # Time complexity: O(1)
    def getHash(self, key):
        hash = key
        return hash

    # Add an element to the hash map
    # Space complexity: O(n)
    # Time complexity: O(n)
    def __setitem__(self, key, address,  value):
        keyHash = self.getHash(key)
        if self.array[keyHash] is None:
            self.array[keyHash] = list([key, address, [value]])
            self.array[keyHash][2] = []
            return True
        else:
            self.array[keyHash][2].append(value)
            return True

    # Fetch element from hash map
    # Space complexity: O(1)
    # Time complexity: O(1)
    def __getitem__(self, item):
        keyHash = self.getHash(item)
        if self.array[keyHash] is not None:
            return self.array[item]
        return None

    # Instantiate hash map iterable
    # Space complexity: O(1)
    # Time complexity: O(1)
    def __iter__(self):
        self.num = 0
        return self

    # Iterate over hash map iterable
    # Space complexity: O(n)
    # Time complexity: O(n)
    def next(self):
        if self.num >= self.size:
            raise StopIteration
        self.num += 1
        return self.num

    # Print the distances hashmap
    # Space complexity: O(n)
    # Time complexity: O(n)
    # --------------------------
    def printDistancesHash(self):
        for item in self.array:
            if item is not None:
                print(str(item))

