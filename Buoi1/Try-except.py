def chia(a,b):
    return a/b

def tinh(a,b):
    return a+b+2*b+2*a

print("1")
print("2")

try:
    print(chia(4,2))
except:
    print("Cai nay dang bi loi")
finally:
    print("Du dung hay sai thi van in ra dong nay")

print("3")
print("4")
print(tinh(1,2))
#Viet 1 ham nhap 1 so tu ban phim, tinh can bac hai cua so do
#Dung try - except de xu ly trong truong hop nguoi dung khong nhap ma nhap chu
