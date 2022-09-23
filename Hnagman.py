
import random
from tkinter import *
from tkinter.font import BOLD

def new_game():
    global answer, letter_list, all_chance

    #word list
    word=['banana','apple','mango','orange']

    answer=random.choice(word)

    letter_list=['-' for i in answer]
    all_chance=len(letter_list)+3

def end_game():
    new_game()
    label_word.config(text=f"{' '.join(letter_list)}")

def check_letters():
    global all_chance
    resualt.config(text=' ')
    new_letter = your_letter.get()

    if new_letter in answer:
        for indexes, letter in enumerate(answer):
            if letter==new_letter:
                letter_list[indexes]=letter
                label_word.config(text=f"{' '.join(letter_list)}")


    if (new_letter==answer) or ('-' not in letter_list):
        resualt.config(text=f'you won the game, answer is : {answer}')
        end_game()

    all_chance-=1
    your_letter.delete(0,END)

    label_chance.config(text=f"Remaning chance : {all_chance}")

    if all_chance==0:
        resualt.config(text=f'OOPS! you lose the game, answer is : {answer}')
        end_game()
new_game()

#tk intre
window=Tk()
window.title("Hangman game")
window.geometry("320x400")

label_word=Label(window, text=f"{' '.join(letter_list)}",
            justify="center",font=("tahoma",20))

label_word.pack(fill=BOTH,pady=25)

my_label=Label(window, text="Enter a letter or word",justify=CENTER,font=("tahome",20,BOLD))
my_label.pack(fill=BOTH,pady=25)

your_letter=Entry(window, justify="center",font=("tahoma",20))

your_letter.pack(fill=BOTH,pady=25)

btn= Button(window,text="Submit",font=("tahome",20), command=check_letters)
btn.pack(padx=10, pady=5)

label_chance=Label(window, text=f"Remaning chances : {all_chance}",justify="center", font=("tahoma",12))
label_chance.pack(fill="both",pady=5)
resualt = Label(window, font=("tahoma",10),text=' ', justify="center",bd=0,bg="systembuttonface")
resualt.pack(fill="both",pady=5)
window.mainloop()


#roze seshanbe
