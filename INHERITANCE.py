# SINGLE INHERITANCE
'''
class parent():
    def p(self):
        print("parent")



class child(parent):
    def c(self):
        print("child")


p=parent()
p.p()


c=child()
c.c()

c.p()
'''

# MULTILEVEL INHERITANCE
'''
print()
class father():
    def p1(self):
        print("father")

class mother(father):
    def m1(self):
        print("mother")

class child(mother):
    def c1(self):
        print("child")

m=mother()
m.m1()
m.p1()

print()
c=child()
c.c1()
c.m1()
c.p1()
'''

# MULTIPLE INHERITANCE
'''
print()
class parent1():
    def p1(self):
        print("parent1")

class parent2():
    def p2(self):
        print("parent2")

class child(parent1,parent2):
    def c1(self):
        print("child")


p=parent1()
p.p1()
p=parent2()
p.p2()

c=child()
c.c1()

c.p1()
c.p2()
'''
# HEIRACHIAL INHERITANCE
'''
print()
class Father():
    def F1(self):
        print("father")

class Child1(Father):
    def C1(self):
        print("child 1")

class Child2(Father):
    def C2(self):
        print("child 2")

c2=Child2()
c2.C2()
c2.F1()

print()
c1=Child1()
c1.C1()
c1.F1()
'''

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







































