from typing import Tuple
import customtkinter as ct
import password_study as ps #importing the program
master_pass="master"
global count
class MyFrame(ct.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        

    def clearframe(self):
            for widget in self.winfo_children():
                 widget.destroy()


    def add(self):
         usr_nameLabel=ct.CTkLabel(self,text="Username")
         usr_nameLabel.grid(row=0,column=0,padx=10,pady=10,sticky="w")

         self.usr_entry=ct.CTkEntry(self)
         self.usr_entry.grid(row=0,column=1,padx=10,pady=10,sticky="ew")

         
         psw_Label=ct.CTkLabel(self,text="Password")
         psw_Label.grid(row=1,column=0,padx=10,pady=10,sticky="w")

         self.psw_entry=ct.CTkEntry(self,show="*")
         self.psw_entry.grid(row=1,column=1,padx=10,pady=10,sticky="ew")

         sub_Bt=ct.CTkButton(self,text="Submit",command=self.submit,fg_color="#00C000",hover_color="#007300",text_color="white")
         sub_Bt.grid(row=2,column=0,columnspan=2,padx=10,pady=10,sticky="ew")
    def view(self):
        global count
        count=0
        label_master=ct.CTkLabel(self,text="Master Password")
        label_master.grid(row=0,column=0,padx=10,pady=10,sticky="w")

        self.master_entry=ct.CTkEntry(self)
        self.master_entry.grid(row=0,column=1,padx=10,pady=10,sticky="ew")

        sub_Bt_Master=ct.CTkButton(self,text="Submit",command=self.submitcheck,fg_color="#0086ff",hover_color="#03315a",text_color="white")
        sub_Bt_Master.grid(row=1,column=0,columnspan=2,padx=10,pady=10,sticky="ew")
        

    def submitcheck(self):
        global count
        input_master = self.master_entry.get()
        self.master_entry.delete(0,ct.END)
        
        if input_master == master_pass:
            self.clearframe()
            credentials = ps.view()  
            for username, password in credentials:
                ct.CTkLabel(self, text=f"User: {username} - Password: {password}").grid(pady=5)
        else:
            ct.CTkLabel(self, text="🚫 Incorrect Master Password").grid(pady=10)
            count=count+1
            if (count==4):
                self.clearframe()
                ct.CTkLabel(self,text="⚠️ System Locked ⚠️").grid(pady=5)

    def submit(self):
        input_ac_name=self.usr_entry.get()
        input_pass=self.psw_entry.get()
        ps.add(input_ac_name,input_pass)
        self.usr_entry.delete(0,ct.END)
        self.psw_entry.delete(0,ct.END)

class Window(ct.CTk):
    def __init__(self):
        super().__init__()
        
        
        self.title("Password Manager")
        self.geometry("500x250")
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.Menuframe = ct.CTkFrame(self,width=100)
        self.Menuframe.grid(row=0,column=0,padx=10,pady=(10,10),sticky="nsw") #padx,.pady control the spacing within the boundaries.
        
        self.Add_button=ct.CTkButton(self.Menuframe,text="Add",command=self.addpage,fg_color="#00C000",hover_color="#007300",text_color="white")
        self.Add_button.grid(row=0,column=0,padx=10,pady=10,sticky="ew")

        self.View_button=ct.CTkButton(self.Menuframe,text="View",command=self.viewpage,fg_color="#0086ff",hover_color="#03315a",text_color="white")
        self.View_button.grid(row=1,column=0,padx=10,pady=10,sticky="ew")

        self.Clear_button=ct.CTkButton(self.Menuframe,text="Clear",command=ps.clear,fg_color="#f44336",
                                          hover_color="#89221F",
                                          text_color="white")
        self.Clear_button.grid(row=2,column=0,padx=10,pady=10,sticky="ew")

        self.Contentframe = MyFrame(master=self)
        self.Contentframe.grid(row=0,column=1,padx=1,pady=(10,10),sticky="nsew")

        # self.Contentframe = ct.CTkFrame(self)
        # self.Contentframe.grid(row=0,column=1,padx=10,pady=(10,10),sticky="nsew")
        
    
            
    def addpage(self):
        self.Contentframe.clearframe()
        self.Contentframe.add()  
        
    def viewpage(self):
         self.Contentframe.clearframe()
         self.Contentframe.view()

window =Window()
window.mainloop()