# Viet chuong trinh nhap va in ra 1 ma tran
m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))
matrix = []
def Input(m,n):
    for i in range(m):
        row = []
        for j in range(n):
            a = int(input("Nhap phan tu [{}][{}]: ".format(i,j)))
            row.append(a)
        matrix.append(row)
    
Input(m,n)

#print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print("{:<10}".format(matrix[i][j]),end="")
    print()
print()
            


