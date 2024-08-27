# single inheritance

# In single inheritance child class have only one parent class

class father:
    def car(self):
        print("father have a car")


class son(father):
    def bike(self):
        print("son have a bike")

a=son()
a.car()
a.bike()