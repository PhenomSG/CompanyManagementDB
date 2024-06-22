import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# import all idk
#from tkinter import *

# functionalities
from main import *

# making frames

class PayrollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")

        # menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # making main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        
        # button
        ttk.Button(main_frame, text="Add Employee", command=self.add_employee).grid(row=0, column=0, padx=10, pady=10)

    def add_employee(self):
        messagebox.showinfo("Add Employee", "Functionality to add employee will be implemented here.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PayrollApp(root)
    root.mainloop()
