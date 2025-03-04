import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Task cannot be empty")

def clear_all():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List - DevB")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

clear_button = tk.Button(root, text="Clear All", command=clear_all)
clear_button.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=5)

root.mainloop()