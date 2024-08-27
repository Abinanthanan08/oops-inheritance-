#hierarchical inheritance

# In hierarchical inheritance one parent class have more than one child class


class father:
    def car(self):
        print("father have a car")


class son(father):
    def bike(self):
        print("son have a bike")


class daughter(father):
    def scooty(self):
        print("daughter have a scooty")


a = son()
a.car()
a.bike()

b = daughter()
b.car()
b.scooty()