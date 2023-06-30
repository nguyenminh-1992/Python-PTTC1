#r w 
#Cac quyen cho file
#r : Read
#r+: Read + Write
#w : Write
#w+ : Write + Read


#read_file = open('Buoi11/test.txt','r')
#print(read_file)




#read_file.close()
with open('Buoi11/test.txt','r') as read_file:
    #content = read_file.read()  #fetch all
    content = read_file.readlines()
    line = int(1)
    while line in content:
        print("content{}: {}".format(line, line.strip()))
        line = line + 1
        line = read_file.readlines()
       
    
#content = content + "Xin chao den voi PTTC1"
#print(content)   