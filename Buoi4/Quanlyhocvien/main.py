#Them
#Xoa
#Sua
#Hien thi

while(True):
    print("|--------------------------------------|")
    print("|----Chuong trinh quan ly hoc vien     |")
    print("|1. Chuc nang them                     |")
    print("|2. Chuc nang xoa                      |")
    print("|3. Chuc nang sua                      |")
    print("|4. Chuc nang hien thi                 |")
    print("|0. Thoat                              |")
    print("|--------------------------------------|")

    nhap = int(input("Nhap chuc nang theo so: "))
    if nhap==1:
        print("Them")
    elif nhap==2:
        print("Xoa")
    elif nhap==3:
        print("Sua")
    elif nhap==4:
        print("Hien thi")
    elif nhap == 0:
        print("Tam biet")
        break
    else: 
        print("Nhap sai vui long nhap lais")
        
