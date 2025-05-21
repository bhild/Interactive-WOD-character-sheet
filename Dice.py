from tkinter import *
import random
from tkinter.ttk import Combobox

root=Tk()
root.geometry("600x80")
mastery = IntVar()

#recursivly handles mastery rolls
def dice_loop(dc,rawDice):
    roll = random.randint(1, 10)#rolls a d10
    suc = 0
    rawDice += str(roll) + ','#adds roll to log
    if roll >= dc:#only 2 cases need success or botch
        suc += 1
        if roll == 10 and mastery.get() == 1: #this runs if the mastery conditions are met
            temp = dice_loop(dc,rawDice) #recursive call
            if not temp[0] == -1: #ensures that only non-botch mastery rolls are counted
                suc += temp[0]
                rawDice = temp[1]
    elif roll == 1: #botch removes 1 success
        suc -= 1
    return [suc,rawDice]#returns array of the dice rolls and number of successes

#outputs the dice based on the input from the comboboxes uses dice_loop as a helper function
def roll_my_dice():
    rolls = int(combobox[0].get())+int(combobox[1].get()) #get values from combobox and cast to int summing for num dice
    dc = int(combobox[2].get()) #get values from combobox and cast to int
    successes = 0 #storage for number of successes
    rawDice = '' #storage for dice log
    for x in range(rolls): #call dice_loop for each dice roll
        temp = dice_loop(dc,rawDice)
        rawDice = temp[1] #store dice log
        successes += temp[0]#store successes
    rawDice = rawDice[0:len(rawDice)-1]#remove trailing comma
    if successes <= 0: #special botch case
        results.configure(text='Botch: '+ str(successes))
    else: #non-botch output
        results.configure(text="Successes: "+successes)
    diceOut.configure(text="Result: "+rawDice) #output dice log

#create the comboboxes (dropdowns)
options = ['0','1','2','3','4','5','6','7','8','9','10']
#this goes to 10 to allow trivial skill checks and supernatural skill and/or attributes
num_combobox = 3
combobox = [] #this is the storage for the comboboxes
for i in range(num_combobox):
    comboboxT = Combobox(root,state='readonly',values=options,height=10,width=9)
    comboboxT.place(x=i*80+5,y=5) #dynamicly determine location
    combobox.append(comboboxT) #add to array
#set defaults for the comboboxes which will be unselectable
combobox[0].set('attribute')
combobox[1].set('skill')
combobox[2].set('dc')

#this is the button to indicate weather or not to roll with mastery
Checkbutton(root, text='mastery', variable=mastery, onvalue=1, offvalue=0).place(x=250,y=5)
#this is the button to roll dice
rollButton=Button(root, height=1, width=6, text="Roll", command=lambda: roll_my_dice())
rollButton.place(x=330,y=5)
#output fields
diceOut = Label(root, text='Raw Dice Here')
diceOut.place(x=10,y=45)
results = Label(root, text='Results')
results.place(x=420,y=5)

mainloop()