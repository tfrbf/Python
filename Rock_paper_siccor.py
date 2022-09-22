from asyncore import loop
import random
from tkinter import *


window=Tk()
window.title("ROCK - PAPER - SICCOR")
window.minsize(250,250)
window.geometry("400x400")



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