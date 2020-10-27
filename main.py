# Christopher Leonard       StudentID: #001134335

from distances import importDistances
from packages import importPackages
from datetime import datetime, timedelta



# Import data from the distance and package CSV files
# Space complexity:
# Time complexity:
distances = importDistances.importFile()
packages = importPackages.importFile()


# Initialize and load trucks
# --------------------------
truck1 = [packages[9], packages[2], packages[4], packages[5], packages[7], packages[8],
          packages[10], packages[11], packages[12], packages[17], packages[21], packages[22],
          packages[23], packages[24], packages[26], packages[27]]

truck2 = [packages[3], packages[18], packages[36], packages[38], packages[15], packages[37],
          packages[14], packages[13], packages[16], packages[19], packages[20], packages[30]]

truck3 = [packages[6], packages[25], packages[28], packages[32], packages[1], packages[29],
          packages[31], packages[34], packages[40], packages[33], packages[35], packages[39]]


# Take address number as a string, and return the id of the current location address
# Space complexity:
# Time complexity:
def getCurrentLocationId(address):
    for index in range(len(distances)):
        if index > 0:
            if address == distances[index][1]:
                currentLocationId = distances[index][0]
                return int(currentLocationId)


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
    return float(distances.__getitem__(location)[2][destination-1])


def deliverPackageTime(startTime, distanceTraveled):
    strTime = datetime.strptime(startTime, "%I:%M")
    minutesTaken = distanceTraveled / .3
    strTime += timedelta(minutes=minutesTaken)
    return datetime.strftime(strTime, "%I:%M:%S")




# Start nearest neighbor algorithm
# Space complexity:
# Time complexity:
totalDistanceForAllTrucks = 0
truckTotalDistance = 0
previousDistance = 100
def findNearestNeighbor(truck, startTime, currentLocation, previousDistance, truckTotalDistance):
    global totalDistanceForAllTrucks
    isTruck2 = truck == truck2
    if len(truck) > 0:
        packageToRemove = 0
        for package in truck:
            destination = getDestinationId(package.getAddress())
            distanceToDest = distanceToDestination(currentLocation, destination)
            if distanceToDest < previousDistance:
                previousDistance = distanceToDest
                packageToRemove = package
    truckTotalDistance += previousDistance
    timeDelivered = deliverPackageTime(startTime, truckTotalDistance)
    packageToRemove.setStatus("Delivered at: " + str(timeDelivered))
    truck.remove(packageToRemove)
    currentLocation = getCurrentLocationId(packageToRemove.getAddress())

    # From the last package delivery location for Truck2 return to the depot to swap trucks
    if len(truck) == 1 and isTruck2:
        distanceToHub = distanceToDestination(currentLocation, 1)
        totalDistanceForAllTrucks += distanceToHub

    if len(truck) > 0:
        findNearestNeighbor(truck, startTime, currentLocation, 100, truckTotalDistance)
    else:
        totalDistanceForAllTrucks += truckTotalDistance


def searchByTime(time):
    tempArray = packages
    searchTime = datetime.strptime(time, "%H:%M")
    i = 1
    print("\n*************************************************************************************")
    print('{0:20}{1:20}{2}'.format("PACKAGE ID", "DEADLINE", "CURRENT STATUS"))
    print("*************************************************************************************")
    while i < 41:
        substring = packages[i].getStatus()[-8:]
        deliveryTime = datetime.strptime(substring, "%H:%M:%S")
        if deliveryTime < searchTime:
            currentStatus = datetime.strftime(deliveryTime, "%I:%M:%S")
            tempArray[i].setStatus("Delivered at: " + currentStatus)
        else:
            tempArray[i].setStatus("Not Delivered")
        print('{0:20}{1:20}{2}'.format(str(tempArray[i].getId()), str(tempArray[i].getDeadline()), str(tempArray[i].getStatus())))
        i += 1
    print("*************************************************************************************\n")

#Deliver Packages
# Truck 2 will leave  at 8:00 and returns to hub before 10:20 so driver can take truck 1
findNearestNeighbor(truck2, "8:00", 1, previousDistance, truckTotalDistance) # Truck2 = 31.3 miles

# Truck 3 will leave at 9:05 when delayed packages arrive
findNearestNeighbor(truck3, "9:05", 1, previousDistance, truckTotalDistance) # Truck3 = 27.4 miles

# Truck 1 waits for new address for package 9 and leaves at 10:20
findNearestNeighbor(truck1, "10:20", 1, previousDistance, truckTotalDistance) # Truck1 = 44.3 miles

# Begin simulation
print("\n\n*********************************")
print("WGUPS Package Delivery Simulation")
print("*********************************")
print("Choose an option:")
print("1 - Print all packages status")
print("2 - Search for package by package ID")
print("3 - Print packages status at a given time")
print("4 - Print total distance traveled for all trucks")
beginSim = raw_input("Enter your choice:")
if beginSim == "1":
    packages.printAllPackages()
elif beginSim == "2":
    packageID = input("Input id of package you would like to see:")
    packages.printPackage(packageID)
elif beginSim == "3":
    enteredTime = raw_input("Enter the time you'd like to see in 24 hour format (XX:XX): ")
    searchByTime(enteredTime)
elif beginSim == "4":
    print("Total distance traveled by all trucks is " + str(totalDistanceForAllTrucks))
else:
    print("you entered an invalid value")