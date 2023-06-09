
#Truc toa Oxy

#Nhap toa do cac diem trong truc toa do Oxy

#Nhap r (ban kinh hinh tron tam 0 (0,0)

#Viet chuong trinh dem so diem nam trong duong tron tam 0,
#ban kinh r
import math
class Diem:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def so_diem_trong_ban_kinh(self,ban_kinh):
        khoang_cach = math.sqrt(self.x**2 + self.y**2)
        if khoang_cach <= ban_kinh:
            return True
        else:
            return False
n = int(input("bao nhieu diem muon nhap: "))
list_diem = []
for i in range(1,n+1):
    x = float(input("nhap diem x: "))
    y = float(input("nhap diem y: "))
    toa_do = Diem(x,y)
    list_diem.append(toa_do)

ban_kinh = float(input("nhap ban kinh: "))

so_diem = 0
for diem in list_diem:
    if diem.so_diem_trong_ban_kinh(ban_kinh):
        so_diem += 1

print("so diem trong ban kinh la: ", so_diem)