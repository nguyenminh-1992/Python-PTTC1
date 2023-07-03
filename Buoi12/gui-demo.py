#Thu vien thiet ke giao dien
import tkinter

#pip3 install tk

#Khung giao dien
giaodien = tkinter.Tk()
giaodien.title('Chuong trinh')
giaodien.geometry('500x200')

label3 = tkinter.Label(giaodien,text="Tinh tong 2 so",fg='black',bg='white')
label3.grid(column=3,row=0)

label1 = tkinter.Label(giaodien,text="So thu nhat",fg='black',bg='white')
label1.grid(column=2,row=1)
textbox1 = tkinter.Entry(giaodien,width=30)
textbox1.grid(column=3,row=1)


label2 = tkinter.Label(giaodien,text="So thu hai",fg='black',bg='white')
label2.grid(column=2,row=2)
textbox2 = tkinter.Entry(giaodien,width=30)
textbox2.grid(column=3,row=2)

button = tkinter.Button(giaodien,text="Click vao",bg='blue',fg='black')
button.grid(column=3,row=3)

textbox3 = tkinter.Entry(giaodien,width=10)
textbox3.grid(column=3,row=4)





giaodien.mainloop()