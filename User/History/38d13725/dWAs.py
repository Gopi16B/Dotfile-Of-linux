import tkinter as tk 
import random


window=tk.Tk()
window.title("Hangman Game")
window.minsize(width=200,height=300)
window.resizable(False,False)



def reset_game():
    global word, underscores, tries
    word = random.choice(words).upper()
    underscores=" ".join(["_"]*len(word))
    label.config(text=underscores)
    tries=len(word)-1
    tries_text.config(text="tries left:"+str(tries))
    result_text.config(text="")
    messagebox.delete(0,1)

def ok():
    popup.destroy()
    reset_game()

def Underscore():
    global underscores
    global underscores_list
    guess=messagebox.get().upper()
    for i in range(len(word)):
        if word[i]==guess:
            position=i*2
            underscores_list=list(underscores)
            underscores_list[position]=guess
            underscores="".join(underscores_list)
            label.config(text=underscores)
def exit1():
    popup.destroy()
    window.destroy()

def PopupFunc(Bp):
        global popup
        popup=tk.Tk()
        popup.title("You Win!")
        popup.resizable(False,False)
        if Bp==True:
                win_label=tk.Label(popup,text="Congratulations! You guessed the word!",font=("Arial",14))
                win_label.pack(padx=20,pady=20)
                Again_button=tk.Button(popup,text="Play Again",command=ok)
                Again_button.pack()
                Exit_button=tk.Button(popup,text="Exit",command=exit1)
                Exit_button.pack()
        else:
                lose_label=tk.Label(popup,text=f"Sorry, you lost! The word was: {word}",font=("Arial",14))
                lose_label.pack(padx=20,pady=20)
                Again_button=tk.Button(popup,text="Play Again",command=ok)
                Again_button.pack()
                Exit_button=tk.Button(popup,text="Exit",command=exit1)
                Exit_button.pack()

        popup.mainloop()

def SubAction():
    guess=messagebox.get().upper()
    print(guess)
    print(word)
    tries=len(word)-1
    position=word.find(guess)
    print(position)

    if guess == "":
        result_text.config(text="Please enter a letter")
    elif guess in word:
        result_text.config(text="Nice")
        Underscore()
        if "_" not in underscores:
            PopupFunc(True)

    elif guess not in word:
        tries-=1
        tries_text.config(text="tries left:"+str(tries))
        if tries==0:
            PopupFunc(False)


            
            

    else:
        result_text.config(text="Nope")




words = ["PYTHON", "HANGMAN", "COMPUTER", "KEYBOARD", "PRINTER", "PROGRAM", "WINDOW", "MONITOR", "INTERNET", "NETWORK"]
word = random.choice(words).upper()

underscores = " ".join(["_"]*len(word))


label=tk.Label(window,text=underscores,font=("Arial",27))
label.grid(row=0,column=2,padx=10,pady=10)



messagebox=tk.Entry(window,width=10,font=("Arial",24),justify="center",bg="lightgrey",fg="black")
messagebox.grid(row=1,column=2,padx=30,pady=30)

messagebox.bind("<Return>", lambda event: SubAction())

submit=tk.Button(window,text="Submit",font=("Arial",14), command=SubAction)
submit.grid(row=2,column=2) 

result_text=tk.Label(window,text="")
result_text.grid(row=3,column=2)


tries=len(word)-1

tries_text=tk.Label(window,text="tries left:"+str(tries))
tries_text.grid(row=4,column=2)


window.mainloop()