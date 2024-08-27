#multiple inheritance

# In multiple inheritance child class have one or more parent class

class father:
    def car(self):
        print("father have a BMW")


class mother:
    def scooty(self):
        print("mother have a pep")

class son(father,mother):
    def bike(self):
        print("son have a KTM")

ram=son()
ram.car()
ram.scooty()
ram.bike()

