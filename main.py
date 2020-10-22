# Christopher Leonard       StudentID: #001134335

from distances import importDistances
from packages import importPackages

# Import data from the distance and package CSV files
# Space complexity:
# Time complexity:
distances = importDistances.importFile()
packages = importPackages.importFile()


# Initialize and load trucks
# --------------------------

# Truck 1 waits for new address for package 9 and leaves at 10:20
# Space complexity:
# Time complexity:
truck1 = [packages[9], packages[2], packages[4], packages[5], packages[7], packages[8],
          packages[10], packages[11], packages[12], packages[17], packages[21], packages[22],
          packages[23], packages[24], packages[26], packages[27]]

# Truck 2 is first truck to leave in the morning and
# returns to hub before 10:20 so driver can take truck 1
# Space complexity:
# Time complexity:
truck2 = [packages[3], packages[18], packages[36], packages[38], packages[15],
          packages[14], packages[13], packages[16], packages[19], packages[20]]

# Truck 3 will leave at 9:05 when delayed packages arrive
# Space complexity:
# Time complexity:
truck3 = [packages[6], packages[25], packages[28], packages[32], packages[1], packages[29],
          packages[30], packages[31], packages[34], packages[37], packages[40], packages[33],
          packages[35], packages[39]]




# Helper Methods
# --------------

# Take address number as a string, and return the id of the current location address
# Space complexity:
# Time complexity:
def getCurrentLocationId(address):
    for index in range(len(distances)):
        if index > 0:
            if address == distances[index][1]:
                currentLocationId = distances[index][0]
                return int(currentLocationId - 1)


# Take address number as a string and return the id of that destination address
# Space complexity:
# Time complexity:
def getDestinationId(address):
    for index in range(len(distances)):
        if index > 0:
            if address == distances[index][1]:
                currentDestinationId = distances[index][0]
                return int(currentDestinationId)


# Take current location id and destination id, return the distance from
# current location to destination
# Space complexity:
# Time complexity:

# TODO: the thing works unless I add packages[38] to this truck
testTruck = [packages[3], packages[18], packages[36], packages[38]]
def distanceToDestination(location, destination):
    return float(distances[destination][2][location])

# TODO: account for packages with the same destination
# Start nearest neighbor algorithm
# Space complexity:
# Time complexity:
currentLocation = getCurrentLocationId('4001')          # Get current location id at hub
truckTotalDistance = 0
def findNearestNeighbor(truck, currentLocation, nearestNeighbor, truckTotalDistance):
    if len(truck) > 0:
        for package in truck: # {
            currentNearestNeighborDist = nearestNeighbor
            destination = getDestinationId(package.getAddress())    # Get destination id
            distanceToDest = distanceToDestination(currentLocation, destination)    # Calculate distance from location to destination
            if distanceToDest < currentNearestNeighborDist:          # Determine if current package is nearest neighbor
                currentNearestNeighborDist = distanceToDest
                currentLocation = getCurrentLocationId(package.getAddress())
            truckTotalDistance += currentNearestNeighborDist
        # }
            print("Remove package: " + str(package.getId()))
            truck.remove(package)
            print("Total distance covered by truck: " + str(truckTotalDistance))
        findNearestNeighbor(truck, currentLocation, currentNearestNeighborDist, truckTotalDistance)




findNearestNeighbor(testTruck, currentLocation, 100.0, truckTotalDistance)