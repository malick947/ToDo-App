import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

def remove_task():
    try:
        selected_task = listbox.curselection()
        listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "No task selected")

root = tk.Tk()
root.title("To-Do List - DevA")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=5)

root.mainloop()
#new things are added