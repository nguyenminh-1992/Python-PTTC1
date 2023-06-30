L = ["Geeks\n", "for\n", "Geeks\n"]
 
# writing to file
file1 = open('Buoi11/test2.txt', 'w')
file1.writelines(L)
file1.close()
 
# Using readlines()
file1 = open('Buoi11/test2.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))