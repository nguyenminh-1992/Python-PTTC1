#C R U D
#Create
#Read
#Update
#Delete

from PTTC1Dinhnghia import PTTC1

class Quanlyhocvien:
    list_hocvien = []

    def themhocvien(self):
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
            self.list_hocvien.append(hocvien)

    def hienthihocvien(self):
        print ("{:<15} {:<15} {:<15} {:<10}{:<15}{:<20}".format("Ten","Tuoi","Que Quan","Lop","Tieng Anh","Tin Hoc"))
        for i in self.list_hocvien:
            print("{:<15} {:<15} {:<15} {:<10}{:<15}{:<20}".format(i.ten,i.tuoi,i.quequan,i.lop,i.tienganh,i.tinhoc))

test = Quanlyhocvien()
test.themhocvien()
test.hienthihocvien()