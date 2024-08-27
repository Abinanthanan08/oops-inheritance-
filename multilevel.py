#multileve inheritance

# In multileve inheritance parent class depends on another parent class like family tree

class grandfather:
    def bullet(self):
        print("grandfather have a bullet")

class father(grandfather):
    def car(self):
        print("father have a car")


class son(father):
    def bike(self):
        print("son have a bike")


class grandson(son):
    def cycle(self):
        print("grandson have a cycle")

a=grandson()
a.bullet()
a.car()
a.bike()
a.cycle()