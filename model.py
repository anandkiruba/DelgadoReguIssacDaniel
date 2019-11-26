from datetime import date, datetime
import json


class Breed:
    def __init__(self, id1: int, name: str, temperament: str, coat: str):
        self.id1 = id1
        self.name = name
        self.temperament = temperament
        self.coat = coat

    def __initnoid__(self, name: str, temperament: str, coat: str):
        self.name = name
        self.temperament = temperament
        self.coat = coat

    def __str__(self):
        test = (str(self.id1) + self.name + self.temperament + self.coat)
        return test


class Pupper:
    def __init__(self, id1: int, name: str, sex: str, weight: str, height: str, color: str, birthdate: str,
                 breed: Breed):
        self.id1 = id1
        self.name = name
        self.sex = sex
        self.weight = weight
        self.height = height
        self.color = color
        self.birthdate = date(int(birthdate[0:4]), int(birthdate[4:6]), int(birthdate[6:8]))
        self.breed = breed

    def __initnoid__(self, name: str, sex: str, weight: str, height: str, color: str, birthdate: str, breed: Breed):
        self.name = name
        self.sex = sex
        self.weight = weight
        self.height = height
        self.color = color
        self.birthdate = date(int(birthdate[0:4]), int(birthdate[4:6]), int(birthdate[6:8]))
        self.breed = breed

    def __str__(self):
        test = (str(self.id1) + self.name + self.sex + self.weight + self.height + self.color + str(
            self.birthdate) + str(self.breed))
        return test


if __name__ == "__main__":
    testbreed = Breed(1, "Labrador", "Gun Dog", "Ash")
    testpupper = Pupper(1, "Azlan", "M", "90 lbs", "3 feet", "Ash", "20140507", testbreed)
    print(testbreed)
    print(testpupper)
