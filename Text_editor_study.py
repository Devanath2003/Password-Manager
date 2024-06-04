import tkinter as tk #allow window -we can do different things-may be like swing
from tkinter.filedialog import askopenfilename,asksaveasfilename

def open_file(window,text_editor):
    
    file_path=askopenfilename(filetypes=[("Text Files","*.txt")]) #the format which the file to be saved is given
    if not file_path : 
        return
    text_editor.delete(1.0,tk.END) #so we need to clear the text editor starting from(1,0)-1st line and 0th character to END
    with open(file_path, "r") as f:
        content=f.read()
        text_editor.insert(tk.END,content)
    window.title(f"File :{file_path}")

def save_file(window,text_editor):
    file_path=asksaveasfilename(filetypes=[("Text Files","*.txt")])

    
    if not file_path:
        return
    with open(file_path,"w") as f:
        content=text_editor.get(1.0,tk.END)
        f.write(content)
    window.title(f"Saved file:{file_path}")
    
def close_window(window): #to close the window
    window.destroy()
    




def main() :
    window=tk.Tk() #make a window for the text edw
    window.title("DRText Editor")

    window.rowconfigure(0,minsize=400) #set the size of the text editor window
    window.columnconfigure(1,minsize=400)

    text_editor=tk.Text(window,font="Helvetica 18") #first widget for text editor
    text_editor.grid(row=0,column=1) #the text editor is placed on the basis of grid system of tkinter

    frame=tk.Frame(window,relief=tk.RAISED,bd=2) #creating a frame for the buttons- parameters are-"window=to where it placed", "relief=is for providing a 3D effect with RAISED effect","bd=border width"
    
    save_button=tk.Button(frame,text="Save",command=lambda:save_file(window,text_editor)) #creating the save button
    open_button=tk.Button(frame,text="Open",command=lambda:open_file(window,text_editor)) #, the "lambda" is a kind of function used here, that ensure the function open file is only called when the button pressed. 
    save_button.grid(row=0,column=0,padx=5,pady=5,sticky="ew") #setting the buttons within the frame created, providing a padding something
    open_button.grid(row=1,column=0,padx=5,sticky="ew") #so here we used the sticky -that we can manage the width of both buttons as same
    frame.grid(row=0,column=0,sticky="ns") #setting the frame within the window , the sticky will stick the frame to the ns=north south direction

    window.bind("<Control-s>",lambda x:save_file(window,text_editor)) #applying key bindings
    window.bind("<Control-o>",lambda x:open_file(window,text_editor)) #x is an argument-which pass to the function
    window.bind("<Control-q>",lambda x:close_window(window)) 
    # window.bind("<Control-q>",
   
    window.mainloop() #keep it alive the window until we click the x

main() #-calling this function will produce a window 