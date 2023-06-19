

#Tao menu chay cac chuc nang

#Chuc nang diem trung binh => hoc luc
import Quanlyhocvien
while True:
    print("-------------------------------")
    print("---Hien thi bang nhan phim 1---")
    print("---  sua bang nhan phim 2   ---")
    print("---  xoa bang nhan phim 3   ---")
    print("---  them bang nhan phim 4  ---")
    print("--- thoat bang nhan phim 0  ---")
    n = int(input("nhap so: "))
    if n == 1:
        print("hien thi")
        Quanlyhocvien.getalldata3()
        Quanlyhocvien.ketnoi.close()
    elif n == 2:
        print("sua")
        Quanlyhocvien.updatedata()
        Quanlyhocvien.ketnoi.close()
    elif n == 3:
        print("xoa")
        Quanlyhocvien.deletedata()
        Quanlyhocvien.ketnoi.close()
    elif n == 4:
        print("them")
        Quanlyhocvien.createdata()
        Quanlyhocvien.ketnoi.close()
    elif n == 0:
        print("thoat")
        break
    else:
        print("Vui long nhap lai. ")