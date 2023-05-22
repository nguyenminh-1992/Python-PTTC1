#Viet 1 ham nhap 1 so tu ban phim, tinh can bac hai cua so do
#Dung try - except de xu ly trong truong hop nguoi dung khong nhap ma nhap chu
import math
def tinhcanbac_2(x):
    try:
        print("Gia tri can bac 2:",math.sqrt(x))
    except:
        print("Dữ liệu nhâp sai !!!!!!!!!!!!")

tinhcanbac_2(5)