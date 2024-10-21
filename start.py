import tkinter

from TwoPlayer import TwoPlayer

def two_player():
    window.destroy()
    TwoPlayer()

window = tkinter.Tk()
window.minsize(width=500, height=500)
window.config(pady=200)


two_player = tkinter.Button(text="Two Player", command=two_player)
two_player.pack()
single_player = tkinter.Button(text="Single Player")
single_player.pack()



window.mainloop()