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
        for i in range(1,n+1):
            print("Nhap hoc vien thu {}".format(i))
            ten = input("Nhap ten:  ")
            tuoi = int(input("Nhap tuoi: "))
            quequan = input("Nhap que quan: ")
            lop = input("Nhap lop: ")
            tienganh = float(input("Nhap diem tieng anh: "))
            tinhoc = float(input("Nhap diem tin hoc:  "))
            diemtrungbinh = float((tienganh + tinhoc)/2)
            hocvien = PTTC1(ten,tuoi,quequan,lop,tienganh,tinhoc)
            if (diemtrungbinh > 5):
                hocvien.xeploai = "Gioi"
            else:
                hocvien.xeploai = "Yeu"
            hocvien.id = i
            
            self.list_hocvien.append(hocvien)
#Yeu cau
#1. Tao Id tu dong
#2. Tinh diem trung binh tieng anh + tin hoc
# Xep loai: Trung binh > 5: Gioi, <5: Yeu
#Hienthihocvien show cot ID, cot Xep loai

#Suathongtinhocvien(self) - Sua ten,tuoi

#Xoathongtinhocvien(self) - Xoa ID

    def hienthihocvien(self):
        print ("{:<15}{:<15} {:<15} {:<15} {:<10}{:<15}{:<20}{:<20}".format("ID","Ten","Tuoi","Que Quan","Lop","Tieng Anh","Tin Hoc","Xep loai"))
        for i in self.list_hocvien:
            print("{:<15}{:<15} {:<15} {:<15} {:<10}{:<15}{:<20}{:<20}".format(i.id,i.ten,i.tuoi,i.quequan,i.lop,i.tienganh,i.tinhoc,i.xeploai))

#Problem
    def in__(self):
        print(self.list_hocvien[0])

test = Quanlyhocvien()
test.themhocvien()
test.hienthihocvien()
test.in__()