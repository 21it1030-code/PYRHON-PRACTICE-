# creating a phone account
class con:
    def __init__(self):
        self.contacts={}

    def add(self,name,ph):
        if name not in self.contacts:
            self.contacts[name]=ph
            print("added")
        else:
            print("exist")

    def display(self):
        print("contact:",self.contacts)

    def update(self


p1=con()
p1.add("john",123456789)
p1.add("john",12345678)
p1.display()
print()
p2=con()
p2.add("akcdsg",1234567890)
p2.display()
