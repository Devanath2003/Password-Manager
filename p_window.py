import tkinter as tk
import password_study as ps #importing the program
master_pass="master"
def create() :
    # ps.main()
    def submit(entry_ac_name,entry_pass):
        input_ac_name=entry_ac_name.get()
        input_pass=entry_pass.get()
        ps.add(input_ac_name,input_pass)
        entry_ac_name.delete(0,tk.END)
        entry_pass.delete(0,tk.END)
        
    def add_page() :
        
        label_ac_name=tk.Label(window,text="Enter the ac name :")
        label_ac_name.pack(pady=10)

        entry_ac_name=tk.Entry(window)
        entry_ac_name.pack(pady=10)
        label_pass=tk.Label(window,text="Enter the password :")
        label_pass.pack(pady=10)

        entry_pass=tk.Entry(window,show="*")
        entry_pass.pack(pady=10)
        submit_b=tk.Button(window,text="submit",command=lambda:submit(entry_ac_name,entry_pass))
        submit_b.pack(pady=10)
    def view_pass():
        
        label_master=tk.Label(window,text="Enter the Master password :")
        label_master.pack(pady=10)

        entry_master=tk.Entry(window)
        entry_master.pack(pady=10)

        input_master=entry_master.get()

        if input_master==master_pass :
            label_view=tk.Label(window,text="User and Pass")
            label_view.pack(pady=10)
            usr=ps.user
            pasword=ps.psw
            

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
    window.mainloop()
create()

