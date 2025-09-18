import tkinter as tk 
import random


window=tk.Tk()
window.title("Hangman Game")
window.minsize(width=210,height=250)
window.resizable(False,False)
window.config(bg="#1F2229")


def reset_game():
    global word, underscores, tries
    word = random.choice(words).upper()
    underscores=" ".join(["_"]*len(word))
    underscores_list=list(underscores)
    underscores_list[0]=word[0]
    underscores="".join(underscores_list)
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
        popup.title("")
        popup.resizable(False,False)
        popup.config(bg="#1F2229")

        if Bp==True:
                win_label=tk.Label(popup,text="Congratulations! You guessed the word!",font=("Arial",14),bg="#1F2229",fg="#E5E8EE")
                win_label.pack(padx=20,pady=20)
                Again_button=tk.Button(popup,text="Play Again",command=ok,bg="#4CAF50", fg="white",activebackground="#45a049", activeforeground="white")
                Again_button.pack()
                Exit_button=tk.Button(popup,text="Exit",command=exit1,bg="#E63946", fg="white",activebackground="#c53030", activeforeground="white")
                Exit_button.pack()
        else:
                lose_label=tk.Label(popup,text="Sorry, you lost! The word was:"+word,font=("Arial",14),bg="#1F2229",fg="#E5E8EE")
                lose_label.pack(padx=20,pady=20)
                Again_button=tk.Button(popup,text="Play Again",command=ok,bg="#256327", fg="white",activebackground="#45a049", activeforeground="white")
                Again_button.pack()
                Exit_button=tk.Button(popup,text="Exit",command=exit1,bg="#E63946", fg="white",activebackground="#c53030", activeforeground="white")
                Exit_button.pack()
        Exit_button.config(highlightbackground="#E63946")
        Again_button.config(highlightbackground="#256327")

        popup.mainloop()

def SubAction():
    guess=messagebox.get().upper()
    print(guess)
    print(word)
    global tries
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
    messagebox.delete(0,1)



words = ["PYTHON", "HANGMAN", "COMPUTER", "KEYBOARD", "PRINTER", "PROGRAM", "WINDOW", "MONITOR", "INTERNET", "NETWORK"]
word = random.choice(words).upper()

underscores = " ".join(["_"]*len(word))
underscores_list=list(underscores)
underscores_list[0]=word[0]
underscores="".join(underscores_list)

label=tk.Label(window,text=underscores,font=("Arial",27),bg="#1F2229",fg='#ECEFF4')
label.grid(row=0,column=2,padx=10,pady=10)



messagebox=tk.Entry(window,width=3,font=("Arial",24),justify="center",bg="#6B6C6D",fg="#eceff4",highlightbackground="#6B6C6D",border=0)
messagebox.grid(row=1,column=2,padx=30,pady=30)

messagebox.bind("<Return>", lambda event: SubAction())

submit=tk.Button(window,text="Submit",font=("Arial",14), command=SubAction,bg="#194B1B", fg="white", activebackground="#194B1B", activeforeground="#26C02B",border=False)
submit.grid(row=2,column=2) 

result_text=tk.Label(window,text="",bg='#1F2229',fg='#ECEFF4')
result_text.grid(row=3,column=2)


tries=len(word)-1
tries_text=tk.Label(window,text="tries left:"+str(tries),bg='#1F2229',fg='#ECEFF4')
tries_text.grid(row=4,column=2)

submit.config(highlightbackground="#194B1B",relief="flat")


window.mainloop()






