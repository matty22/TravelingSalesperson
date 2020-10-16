
class Package:
    def __init__(self, id, address, deadline, city, zip, mass, status):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip = zip
        self.mass = mass
        self.status = status

    def getId(self):
        return self.id

    def getAddress(self):
        return self.address

    def getDeadline(self):
        return self.deadline

    def getCity(self):
        return self.city

    def getZip(self):
        return self.zip

    def getMass(self):
        return self.mass

    def getStatus(self):
        return self.status