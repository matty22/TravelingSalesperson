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

# Truck 2 is first truck to leave in the morning and returns to hub so driver can take truck 1
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

# Take address number as a string, and return the id of that current location address
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
def distanceToDestination(location, destination):
    return distances[destination][2][location]
