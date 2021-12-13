
class superHero:

    def __init__(self, name, power, secretname, city, location):
        self.name = name
        self.power = power
        self.secretName = secretname
        self.city = city
        self.location = location

    def maxPower(self, max):
        self.power += max
        return self.power

    def minPower(self, min):
        if min >= 0:
            if self.power < min:
                self.power = 0
            else:
                self.power -= min
        else:
            self.power = 0
        return self.power


    def __str__(self) -> str:
        return "name: " + str(self.name) + \
               ", power: " + str(self.power) + \
               ", secretName: " + str(self.secretName) + \
               ", city: " + str(self.city) + \
               ", location: " + str(self.location)