import tkinter as tk
import password_study as ps #importing the program
global entry
def create() :
    # ps.main()
    
    window=tk.Tk()
    window.title("Password Manager")

    window.rowconfigure(0,minsize=400)
    window.columnconfigure(1,minsize=400)
    
    pass_menu=tk.Menu(window)
    # pass_menu=tk.Menu(menubar,tearoff=0)
    pass_menu.add_command(label="Add",command=lambda:add_page())
    pass_menu.add_command(label="View",command=lambda:ps.view())
    pass_menu.add_command(label="Clear",command=lambda:ps.clear())
    
    window.config(menu=pass_menu)
    def submit():
        input=entry.get()
        print(input)
    def add_page() :
        label=tk.Label(window,text="Enter the ac name :")
        label.pack(pady=10)

        entry=tk.Entry(window)
        entry.pack(pady=10)
        submit_b=tk.Button(window,text="submit",command=lambda:submit())
        submit_b.pack(pady=10)
    window.mainloop()
create()

