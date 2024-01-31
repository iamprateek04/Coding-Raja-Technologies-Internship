# to-do-list application with GUI.

import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime




def add ():
    Task = enter_task.get()
    Priority = enter_priority.get()
    Due_Date = enter_due_date.get()


    enter_task.insert(END,Task)
    with open('data.txt', 'a') as file:
        file.write(Task)
        file.seek(0)
        file.close


    enter_priority.insert(END,Priority)
    with open('data.txt', 'a') as file:
        file.write(Priority)
        file.seek(0)
        file.close


    enter_due_date.insert(END,Due_Date)
    with open('data.txt', 'a') as file:
        file.write(Due_Date)
        file.seek(0)
        file.close



    if Task:
        task_data = {'Task': Task, 'Priority': Priority, 'Due-Date': Due_Date}
        listbox.insert(tk.END, task_data)
        enter_task.delete(0, tk.END)
        enter_priority.delete(0, tk.END)
        enter_due_date.delete(0, tk.END)
        save ()

    else:
        messagebox.showwarning("warning", "Please enter task to add.")


def delete ():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
        save ()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_completed():
    try:
        selected_task = listbox.curselection()[0]
        task = listbox.get(selected_task)
        completed_tasks.insert(tk.END, task)
        listbox.delete(selected_task)
        save ()
    except IndexError:
        messagebox.showwarning("Warning", "Please select task to mark completed.")

def save ():
    task_data = [listbox.get(i) for i in range(listbox.size())]
    with open("tasks.json", "w") as file:
        json.dump(task_data, file)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            task_data = json.load(file)
            for task_data in task_data:
                listbox.insert(tk.END, task_data)
    except FileNotFoundError:
        pass





root = tk.Tk()
root.title("To-Do-List")
root.geometry("900x650+400+100")



frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)



image_icon = PhotoImage(file="images/task.png")
root.iconphoto(False,image_icon)

topimage = PhotoImage(file="images/topbar.png")
Label(root,image=topimage).place(x=497,y=2)

dockimage = PhotoImage(file="images/dock.png")
Label(root,image=dockimage,bg="#32405b").place(x=530,y=25)

noteimage = PhotoImage(file="images/task.png")
Label(root,image=noteimage,bg="#32405b").place(x=840,y=19)




heading=Label(root,text="ALL TASKS",font="ariel 22 bold", fg="white",bg="#32405b")
heading.place(x=620,y=20)


heading=Label(root,text="ENTER TASK DETAILS",font="ariel 20 bold", fg="white",bg="#32405b",width=28,height=2)
heading.place(x=5,y=5)


heading=Label(root,text="COMPLETED TASK",font="ariel 20 bold", fg="white",bg="#32405b",width=28,height=2)
heading.place(x=5,y=430)





frame1= Frame(root,bd=3,width=300,height=400,bg="#32405b")
frame1.place(x=505,y=83)

listbox= Listbox(frame1,font=('ariel,12'),width=33,height=17,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT , fill=BOTH, padx=2)

completed_tasks = tk.Listbox(root, height=8, width=80, selectbackground="blue",border=4)
completed_tasks.place(x=5,y=505)




scrollbar_tasks = tk.Scrollbar(frame1)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(xscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox.xview)




heading=Label(root,text="TASK NAME",font="ariel 15 bold", fg="white",bg="#32405b",width=11)
heading.place(x=5,y=110)

heading=Label(root,text="PRIORITY",font="ariel 15 bold", fg="white",bg="#32405b",width=11)
heading.place(x=5,y=180)

heading=Label(root,text="DUE DATE",font="ariel 15 bold", fg="white",bg="#32405b",width=11)
heading.place(x=5,y=250)






enter_task = tk.Entry(root, width=30,font="ariel 15",border=4)
enter_task.place(x=160,y=112)

enter_priority = tk.Entry(root, width=30,font="ariel 15",border=4)
enter_priority.place(x=160,y=182)

enter_due_date = tk.Entry(root, width=30, font="ariel 15",border=4)
enter_due_date.place(x=160,y=252)






button_add = tk.Button(root, text="ADD TASK", width=20, border=3, command=add)
button_add.place(x=50,y=340)

button_delete = tk.Button(root, text="DELETE TASK", width=20,border=3, command=delete)
button_delete.place(x=300,y=340)

button_complete = tk.Button(root, text="MARK COMPLETE", width=25, border=3 , command=mark_completed)
button_complete.place(x=580,y=550)


load_tasks()


root.mainloop()







