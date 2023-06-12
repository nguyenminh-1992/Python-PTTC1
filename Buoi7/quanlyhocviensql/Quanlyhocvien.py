import Connectsql

# Ket noi voi MySql
ketnoi = Connectsql.getConnection()
#print(ketnoi)
dulieu = ketnoi.cursor()

#Lay du lieu tu MySql ve Visual Code
def getalldata():
   #Yeu cau MySql thuc hien cau lenh trong nhay doi
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
   #Tra du lieu ve Visual Code
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)

def getalldata2():
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
    ketqua = dulieu.fetchone()
    while ketqua is not None:
        print(ketqua)
        ketqua = dulieu.fetchone()

#Loc du lieu theo id
def getdatabyid():
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = 3")
   #Tra du lieu ve Visual Code
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)

#SELECT * FROM Quan_ly_hoc_vien.Hocvien

getdatabyid()
#Dong ket noi
ketnoi.close()