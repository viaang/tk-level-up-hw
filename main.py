from tkinter import *
window = Tk()

window.geometry('600x800')
window.title('Age and name')

frame1 = Frame(height='600', width='400', bg = '#008000' )
frame1.pack()

Lable1 = Label(master=frame1,text = 'name',  height = '1', width='5')
Lable1.place(x = 120, y = 300)

Entry1 = Entry(master=frame1, height = '1', width = '5')
Entry1.place(x = 180, y = 300)


Lable2 = Label(master=frame1,text = 'year', height = '1', width='5')
Lable2.place(x = 120, y = 270)
Entry2 = Entry(master=frame1, height = '1', width = '5')
Entry2.place(x = 180, y = 270)


Lable3 = Label(master=frame1, text = 'month', height = 1, width='5')
Lable3.place(x = 120, y = 240)

Entry3 = Entry(master=frame1, height = '1', width = '5')
Entry3.place(x = 180, y = 240)

Lable4 = Label(master = frame1, text = 'day', height = '1', width = '5')
Lable4.place(x = 180, y = 210 )

Entry4 = Entry(master=frame1, height = '1', width = '5')
Entry4.place(x = 180, y = 210)


def display ():
    Tex = Text("hello" +  Entry1 +  "you birthday is" + Entry2 + Entry3 + Entry4)
    Tex.pack
Butto = Button(text = 'click me', height='2', width='4', command=display)
Butto.pack()
window.mainloop()