
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
        if self.map[keyHash] is None:
            self.map[keyHash] = list([value])
            return True
        else:
            self.map[keyHash].append(value)
            return True

    def __getitem__(self, key):
        keyHash = self.getHash(key)
        return self.map[keyHash][0]

    def __delitem__(self, key):
        keyHash = self.getHash(key)
        del self.map[keyHash][0]

    def __iter__(self):
        return iter(self.map)

    def next(self):
        return next()

    def printPackage(self, key):
        if not self.map[key]:
            print("Item has been deleted or does not exist")
            return
        for item in self.map[key]:
            if item.getId() == key:
                if item is not None:
                    print("\n***********************************")
                    print("ID: " + str(item.getId()))
                    print("Address: " + item.getAddress())
                    print("City: " + item.getCity())
                    print("State: " + item.getState())
                    print("Zip: " + item.getZip())
                    print("Deadline: " + item.getDeadline())
                    print("Mass: " + item.getMass())
                    print("Status: " + item.getStatus())
                    print("***********************************\n")

    def printAllPackages(self):
        print("\n*************************************************************************************")
        print('{0:20}{1:20}{2}'.format("PACKAGE ID", "DEADLINE", "CURRENT STATUS"))
        print("*************************************************************************************")
        for item in self.map:
            if item is not None:
                print('{0:20}{1:20}{2}'.format(str(item[0].getId()), str(item[0].getDeadline()), str(item[0].getStatus())))
        print("*************************************************************************************\n")

