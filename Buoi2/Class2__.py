class PTTC1:
    #Thuoc tinh
    def __init__(self,name,age,country,clazz):
        self.name = name
        self.age = age
        self.country = country
        self.clazz = clazz
    #Phuong thuc
    def an(self):
        print("Phan an day du truoc khi toi lop")
    def hoc(self):
        print(self.name+" hoc Python")


student1 = PTTC1("Minh",20,"Hn","PTTC1")
print(student1.name)
student1.an()
student1.hoc()