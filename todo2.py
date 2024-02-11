from tkinter import*
import customtkinter as c
from PIL import Image

c.set_appearance_mode("light")
root=c.CTk()
root.geometry("650x400+400+150")
root.resizable(False,False)
root.iconbitmap("todo icon.ico")
root.title("To Do List:By Shivam Verma")

def focusin(event):
    if input_entry.get() == "Enter Your Task":
        input_entry.delete(0, END)
        input_entry.configure(text_color='red',font=("Helvetica",20, "bold"),justify=RIGHT,fg_color="#000000")

def focusout(event):
    if input_entry.get() == "":
        input_entry.insert(0, "Enter Your Task")
        input_entry.configure(text_color='grey',font=("Helvetica",20, "bold"),justify=CENTER,fg_color="#000000")

def add(event):
    global task
    if task.get()=="Enter Your Task":
        pass
    else:
        t=str(task.get())
        lbx.insert(END,f"{t}")                                
        with open('task_file.txt','a') as task_file:               
            t=t+"\n"
            task_file.write(t)
            task_file.seek(0)
            task_file.close()
        input_entry.delete(0,END) 

def delete(event):
    selected_index = lbx.curselection()
    if selected_index:
        lbx.delete(selected_index)
        with open('task_file.txt', 'r') as task_file:
            lines = task_file.readlines()
        with open('task_file.txt', 'w') as task_file:
            for i, line in enumerate(lines):
                if i != selected_index[0]:
                    task_file.write(line)

def previous_data():
    try:
        with open('task_file.txt', 'r') as task_file:
            tasks = task_file.readlines()
            for task in tasks:
                lbx.insert(END, task.strip())
    except FileNotFoundError:
        pass

def delete_all(lbx):
    total = lbx.size()
    lbx.delete(0, total - 1)
    with open('task_file.txt', 'w'):
        pass

task=StringVar()

logo=c.CTkImage(dark_image=Image.open("to do list.png"),size=(650,100))
top_img=c.CTkLabel(root,image=logo,text="")
top_img.grid(row=0,column=0,columnspan=6)

input_entry=c.CTkEntry(root,textvariable=task,font=("Helvetica",20,"bold"),width=300,justify=CENTER,fg_color="#000000",text_color="grey",border_color="#000000",border_width=8)
entry_placeholder = "Enter Your Task"
input_entry.insert(0, entry_placeholder)                                 
input_entry.bind("<FocusIn>", focusin)                                   
input_entry.bind("<FocusOut>", focusout)
input_entry.grid(row=1,column=0,columnspan=2,padx=10,pady=5)

lbx=Listbox(root,height=7,width=17,bg="black",relief=RIDGE,border=5,font=("Helvetica",20,"bold"),fg="red")
lbx.grid(row=1,column=2,columnspan=3,rowspan=4,pady=10,padx=10)

vscrollbar = Scrollbar(root, command=lbx.yview)
vscrollbar.grid(row=1, column=5,rowspan=4, sticky='ns',pady=10,padx=10)
lbx.config(yscrollcommand=vscrollbar.set)

hscrollbar = Scrollbar(root, command=lbx.xview,orient="horizontal")
hscrollbar.grid(row=5, column=2,columnspan=3, sticky='we',padx=10)
lbx.config(xscrollcommand=hscrollbar.set)


add_btn=c.CTkButton(root,text="ADD TASK",fg_color="#BBE2EC",font=("Helvetica",20,"bold"),text_color="#211C6A",width=300,height=50,cursor="hand2")
add_btn.grid(row=2,column=0,columnspan=2,padx=10,pady=5)
add_btn.bind("<Button-1>", add)

del_btn=c.CTkButton(root,text="DELETE TASK",fg_color="#BBE2EC",font=("Helvetica",20,"bold"),text_color="#0D9276",width=300,height=50,cursor="hand2")
del_btn.grid(row=3,column=0,columnspan=2,padx=10,pady=5)
del_btn.bind("<Button-1>", delete)

delall_btn=c.CTkButton(root,text="DELETE ALL",fg_color="#BBE2EC",font=("Helvetica",20,"bold"),text_color="red",width=300,height=50,cursor="hand2",command=lambda:delete_all(lbx))
delall_btn.grid(row=4,column=0,columnspan=2,padx=10,pady=5)

previous_data()
root.mainloop()
