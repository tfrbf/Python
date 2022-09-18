import random


def winner(p1,p2):
    p1=int(0)
    p2=int(0)

    if p1=="rock" and p2=="paper":
        p1+=1
    elif p1=="rock" and p2=="siccor":
        p1+=1
    elif p1=="rock" and p2=="rock":
        pass
    elif p1=="paper" and p2=="rock":
        p2+=1
    elif p1=="paper" and p2=="siccor":
        p2+=1
    elif p1=="paper" and p2=="paper":
        pass
    elif p1=="siccor" and p2=="rock":
        p2+=1
    elif p1=="siccor" and p2=="paper":
        p1+=1
    elif p1=="siccor" and p2=="siccor":
        pass

    print(p1,p2)
    


pc_choice=("rock", "paper", "siccor")
user_choice=input("rock, siccor, paper ?")

x1=random.choice(pc_choice)
print("pc:",x1)
winner(x1,user_choice)

 