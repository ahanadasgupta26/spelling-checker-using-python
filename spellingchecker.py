from tkinter import *
from textblob import TextBlob

root=Tk()
root.title("Spelling Checker")
root.geometry("700x600")
root.resizable(False,False)
root.config(background='lightgreen')

def checking():
    a=TextBlob(spell.get())
    spelling=Label(root,text="The correct spelling is: ",font=("Times new roman",30,"bold"),bg="gray")
    spelling.pack(pady=10)
    correct=Label(root,text=str(a.correct()),font=("Arial",30,"bold"))
    correct.pack(pady=15)

def reset():
    spell.delete(0,END) 
    for widget in root.pack_slaves():
        if isinstance(widget,Label) and widget!=head and widget!=check:
            widget.pack_forget() 

head=Label(root,text="Spelling Checker",font=("Times new roman",30,"bold"),bg="lightblue",fg="black")
head.pack(pady=25)

check=Label(root,text="Enter the text",font=("Times new roman",20,"bold"),bg="lightgreen")
check.pack(pady=20)

spell=Entry(root,font=("Arial",15,"bold"),width=50,bg="lightpink") 
spell.pack(pady=20)

check_but=Button(root,text="Check",font=("Times new roman",20,"bold"),bg="gray",command=checking)
check_but.pack(pady=25)

reset_but = Button(root, text="Reset", font=("Times new roman", 20, "bold"), bg="gray", command=reset)
reset_but.pack(pady=25)

root.mainloop()