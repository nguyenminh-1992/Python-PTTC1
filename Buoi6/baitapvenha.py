# A  4  5  7  9  1
# 0  2  4  8  1  0
# 1  4  9  1  4  3
# 2  4  5  6  7  9 
# 1  3  5  7  8  B

#Di tu A -> B: Tong cac trong so la nho nhat
#Duoc di len, di ngang, di cheo

#A:0
#B:0
#Output
#[0][0], [1][0], [2][0]

a =[[0,4,5,7,9,1],[0,2,4,8,1,0],[1,4,9,1,4,3],[2,4,5,6,7,9],[1,3,5,7,8,0]]

tongquangduong = 0
quangduong = []

i=0
j=0
list=[a[i-1][j-1],a[i-1][j],a[i-1][j+1],a[i][j-1],a[i][j+1],a[i+1][j-1],a[i+1][j],a[i+1][j+1]]
#       a[i-1;j-1],a[i-1,j],a[]
for k in list:
    min = a[i-1][j-1]
    if min > k:
        min = k
tongquangduong += min
quangduong.append(k)

