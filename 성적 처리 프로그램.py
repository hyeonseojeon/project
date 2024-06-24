from tkinter import *
def proc1():
    total.set(int(kor.get())+int(eng.get())+int(math.get()))
    average.set(int(total.get())/3)
def proc2():
    name.set('')
    kor.set('')
    eng.set('')
    math.set('')
    total.set('')
    average.set('')

w=Tk()
w.title('성적처리')
w.resizable( width=0, height=1)
w.geometry('640x400+100+100')
la1=Label(w,text='이름 ',font=('',20)).grid(row=1,column=1)
name=StringVar()
et1=Entry(w,textvariable=name,font=('',20),width=10).grid(row=1,column=2)

la2=Label(w,text='국어 ',font=('',20)).grid(row=2,column=1)
kor=StringVar()
et2=Entry(w,textvariable=kor,font=('',20),width=10).grid(row=2,column=2)

la3=Label(w,text='영어 ',font=('',20)).grid(row=3,column=1)
eng=StringVar()
et3=Entry(w,textvariable=eng,font=('',20),width=10).grid(row=3,column=2)

la4=Label(w,text='수학 ',font=('',20)).grid(row=4,column=1)
math=StringVar()
et4=Entry(w,textvariable=math,font=('',20),width=10).grid(row=4,column=2)

la5=Label(w,text='총점 ',font=('',20)).grid(row=5,column=1)
total=StringVar()
et5=(Entry(w,textvariable=total,font=('',20),width=10,state='readonly').grid(row=5,column=2))

la6=Label(w,text='평균 ',font=('',20)).grid(row=6,column=1)
average=StringVar()
et6=(Entry(w,textvariable=average,font=('',20),width=10,state='readonly').grid(row=6,column=2))
button1=Button(w,text='계산',font=('',20),command=proc1).grid(row=7,column=1)
button2=Button(w,text='지우기',font=('',20),command=proc2).grid(row=7,column=2)
w.mainloop()