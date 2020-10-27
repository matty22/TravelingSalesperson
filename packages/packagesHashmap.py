
# Define Package hashmap shape and methods
# --------------------------
class PackagesHashMap:
    # Init hash map
    # Space complexity: O(n)
    # Time complexity: O(1)
    def __init__(self):
        self.size = 21
        self.array = [None] * self.size

    # Create hash key
    # Space complexity: O(1)
    # Time complexity: O(1)
    def getHash(self, key):
        hash = key
        return hash

    # Return length of the hash map
    # Space complexity: O(1)
    # Time complexity: O(1)
    def __len__(self):
        return len(self.array)

    # Self-adjust size of hash map if more slots are needed
    # Space complexity: O(n)
    # Time complexity: O(n)
    def shouldResize(self):
        slotCounter = 1
        for slot in self.array:
            if slot is not None:
                slotCounter += 1
        if slotCounter > self.size / 2:
            self.array.append(None)

    # Add an element to the hash map
    # Space complexity: O(n)
    # Time complexity: O(n)
    def __setitem__(self, key, value):
        self.shouldResize()
        keyHash = self.getHash(key)
        if self.array[keyHash] is None:
            self.array[keyHash] = list([value])
            return True
        else:
            self.array[keyHash].append(value)
            return True

    # Fetch item from hash map
    # Space complexity: O(1)
    # Time complexity: O(1)
    def __getitem__(self, key):
        keyHash = self.getHash(key)
        if self.array[keyHash] is not None:
            return self.array[keyHash][0]
        else:
            return None

    # Instantiate hash map iterable
    # Space complexity: O(1)
    # Time complexity: O(1)
    def __iter__(self):
        return iter(self.array)

    # Iterate over hash map iterable
    # Space complexity: O(n)
    # Time complexity: O(n)
    def next(self):
        return next()

    # Print 1 package based on entered ID
    # Space complexity: O(1)
    # Time complexity: O(n)
    # --------------------------
    def printPackage(self, key):
        if not self.array[key]:
            print("Item has been deleted or does not exist")
            return
        for item in self.array[key]:
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

    # Print all packages' delivery status
    # Space complexity: O(n)
    # Time complexity: O(n)
    # --------------------------
    def printAllPackages(self):
        print("\n*************************************************************************************")
        print('{0:20}{1:20}{2}'.format("PACKAGE ID", "DEADLINE", "CURRENT STATUS"))
        print("*************************************************************************************")
        for item in self.array:
            if item is not None:
                print('{0:20}{1:20}{2}'.format(str(item[0].getId()), str(item[0].getDeadline()), str(item[0].getStatus())))
        print("*************************************************************************************\n")

