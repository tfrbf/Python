import random
from tkinter import *

#global variebels
pc_point=0
user_point=0



window=Tk()
window.title("ROCK - PAPER - SICCOR")
window.minsize(250,250)




#functions
def greeting():
    #print("welcome",user_name.get())
    greeting_label.config(text="welcome {}".format(user_name.get()))


def user():
    pass





user_choice=Label(window,text="")
user_choice.pack()
#name box
name=Label(window,text="Enter your name")
name.pack()

user_name=Entry(window)
user_name.pack()

#submit useres name
Button(window,text="submit",command=greeting).pack()
greeting_label=Label(window,text="")
greeting_label.pack()


#points
point_user=Label(window,text="You: ")
point_user.pack()

point_pc=Label(window,text="PC: ")
point_pc.pack()



#Buttons
rock_btn=Button(window,text="ROCK",activebackground="blue",width=10,anchor=CENTER,command=user)
rock_btn.pack()

paper_btn=Button(window,text="PAPER",activebackground="blue",width=10,anchor=CENTER)
paper_btn.pack()

siccors_btn=Button(window,text="SICCORS",activebackground="blue",width=10,anchor=CENTER)
siccors_btn.pack()








'''pc_dict=("rock", "paper", "siccor")

def winner():
    

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

        print(f"{username}:{user_point} - pc:{pc_point}")
    if pc_point>user_point:
        print("pc wone!")
    else:
        print("you wone!")
    return user_point,pc_point
    

print("Resualt: ",winner())

'''
window.mainloop()