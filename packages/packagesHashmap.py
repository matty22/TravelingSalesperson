
# Define Package hashmap shape and methods
class PackagesHashMap:
    def __init__(self):
        self.size = 41
        self.map = [None] * self.size

    def getHash(self, key):
        hash = key
        return hash

    def __setitem__(self, key, value):
        keyHash = self.getHash(key)
        keyValue = value
        if self.map[keyHash] is None:
            self.map[keyHash] = list([keyValue])
            return True
        else:
            self.map[keyHash].append(keyValue)
            return True

    def __getitem__(self, key):
        keyHash = self.getHash(key)
        return self.map[keyHash]

    def printPackagesHash(self, key):
        for item in self.map[key]:
            if item is not None:
                print(item.getId())
                print(item.getAddress())
                print(item.getDeadline())
                print(item.getCity())
                print(item.getZip())
                print(item.getMass())
                print(item.getStatus())

