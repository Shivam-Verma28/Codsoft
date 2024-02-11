#=================================================importing required packages=============================================
from tkinter import*
import customtkinter as c
from PIL import Image
import random
import time

#=================================================defining root(window) layout============================================
c.set_appearance_mode("light")
root=c.CTk()
root.geometry("400x400+500+150")
root.resizable(False,False)
root.iconbitmap("2icon.ico")
root.title("Password Generator:By Shivam Verma")

#======================================defining variable name and its data type===========================================
numvar=IntVar()
special_charsvar=IntVar()
entvar=StringVar()

#===================================defining function for giving placeholder in entry widget==============================
def focusin(event):
    if input_entry.get() == "Enter desired length":
        input_entry.delete(0, END)
        input_entry.configure(fg_color='snow',font=("Helvetica",20 ,"bold"),text_color="#FF6C22")

def focusout(event):
    if input_entry.get() == "":
        input_entry.insert(0, "Enter desired length")
        input_entry.configure(font=("Helvetica",20 ,"bold"),text_color="grey")


#============================================defining function for generate button========================================
def gen(event):
    global entvar
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number='1234567890'
    special_charsial_char='!@#$%^&*()._'
    length=int(entvar.get())
    try:
        if int(numvar.get())==1:
            if int(special_charsvar.get())==1:
                string=lower+upper+number+special_charsial_char
            else:
                string=lower+upper+number
        elif int(special_charsvar.get())==1:
            string=lower+upper+special_charsial_char
        else:
            string=lower+upper
        password="".join(random.sample(string,length))
        input_entry.delete(0,END)
        output_entry.delete(0,END)
        output_entry.insert(0,password)
    except:
        input_entry.insert(0,"Invalid Input")
        time.sleep(2)
        input_entry.delete(0,END)
    special_charsvar.set(0)
    numvar.set(0)

#===============================================defining function for copy button=========================================
def copy(event):
    password = output_entry.get()
    root.clipboard_clear()  
    root.clipboard_append(password)  
    root.update()  
    output_entry.delete(0,END)

#==================================inserting a .png image at the left side in root window=================================
logo=c.CTkImage(dark_image=Image.open("pass2.png"),size=(400,100))
top_img=c.CTkLabel(root,image=logo,text="")
top_img.grid(row=0,column=0,columnspan=5)

#===========================================Entry widget for input and output=============================================
input_entry=c.CTkEntry(root,textvariable=entvar,font=("Helvetica",20,"bold"),width=350,justify=CENTER,fg_color="snow",text_color="grey",border_color="#FF6C22",border_width=8)
entry_placeholder = "Enter desired length"
input_entry.insert(0, entry_placeholder)                                 #displaying the placeholder text
input_entry.bind("<FocusIn>", focusin)                                   #placeholder text disappears when clicked to give input
input_entry.bind("<FocusOut>", focusout)
input_entry.grid(row=1,column=0,columnspan=4,padx=20,pady=5)

output_entry=c.CTkEntry(root,font=("Helvetica",20,"bold"),width=350,justify=RIGHT,fg_color="snow",text_color="#FF6C22",border_color="#FF6C22",border_width=8)
output_entry.grid(row=4,column=0,columnspan=4,padx=20,pady=5)

#============================Checkbox widgets to include specsial characters and numbers===================================
num=c.CTkCheckBox(root,text="Numbers",variable=numvar,border_color='#FF6C22',border_width=2,font=("Arial",12,"bold"),hover_color="#2B3499",checkmark_color="#FF6C22",corner_radius=60,text_color="#FF6C22")
num.grid(row=2,column=0,columnspan=2)

special_chars=c.CTkCheckBox(root,text="Special Characters",variable=special_charsvar,border_color='#FF6C22',border_width=2,font=("Arial",12,"bold"),hover_color="#2B3499",checkmark_color="#FF6C22",corner_radius=60,text_color="#FF6C22")
special_chars.grid(row=2,column=2,columnspan=2)

#========================================================Button widgets===================================================
generate_img=c.CTkImage(dark_image=Image.open("g_btn2.png"),size=(150,50))
generate=c.CTkButton(root,image=generate_img,text="",corner_radius=50,fg_color="transparent",width=150,cursor="hand2")
generate.grid(row=3,column=1,columnspan=2,pady=5)
generate.bind("<Button-1>", gen)

copy_img=c.CTkImage(dark_image=Image.open("c_btn2.png"),size=(150,50))
copy_btn=c.CTkButton(root,text="",image=copy_img,fg_color="transparent",width=120,cursor="hand2")
copy_btn.grid(row=5,column=1,columnspan=2,pady=5)
copy_btn.bind("<Button-1>", copy)


root.mainloop()
#=====================================================END of mainloop=====================================================