#matran 1
# 12 7  3
# 4  5  6
# 7  8  9


#matran 2
# 5  8  1
# 6  7  3
# 4  5  9

#Viet chuong trinh tinh tong matran1 + matran2
matran1=[[12,7,3],[4,5,6],[7,8,9]]
matran2=[[5,8,1],[6,7,3],[4,5,9]]
matrantong=[]
for i in range(len(matran1)):
    a=[]
    for j in range(len(matran1[i])):
        m=matran1[i][j]+matran2[i][j]
        a.append(m)
    matrantong.append(a)
print(matrantong)

#matran 3
# 12 7
# 4  5
# 3  8

#Viet chuong trinh tinh ma tran chuyen vi
#output
# 12 4  3
# 7  5  8

matran3=[[12,7],[4,5],[3,8]]
matran4=[]

for i in range(len(matran3[0])):
    b=[]
    for j in range(len(matran3)):
        if i==j:
            c=matran3[i][j]
            b.append(c)
        else:
            c=matran3[j][i]
            b.append(c)
    matran4.append(b)
print(matran4)