
class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.status = status

    def getId(self):
        return self.id

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getDeadline(self):
        return self.deadline

    def getZip(self):
        return self.zip

    def getMass(self):
        return self.mass

    def getStatus(self):
        return self.status