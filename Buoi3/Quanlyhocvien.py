class PTTC1():
    def __init__(self,ten,tuoi,quequan,lop,tienganh,tinhoc):
        self.ten = ten
        self.tuoi = tuoi
        self.quequan = quequan
        self.lop = lop
        self.tienganh = tienganh
        self.tinhoc = tinhoc

n = int(input("Nhap so luong hoc vien: "))
list_hocvien = []
for i in range(1,n+1):
    print("Nhap hoc vien thu {}".format(i))
    ten = input("Nhap ten:  ")
    tuoi = int(input("Nhap tuoi: "))
    quequan = input("Nhap que quan: ")
    lop = input("Nhap lop: ")
    tienganh = float(input("Nhap diem tieng anh: "))
    tinhoc = float(input("Nhap diem tin hoc:  "))
    hocvien = PTTC1(ten,tuoi,quequan,lop,tienganh,tinhoc)
    list_hocvien.append(hocvien)

print ("{:<15} {:<15} {:<15} {:<10}{:<15}{:<20}".format("Ten","Tuoi","Que Quan","Lop","Tieng Anh","Tin Hoc"))
for i in list_hocvien:
    print("{:<15} {:<15} {:<15} {:<10}{:<15}{:<20}".format(i.ten,i.tuoi,i.quequan,i.lop,i.tienganh,i.tinhoc))