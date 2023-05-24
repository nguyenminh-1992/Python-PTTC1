#Class
#O-O-P
# Cac phan tu trong Class se duoc goi la cac doi tuong
class PTTC1():
    #Thuoc tinh
    name = 'abc'
    age = 0
    country = 'HN'
    #Phuong thuc
    def hoc(self):
        print("Phai hoc Python")
    def thi(self):
        print("Phai thi Python")
    def an(self):
        print("An ngay 3 bua")


student1 = PTTC1()
student1.name = "Nguyen Van A"
student1.age = 20
student1.country = "Ha Noi"

student2 = PTTC1()
student2.name = "Nguyen Van B"
student2.age = 21
student2.country = "Sai Gon"

student3 = PTTC1()
student3.name = "Nguyen Van C"
student3.age = 22
student3.country = "Da Nang"

print(student1.name)
print(student2.name)
print(student3.name)

student1.hoc()
