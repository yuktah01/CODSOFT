import tkinter as tkr
from tkinter import messagebox

def add_to_do():
    item = entry.get()
    if item:
        listbox.insert(tkr.END, item)
        entry.delete(0, tkr.END)
    else:
        messagebox.showwarning("Warning!", "The entry is empty. Please add a to-do task.")

def remove_to_do():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning!", "Select an item and then click 'remove' button.")

def mark_completed():
    try:
        index = listbox.curselection()[0]
        current_text = listbox.get(index)
        if "[Completed]" in current_text:
            new_text = current_text.replace("[Completed]", "").strip()
        else:
            new_text = f"[Completed] {current_text}"
            messagebox.showinfo("Hurray!", "Task Completed!")
        listbox.delete(index)
        listbox.insert(index, new_text)
    except IndexError:
        messagebox.showwarning("Warning!", "Select an item and then click 'mark completed' button.")

app = tkr.Tk()
app.title("GUI To-Do List")

# Box for entry and buttons
frame = tkr.Frame(app)
frame.pack(pady=10)

# Heading for entry field
entry_label = tkr.Label(frame, text="Enter a new to-do task:")
entry_label.pack()

entry = tkr.Entry(frame, width=50, bg="lightpink", fg="red")
entry.pack(side=tkr.LEFT, padx=5)

# Button to add the task
add_button = tkr.Button(frame, text="Add Task", command=add_to_do)
add_button.pack(side=tkr.LEFT, padx=5)

# Button to remove the task
remove_button = tkr.Button(frame, text="Remove Task", command=remove_to_do)
remove_button.pack(side=tkr.LEFT, padx=5)

# Button to mark the task as completed
mark_button = tkr.Button(frame, text="Mark Completed", command=mark_completed)
mark_button.pack(side=tkr.LEFT, padx=5)

# Heading for the listbox
listbox_label = tkr.Label(app, text="Your To-Do List:")
listbox_label.pack(pady=10)

listbox = tkr.Listbox(app, width=100, height=15, bg="lightblue", fg="darkblue")
listbox.pack(pady=10)

app.mainloop()