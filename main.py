# Kerolos Amgad

import tkinter
from tkinter import *



"""
hex code : name of color
#17161b : Duron Tricorn Black color
#fff : white color
#3697f5 : sky berry color
#2a2d36 : Ebony color 
#fe9037 :  medium light shade of orange
"""
root =Tk()
root.title ("Simple Calculator App")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b") # Duron Tricorn Black color
equation=""
def clear ():
    """the clear function , use it to clear anything in result label"""
    global equation
    equation=""
    result_label.config(text="")
def show (value):
    """the show fuction is used to show all symbols in result label"""
    global equation
    equation+=value
    result_label.config(text=equation)
def calculate ():
    """the calculate function used to calculate the operation """
    global equation
    result=""
    if equation !="" :
        try:
            result=eval(equation) # The eval() function evaluates the specified expression
        except:
            result="error"
            equation=""
    result_label.config(text=result)




#----------------------------Label---------------------------
result_label=Label(root,text="",width=25, height=2 , font=("arial",30))
result_label.pack()
#-----------------------------Buttons---------------------------------

# C / % *
clear_button =Button (root, text="C", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#3697f5", command=lambda :clear()).place(x=10, y=100)
division_button =Button (root, text="/", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("/")).place(x=150, y=100)
percentage_button =Button (root, text="%", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("%")).place(x=290, y=100)
multiply_button =Button (root, text="*", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("*")).place(x=430, y=100)

# 7 8 9 -
seven_button =Button (root, text="7", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("7")).place(x=10, y=200)
eight_button =Button (root, text="8", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("8")).place(x=150, y=200)
nine_button =Button (root, text="9", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("9")).place(x=290, y=200)
subtract_button =Button (root, text="-", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("-")).place(x=430, y=200)

#4 5 6 +
four_button =Button (root, text="4", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("4")).place(x=10, y=300)
five_button =Button (root, text="5", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("5")).place(x=150, y=300)
six_button =Button (root, text="6", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("6")).place(x=290, y=300)
add_button =Button (root, text="+", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("+")).place(x=430, y=300)

# 1 2 3 0
one_button =Button (root, text="1", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("1")).place(x=10, y=400)
two_button =Button (root, text="2", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("2")).place(x=150, y=400)
three_button =Button (root, text="3", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("3")).place(x=290, y=400)
zero_button =Button (root, text="0", width=11 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show("0")).place(x=10, y=500)

# . =
dot_button =Button (root, text=".", width=5 , height=1 , font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda :show(".")).place(x=290, y=500)
equal_button =Button (root, text="=", width=5 , height=3 , font=("arial",30,"bold"),fg="#fff",bg="#fe9037",command=lambda :calculate()).place(x=430, y=400)


root.mainloop()