import tkinter
import tkinter.font
window = tkinter.Tk()
window.title('음식계산기')
window.geometry('600x400+100+100')
title_font = tkinter.font.Font(family= '맑은 고딕', size=20)
title = tkinter.Label(window, text='음식 계산기', font=title_font)
title.grid(row=0, column=0)
def func1():
    price = 0
    trip = 0
    if cv1.get() == 1:
        price += 40
    if cv2.get() == 1:
        price += 50
    if cv3.get() == 1:
        price += 60
    if cv4.get() == 1:
        price += 70
    if 0 < price < 230:
        trip = 30
    if tip == 0:
        cal.config(text=f'가격 : {price}원')
        cal1.config(text='')
    else:
        cal.config(text=f'가격: {price + tip}')

image1 = tkinter.PhotoImage(file='마라탕후루.png')
image2 = tkinter.PhotoImage(file='국밥1.png')
image3 = tkinter.PhotoImage(file='뿌링뿌링뿌링클.png')
image4 = tkinter.PhotoImage(file='그럼 제가 선배맘에 탕탕후루후루.png')

label1 = tkinter.Label(window, image=image1)
label2 = tkinter.Label(window, image=image2)
label3 = tkinter.Label(window, image=image3)
label4 = tkinter.Label(window, image=image4)

cv1 = tkinter.IntVar()
ckd1 = tkinter.Checkbutton(window, text='40원',variable=cv1,command=func1)
cv2 = tkinter.IntVar()
ckd2 = tkinter.Checkbutton(window, text='50원',variable=cv1,command=func1)
cv3 = tkinter.IntVar()
ckd3 = tkinter.Checkbutton(window, text='60원',variable=cv1,command=func1)
cv4 = tkinter.IntVar()
ckd4 = tkinter.Checkbutton(window, text='70원',variable=cv1,command=func1)
label1.grid(row=1, column=0)
label2.grid(row=1, column=1)
label3.grid(row=1, column=2)
label4.grid(row=1, column=3)
title_font = tkinter.font.Font(family='맑은 고딕')
window.mainloop()

#버튼에 사진 넣는 코드
#image1 = tk.PhotoImage(file='')
#button = tk.Button(image=image1, command = func, bd=0)
#button.pack()