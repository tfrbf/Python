from asyncore import loop
from cProfile import label
from cgitb import text
from ctypes import alignment
import random
from tkinter import *
from tkinter import font
from turtle import left, right
from winreg import EnableReflectionKey
import emoji

window=Tk()
window.title("ROCK - PAPER - SICCOR")
window.minsize(250,250)


name=Label(window,text="Enter your name")
name.pack()

user_name=Entry(window)
user_name.pack()


rock_btn=Button(window,text="ROCK",activebackground="blue",width=10,anchor=CENTER)
rock_btn.pack()

paper_btn=Button(window,text="PAPER",activebackground="blue",width=10,anchor=CENTER)
paper_btn.pack()


siccors_btn=Button(window,text="SICCORS",activebackground="blue",width=10,anchor=CENTER)
siccors_btn.pack()








'''pc_dict=("rock", "paper", "siccor")

def winner():
    pc_point=0
    user_point=0

    while pc_point<=2 and user_point<=2:

        user_choice=input("rock, siccor, paper ?")
        pc_choice=random.choice(pc_dict)

        if pc_choice=="rock" and user_choice=="paper":
            user_point+=1
        elif pc_choice=="rock" and user_choice=="siccor":
            pc_point+=1
        elif pc_choice=="rock" and user_choice=="rock":
            pass
        elif pc_choice=="paper" and user_choice=="rock":
            user_point+=1
        elif pc_choice=="paper" and user_choice=="siccor":
            user_point+=1
        elif pc_choice=="paper" and user_choice=="paper":
            pass
        elif pc_choice=="siccor" and user_choice=="rock":
            user_point+=1
        elif pc_choice=="siccor" and user_choice=="paper":
            pc_point+=1
        elif pc_choice=="siccor" and user_choice=="siccor":
            pass

        print(f"you:{user_point} - pc:{pc_point}")
    if pc_point>user_point:
        print("pc wone!")
    else:
        print("you wone!")
    return user_point,pc_point
    

print("Resualt: ",winner())

'''
window.mainloop()