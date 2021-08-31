import tkinter
import random

root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll Dice')

# Label om hem te displayen
label = tkinter.Label(root, text='', font=('Helvetica', 260))

# Knop activeert de functie
def rollen():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')
    label.pack()

# button
button = tkinter.Button(root, text='worp', foreground='green', command=rollen)

# Button packen
button.pack()

# Het menu open houden
root.mainloop()
