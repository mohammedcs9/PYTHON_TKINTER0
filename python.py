#from tkinter import *
#pro = Tk()
#pro.geometry('300x300+900+100')
#pro.resizable(True, True)
#pro.title('Learn python tkinter')
#pro.config(background='yellow')
#pro.iconbitmap('')
#pro.minsize(200,200)
#pro.maxsize(400,400)
#pro.mainloop()
print("*" * 80)
#pro1 = Tk()
#pro2 = Tk()
#pro1.title('Title1')
#pro2.title('Title2')
#pro1.geometry('300x300+10+10')
#pro2.geometry('300x300+320+10')
#pro1.config(background='red')
#pro2.config(background='blue')
#pro1.mainloop()
print("*" * 80)
#pro3 = Tk()
#pro4 = Tk()
#pro3.title('1')
#pro3.lift()
#pro4.iconify()
#pro4.lower()
#pro4.state('withdrawn')#pro4.state('iconic')#pro4.state('normal')
#pro3.mainloop()
print("*" * 80)
#pro5 = Tk()
#pro5.geometry('800x500')

#fr1 = Frame(width='390',height='499',bg='red')
#fr1.place(x=1,y=1)

#fr2 = Frame(width='390',height='499',bg='blue')
#fr2.place(x=393,y=1)


#bt1 = Button(fr1,text='button1',fg='black',bg='white',cursor='arrow',width='30')
#bt1.place(x=10,y=10)

#bt2 = Button(fr2,text='button2',fg='red',bg='black',cursor='heart',width='30')
#bt2.place(x=10,y=10)

#lbl1 = Label(fr1, text='HELLO', fg='white', bg='red',font=10)
#lbl1.place(x=10,y=40)

#lbl2 = Label(fr2, text='PYTHON', fg='black', bg='blue',font=15)
#lbl2.place(x=10,y=40)

#en1 = Entry(fr1)
#en1.place(x=10,y=100)

#en2 = Entry(fr1, justify='center')
#en2.place(x=10,y=140)

#en3 = Entry(fr1, justify='center',fg='red',bg='black')
#en3.place(x=10,y=180)

#en4 = Entry(fr1, justify='center',fg='red',bg='black',font='10')
#en4.place(x=10,y=220)

#en5 = Entry(fr2)
#en5.place(x=10,y=100)

#pro5.mainloop()
print("*" * 80)
#from tkinter import *
#from tkinter import ttk

#pro = Tk()
#pro.geometry('600x400')

#cmbo1 = ttk.Combobox(pro,
#value=('male','female'),state='readonly'
#)
#cmbo1.place(x=1,y=1)

#cmbo2 = ttk.Combobox(pro, value=('jordan','iraq','syria','marroc'),state='readonly'
#)
#cmbo2.place(x=1,y=40)


#pro.mainloop()
print("*" * 80)
#from tkinter import *
#from tkinter import ttk

#pro = Tk()
#pro.geometry('600x400')

#lst1 = Listbox(pro,width='10',height='20')
#lst1.insert(0,"one")
#lst1.insert(1,"two")
#lst1.insert(2,"three")
#lst1.insert(3,"four")
#lst1.pack()


#pro.mainloop()
print("*" * 80)
from tkinter import *
from tkinter import ttk

pro = Tk()
pro.geometry('600x400')

r1 = ttk.Radiobutton(pro,value=1)
r1.pack()



pro.mainloop()
