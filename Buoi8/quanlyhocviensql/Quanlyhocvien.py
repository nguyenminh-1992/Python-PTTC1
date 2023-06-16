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
#Lay ra danh sach hoc vien co ID = 3
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = 2")
   #Tra du lieu ve Visual Code
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)

def getdatabyid2(id):
    sql = "SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = {}".format(id)
    dulieu.execute(sql)
   #Tra du lieu ve Visual Code
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)

def getdatabyidandage(id,age):
    sql = "SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = {} AND Age = {}".format(id,age)
    dulieu.execute(sql)
   #Tra du lieu ve Visual Code
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)

def createdata():
    sql = "INSERT INTO `Hocvien`(Id,`Name`,Age,Country,English,Information) VALUES (5,'Nguyen Van E',24,'Da Nang',7,9)"
    dulieu.execute(sql)
    ketnoi.commit()
    print("Da them du lieu thanh cong")



#SELECT * FROM Quan_ly_hoc_vien.Hocvien
createdata()
#SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = 1
#Dong ket noi
ketnoi.close()