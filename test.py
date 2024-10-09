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
    
    def clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()
    def add_page() :
        clear_frame(content_frame)
        label_ac_name=tk.Label(content_frame,text="Enter the ac name :")
        label_ac_name.pack(pady=10)

        entry_ac_name=tk.Entry(content_frame)
        entry_ac_name.pack(pady=10)
        label_pass=tk.Label(content_frame,text="Enter the password :")
        label_pass.pack(pady=10)

        entry_pass=tk.Entry(content_frame,show="*")
        entry_pass.pack(pady=10)
        submit_b=tk.Button(content_frame,text="submit",command=lambda:submit(entry_ac_name,entry_pass))
        submit_b.pack(pady=10)
    def view_pass():
        
        clear_frame(content_frame)
        
        label_master=tk.Label(content_frame,text="Enter the Master password :")
        label_master.pack(pady=10)

        entry_master=tk.Entry(content_frame)
        entry_master.pack(pady=10)

        def check_master():
             input_master = entry_master.get()
             if input_master == master_pass:
                clear_frame(content_frame)
                credentials = ps.view()  # Get the list of tuples like [(username, password), ...]
                for username, password in credentials:
                    tk.Label(content_frame, text=f"User: {username} - Password: {password}").pack(pady=5)
             else:
                tk.Label(content_frame, text="Incorrect Master Password").pack(pady=10)
        
        submit_master = tk.Button(content_frame, text="Submit", command=check_master)
        submit_master.pack(pady=10)
    
            

    window=tk.Tk()
    window.title("Password Manager")

    content_frame = tk.Frame(window)
    content_frame.pack(fill="both", expand=True)

    window.rowconfigure(0,minsize=400)
    window.columnconfigure(1,minsize=400)
    
    pass_menu=tk.Menu(window)
    # pass_menu=tk.Menu(menubar,tearoff=0)
    pass_menu.add_command(label="Add",command=lambda:add_page())
    pass_menu.add_command(label="View",command=lambda:view_pass())
    pass_menu.add_command(label="Clear",command=lambda:ps.clear())
    
    window.config(menu=pass_menu)
    window.mainloop()
create()

