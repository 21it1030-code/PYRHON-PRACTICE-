# INHERITANCE USING SUPER
class Codegnan:
    def __init__(self,name,address,phone_no):
        self.name=name
        self.address=address
        self.phone_no=phone_no
        
    def details(self):
        print(self.name,self.address,self.phone_no)
        
        
class Trainer(Codegnan):
    def __init__(self,name,address,phone_no,subject,classes):
        super().__init__(name,address,phone_no)
        self.subject=subject
        self.classes=classes
        
    def details(self):
        super().details()
        print(self.subject,self.classes)
        


t1=Trainer("Jeswanth","Vja",7842807077,"python",3)
t1.details()
