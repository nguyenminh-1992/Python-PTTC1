#Tao 1 Class, dinh nghia Class
#Tao 10 doi tuong trong Class
#In ra danh sach ten 10 doi tuong trong Class

class Lop_hoc:
    def __init__(self,name):
        self.name = name
    def hienthi(self):
        print(self.name)

list_lop_hoc = []

dt1 = Lop_hoc("A")
list_lop_hoc.append(dt1)
dt2 = Lop_hoc("B")
list_lop_hoc.append(dt2)
dt3 = Lop_hoc("C")
list_lop_hoc.append(dt3)
dt4 = Lop_hoc("D")
dt5 = Lop_hoc("E")
dt6 = Lop_hoc("F")
dt7 = Lop_hoc("G")
dt8 = Lop_hoc("H")
dt9 = Lop_hoc("I")
dt10 = Lop_hoc("J")

for i in list_lop_hoc:
    print(i.name)