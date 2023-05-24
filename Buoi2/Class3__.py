class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def an(self):
        print("Phai an")
    def ngu(self):
        print("Phai ngu")
    def hoc(self):
        print("Di hoc 2")

class BKCAD():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hoc(self):
        print("Di hoc 1")
    def thi(self):
        print("Phai thi")

#Tinh ke thua
class PTTC1(BKCAD,Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def giaoluu(self):
        print("Giao luu PTTC1")

class PTTC2(BKCAD,Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def giaoluu(self):
        print("Giao luu PTTC2")



class PTTC1_offline(PTTC1):
    def __init__(self,name,age):
        self.name = name
        self.age = age

student1 = PTTC1("Quang", 22)
student1.hoc()
student1.an()

student3 = PTTC1("Tien", 32)

#Tinh da hinh
def da_hinh(student):
    student.giaoluu()

da_hinh(student1)
da_hinh(student3)

student2 = PTTC1_offline("Hoang", 23)
student2.giaoluu()
student2.hoc()
