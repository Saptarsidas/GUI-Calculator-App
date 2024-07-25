import tkinter as Tk
from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("570x600+100+100")
root.resizable(False,False)
root.config(bg="black")

euqation=""
def show(value):
    global euqation
    euqation+=value
    label_resutl.config(text=euqation)
def clear():
    global euqation
    equation=""
    label_resutl.config(text=equation)

def calculate():
    global euqation
    result=""
    if euqation!="":
        try:
            result=eval(euqation)
        except:
            result="Error"
            euqation=""
    label_resutl.config(text=result)
label_resutl=Label(root,width=30,height=2,text="",font=("Arial",24))
label_resutl.pack()


Button(root,text="C",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(root,text="/",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("/")).place(x=150,y=100)
Button(root,text="%",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("%")).place(x=290,y=100)
Button(root,text="*",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("*")).place(x=430,y=100)

Button(root,text="7",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("7")).place(x=10,y=200)
Button(root,text="8",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("8")).place(x=150,y=200)
Button(root,text="9",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("9")).place(x=290,y=200)
Button(root,text="-",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("-")).place(x=430,y=200)


Button(root,text="4",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("4")).place(x=10,y=300)
Button(root,text="5",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("5")).place(x=150,y=300)
Button(root,text="6",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("6")).place(x=290,y=300)
Button(root,text="+",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("+")).place(x=430,y=300)


Button(root,text="1",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("1")).place(x=10,y=400)
Button(root,text="2",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("2")).place(x=150,y=400)
Button(root,text="3",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("3")).place(x=290,y=400)
Button(root,text="0",width=11,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("0")).place(x=10,y=500)

Button(root,text=".",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show(".")).place(x=290,y=500)
Button(root,text="=",width=5,height=3,font=("Arial",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda:calculate()).place(x=430,y=400)
root.mainloop()
