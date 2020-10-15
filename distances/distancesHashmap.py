
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

    def getHash(self, key):
        hash = key
        return hash

    def addDistance(self, key, value):
        keyHash = self.getHash(key)
        keyValue = [key, value]

        if self.map[keyHash] is None:
            self.map[keyHash] = list([keyValue])
            return True
        else:
            self.map[keyHash].append(keyValue)
            return True

    def getDistance(self, key):
        keyHash = self.getHash(key)
        if self.map[keyHash] is not None:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def deleteDistance(self, key):
        keyHash = self.getHash(key)
        if self.map[keyHash] is None:
            return False
        for i in range(0, len(self.map[keyHash])):
            if self.map[keyHash][i][0] == key:
                self.map[keyHash].pop(i)
                return True

    def printDistancesHash(self):
        for item in self.map:
            if item is not None:
                print(str(item))

