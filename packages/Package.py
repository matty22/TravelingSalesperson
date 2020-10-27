
import re


# Define Package object
# --------------------------
class Package:
    # Space complexity: O(1)
    # Time complexity: O(1)
    def __init__(self, id, address, city, state, zip, deadline, mass, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.status = status

    # Fetch package id
    # Space complexity: O(1)
    # Time complexity: O(1)
    def getId(self):
        return int(self.id)

    # Fetch package address
    # Space complexity: O(1)
    # Time complexity: O(1)
    def getAddress(self):
        return self.address

    # Fetch package address number
    # Space complexity: O(1)
    # Time complexity: O(1)
    def getAddressNumber(self):
        regex = re.compile('(^[^\s]+)')
        addressNumber = regex.match(self.address).group()
        return addressNumber

    # Fetch package city
    # Space complexity: O(1)
    # Time complexity: O(1)
    def getCity(self):
        return self.city

    # Fetch package state
    # Space complexity: O(1)
    # Time complexity: O(1)
    def getState(self):
        return self.state

    # Fetch package deadline
    # Space complexity: O(1)
    # Time complexity: O(1)
    def getDeadline(self):
        return self.deadline

    # Fetch package zip
    # Space complexity: O(1)
    # Time complexity: O(1)
    def getZip(self):
        return self.zip

    # Fetch package mass
    # Space complexity: O(1)
    # Time complexity: O(1)
    def getMass(self):
        return self.mass

    # Fetch package status
    # Space complexity: O(1)
    # Time complexity: O(1)
    def getStatus(self):
        return self.status

    # Set package status
    # Space complexity: O(1)
    # Time complexity: O(1)
    def setStatus(self, status):
        self.status = status