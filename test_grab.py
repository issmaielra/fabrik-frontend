import tkinter as tk

root = tk.Tk()
root.title("Main Window")

top = tk.Toplevel(root)
top.title("Dialog without grab_set")
# Without grab_set() the user can click the main window while the dialog is open.

root.mainloop()
