import customtkinter
from tkinter import *


def get_digit(digit):
    current = screen_variable.get()
    new= current +str(digit)
    result_label.delete(0,END)
    result_label.insert(0,new)
 
def clear():
    result_label.delete(0,END)

def get_operator(op):
   
    current = screen_variable.get()
    new= current +str(op)
    result_label.delete(0,END)
    result_label.insert(0,new)

def get_result():
   
    try:
        x=eval(result_label.get())
        result_label.delete(0,END)
        result_label.insert(0,x)
    except:
        result_label.insert(0,'syntax error')

   
app=customtkinter.CTk()
app.title("Calculator by SHIVAM VERMA")
app.geometry("415x430+400+150")
app.config(bg="orange")
app.resizable(0,0)

screen_variable=StringVar()
result_label = Entry(app,text='',textvariable=screen_variable,bg='black',fg='white',border=25,relief=SUNKEN,font=('verdana',25),width=21,justify=RIGHT)
result_label.grid(row=0,column=0,columnspan=5,pady=(5,5),sticky='e',padx=10)

btn7= Button(app,text='7',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_digit(7) )
btn7.grid(row=1,column=0)

btn8= Button(app,text='8',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_digit(8))
btn8.grid(row=1,column=1)

btn9= Button(app,text='9',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_digit(9))
btn9.grid(row=1,column=2)

btn_add= Button(app,text='+',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_operator ('+') )
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14))


btn4= Button(app,text='4',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn5= Button(app,text='5',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_digit(5))
btn5.grid(row=2,column=1)

btn6= Button(app,text='6',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_digit(6))
btn6.grid(row=2,column=2)

btn_mul= Button(app,text='*',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_operator('*'))
btn_mul.grid(row=3,column=3)

btn1= Button(app,text='1',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_digit(1))
btn1.grid(row=3,column=0)

btn2= Button(app,text='2',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_digit(2))
btn2.grid(row=3,column=1)

btn3= Button(app,text='3',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_digit(3))
btn3.grid(row=3,column=2)

btn_sub= Button(app,text='-',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_operator('-'))
btn_sub.grid(row=2,column=3)

btn_div= Button(app,text='/',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_operator('/'))
btn_div.grid(row=4,column=3)

btn_zero= Button(app,text='0',font=('verdana',14),bg='black',fg='pink',width=10,height=4,command =lambda :get_digit(0))
btn_zero.grid(row=4,column=1)

btn_clear= Button(app,text='C',font=('verdana',14),bg='Red',fg='pink',width=10,height=4,command =lambda :clear())
btn_clear.grid(row=4,column=0)

btn_equal= Button(app,text='=',font=('verdana',14),bg='green',fg='pink',width=10,height=4,command= lambda :get_result())
btn_equal.grid(row=4,column=2)


app.mainloop()