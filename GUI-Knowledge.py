from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดโปรแกรม

B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20 , ipady=20)

L1=Label(GUI,text='โปรแกรมบันทึกคว่ามรู้' , font=('Angsana New',18),fg='green')
L1.place(x=30,y=20)
def Button2():
    text='ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี' ,text)
    #showwarning
    #showerror

FB1 = LabelFrame(GUI,text='Money')
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20,padx=30 ,pady=30)


GUI.mainloop()


