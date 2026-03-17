# METHOD OVER-RIDING

class GrandFather():
    def G1(self):
        print("GrandFather")

class Father():
    def F1(self):
        print("Father")

class Child(Father,GrandFather):
    def C1(self):
        print("child")

c=Child()
c.C1()
c.F1()
c.G1()
print(Child.__mro__)# method resolution order
print(Child.mro())
