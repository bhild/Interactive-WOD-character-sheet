from tkinter import *
import random
from tkinter.ttk import Combobox
from operator import itemgetter
import json

root=Tk()
attribute_values = [[1,1,1],[1,1,1],[1,1,1]]#initlize to 1 because that is the min barring exceptional circumstance
abilities_values = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
virtue_values = [0,0,0]
ten_point_values = [0,0,0]
ten_point_values_max = [0,0,0]
health_value = 0
dc = 0
mastery = IntVar()
attribute_selected = StringVar()
ability_selected = StringVar()

attribute_names = [["Strength","Dexterity","Stamina"],["Charisma","Manipulation","Appearance"],
                   ["Perception","Intelligence","Wits"]]#this stores the name of each attrubtue to popuplate the UI
abilities_names = [["Acting","Alertness","Athletics","Brawl","Doge","Empathy","Intimidation","Leadership","Streetwise","Subtrafuge"]#talents
                   ,["Animal Ken","Drivfe","Etiquette","Firearms","Melle","Music","Repair","Security","Stelth","Surival"]#Skills
                   ,["Bureaucracy","Computer","Finance","Investigation","Law","Linguistics","Medicine","Occult","Pilitics","Science"]#knowlages
                   ]#this stores the name of each abilities to popuplate the UI
virtue_names = ["Conscience","Self-Control","Courage"]
ten_point_names = ["Humanity","Willpower","Faith"]
health_values_name = ["Healthy","Bruised","Hurt","Injured","Wounded","Mauled","Crippled","Incapacitated"]

def update_value_DC(a,n):
    global dc
    dc = int(n)
def update_value_attribute(a,b,n):
    attribute_values[a][b] = int(n)#update the approrate array
    writeToFile()#overwrite the old data with new data
def update_value_ablity(a,b,n):
    abilities_values[a][b] = int(n)
    writeToFile()
def update_value_virtue(a,n):
    ten_point_values_max[a] = int(n)
    writeToFile()
def update_value_10s(a,n,comboboxM):
    if int(n) > ten_point_values_max[a]:#prevent a user from making a current value more than the maximum value
         ten_point_values[a] = ten_point_values_max[a]
    else:
         ten_point_values[a] = int(n)
    comboboxM.set(ten_point_values[a])
    writeToFile()
def update_value_10s_MAX(a,n):
    ten_point_values_max[a] = int(n)
    writeToFile()
def update_value_health(a,n):
    global health_value
    health_value = health_values_name.index(n)
    writeToFile()
def getAllFromFile():
    global attribute_values
    global abilities_values
    global ten_point_values
    global ten_point_values
    global ten_point_values_max
    global virtue_values
    global health_value
    try:
        with open('output.txt', 'r') as file:
            attribute_values = json.loads(file.readline())
            abilities_values = json.loads(file.readline())
            ten_point_values = json.loads(file.readline())
            ten_point_values_max = json.loads(file.readline())
            virtue_values = json.loads(file.readline())
            health_value = int(json.loads(file.readline()))
    except:
        writeToFile()
def writeToFile():
    global attribute_values
    global abilities_values
    global ten_point_values
    global ten_point_values
    global ten_point_values_max
    global virtue_values
    global health_value
    with open('output.txt', 'w') as filehandle:
        json.dump(attribute_values, filehandle)
        filehandle.write('\n')
        json.dump(abilities_values, filehandle)
        filehandle.write('\n')
        json.dump(ten_point_values, filehandle)
        filehandle.write('\n')
        json.dump(ten_point_values_max, filehandle)
        filehandle.write('\n')
        json.dump(virtue_values, filehandle)
        filehandle.write('\n')
        json.dump(health_value, filehandle)

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
    global dc
    global health_value
    global modInputCount
    if typeBox.get() == "Initive":
        rolls = attribute_values[0][1] + attribute_values[2][2]
    else:
        v1 = attribute_values[int(attribute_selected.get().split(",")[0])][int(attribute_selected.get().split(",")[1])]
        v2 = abilities_values[int(ability_selected.get().split(",")[0])][int(ability_selected.get().split(",")[1])]
        rolls = int(v1)+int(v2) #get values from combobox and cast to int summing for num dice
    rolls = min(rolls,rolls+1-health_value) + int(modInputCount.get())
    dc = int(dc) #get values from combobox and cast to int
    successes = 0 #storage for number of successes
    rawDice = '' #storage for dice log
    for x in range(rolls): #call dice_loop for each dice roll
        temp = dice_loop(dc,rawDice)
        rawDice = temp[1] #store dice log
        successes += temp[0]#store successes
    rawDice = rawDice[0:len(rawDice)-1]#remove trailing comma
    successes += int(modInputValue.get())
    if successes <= 0: #special botch case
        results.configure(text='Botch: '+ str(successes))
    else: #non-botch output
        results.configure(text="Successes: "+str(successes))
    diceOut.configure(text="Result: "+str(rawDice)) #output dice log
    diceCount.configure(text="Total Dice: "+ str(min(rolls,len(rawDice.split(",")))))
def predict_my_dice():
    global dc
    global health_value
    global mastery
    if typeBox.get() == "Initive":
        rolls = attribute_values[0][1] + attribute_values[2][2] + int(modInputCount.get())
    else:
        v1 = attribute_values[int(attribute_selected.get().split(",")[0])][int(attribute_selected.get().split(",")[1])]
        v2 = abilities_values[int(ability_selected.get().split(",")[0])][int(ability_selected.get().split(",")[1])]
        rolls = int(v1)+int(v2) #get values from combobox and cast to int summing for num dice
    rolls = min(rolls,rolls+1-health_value)
    prediction = ((10-dc)*rolls)*.1 + int(modInputValue.get())
    if mastery.get() == 1:
        prediction += rolls*.1
    predictFeild.configure(text="Expected Successes: " + str(prediction))    
def clear_values():
    global mastery
    global dc
    global attribute_selected
    global ability_selected
    modInputValue.delete(0,END)
    modInputCount.delete(0,END)
    modInputValue.insert(INSERT,"0")
    modInputCount.insert(INSERT,"0")
    mastery.set(0)
    dc = 0
    dcComboBox.set(0)
    typeBox.set("")
    attribute_selected.set("-1,-1")
    ability_selected.set("-1,-1")


getAllFromFile()
root.title("WOD 1st edition character sheet (Hunter)")
screen_x_scale = int(root.winfo_screenwidth()/1512)
screen_y_scale = int(root.winfo_screenheight()/982)
box_width = 13*screen_x_scale
box_height = 1*screen_y_scale
root.geometry(str(int(1000*screen_x_scale))+"x"+str(int(900*screen_y_scale)))


for i in range(3):#this loop creates the attribute names and feilds
    for j in range(3):
        text_stat_temp = Text(root,height=box_height,width=box_width)#this line and the following create the attribute titles and values
        text_stat_temp.insert(INSERT,attribute_names[i][j])#add the correct name
        text_stat_temp.bindtags((str(text_stat_temp), str(root), "all"))#stop the user from clicking on or typing in the feild
        text_stat_temp.place(x=(i*230+20)*screen_x_scale,y=(j*30+50)*screen_y_scale)#place at the target location
        comboboxT = Combobox(root,state='readonly',values=[0,1,2,3,4,5],height=box_height,width=1,exportselection=0)#create a comboBox that the user can not type into
        comboboxT.place(x=(i*230+35+box_width*6)*screen_x_scale,y=(j*30+50)*screen_y_scale)#place at the target location
        comboboxT.bind("<<ComboboxSelected>>", lambda event,i=i,j=j: update_value_attribute(i,j,event.widget.get()))#cause the combobox to run the target function when a selection is made
        comboboxT.set(attribute_values[i][j])# make the combo box display the correct value to begin with
        Radiobutton(
            root,
            text="",
            variable=attribute_selected,
            value=str(i)+","+str(j),
        ).place(x=(i*230+35+box_width*9)*screen_x_scale,y=(j*30+50)*screen_y_scale)

for i in range(3):#this loop creates the ability names and feilds
    for j in range(10):
        text_stat_temp = Text(root,height=box_height,width=box_width)#this line and the following create the ability titles and values
        text_stat_temp.insert(INSERT,abilities_names[i][j])
        text_stat_temp.bindtags((str(text_stat_temp), str(root), "all"))
        text_stat_temp.place(x=(i*230+20)*screen_x_scale,y=(j*30+50+120)*screen_y_scale)
        comboboxT = Combobox(root,state='readonly',values=[0,1,2,3,4,5],height=box_height,width=1)
        comboboxT.place(x=(i*230+35+box_width*6)*screen_x_scale,y=(j*30+50+120)*screen_y_scale)
        comboboxT.bind("<<ComboboxSelected>>", lambda event,i=i,j=j: update_value_ablity(i,j,event.widget.get()))
        comboboxT.set(abilities_values[i][j])
        Radiobutton(
            root,
            text="",
            variable=ability_selected,
            value=str(i)+","+str(j),
            ).place(x=(i*230+35+box_width*9)*screen_x_scale,y=(j*30+50+120)*screen_y_scale)

for i in range(3):
        text_stat_temp = Text(root,height=box_height,width=box_width)#this line and the following create the virtue titles and values
        text_stat_temp.insert(INSERT,virtue_names[i])
        text_stat_temp.bindtags((str(text_stat_temp), str(root), "all"))
        text_stat_temp.place(x=(i*230+20)*screen_x_scale,y=(50+440)*screen_y_scale)
        comboboxT = Combobox(root,state='readonly',values=[0,1,2,3,4,5],height=box_height,width=1)
        comboboxT.place(x=(i*230+35+box_width*6)*screen_x_scale,y=(50+440)*screen_y_scale)
        comboboxT.bind("<<ComboboxSelected>>", lambda event,i=i: update_value_virtue(i,event.widget.get()))
        comboboxT.set(virtue_values[i])

for i in range(3):
        text_stat_temp = Text(root,height=box_height,width=box_width)#this line and the following create the 10 point titles and values
        text_stat_temp.insert(INSERT,ten_point_names[i])
        text_stat_temp.bindtags((str(text_stat_temp), str(root), "all"))
        text_stat_temp.place(x=(i*230+20)*screen_x_scale,y=(80+440)*screen_y_scale)
        comboboxT = Combobox(root,state='readonly',values=[0,1,2,3,4,5,6,7,8,9,10],height=box_height,width=1)
        comboboxT.place(x=(i*230+35+box_width*6)*screen_x_scale,y=(80+440)*screen_y_scale)
        comboboxM = Combobox(root,state='readonly',values=[0,1,2,3,4,5,6,7,8,9,10],height=box_height,width=1)
        comboboxM.place(x=(i*230+70+box_width*6)*screen_x_scale,y=(80+440)*screen_y_scale)
        comboboxT.bind("<<ComboboxSelected>>", lambda event,i=i: update_value_10s_MAX(i,event.widget.get()))
        comboboxM.bind("<<ComboboxSelected>>", lambda event,i=i,comboboxM=comboboxM: update_value_10s(i,event.widget.get(),comboboxM))
        comboboxT.set(ten_point_values_max[i])
        comboboxM.set(ten_point_values[i])

healthTextBox = Text(root,height=box_height,width=box_width)#this line and the following create the health title and value
healthTextBox.insert(INSERT,"health")
healthTextBox.bindtags((str(text_stat_temp), str(root), "all"))
healthTextBox.place(x=(+20)*screen_x_scale,y=(110+440)*screen_y_scale)
healthComboBox = Combobox(root,state='readonly',values=health_values_name,height=box_height,width=8)
healthComboBox.place(x=(35+box_width*6)*screen_x_scale,y=(110+440)*screen_y_scale)
healthComboBox.bind("<<ComboboxSelected>>", lambda event,i=i: update_value_health(i,event.widget.get()))
healthComboBox.set(health_values_name[health_value])

results = Label(root, text='Results')
results.place(x=700*screen_x_scale,y=245*screen_y_scale)

diceOut = Label(root, text='Raw Dice Here')
diceOut.place(x=700*screen_x_scale,y=265*screen_y_scale)

diceCount = Label(root, text='Total Dice')
diceCount.place(x=700*screen_x_scale,y=290*screen_y_scale)

dcLabel = Text(root,height=box_height,width=box_width)
dcLabel.insert(INSERT,"Roll DC")
dcLabel.bindtags((str(text_stat_temp), str(root), "all"))
dcLabel.place(x=700*screen_x_scale,y=20*screen_y_scale)
dcComboBox = Combobox(root,state='readonly',values=[0,1,2,3,4,5,6,7,8,9,10],height=box_height,width=1)
dcComboBox.place(x=770*screen_x_scale,y=20*screen_y_scale)
dcComboBox.bind("<<ComboboxSelected>>", lambda event,i=i: update_value_DC(i,event.widget.get()))
dcComboBox.set(0)

Checkbutton(root, text='mastery', variable=mastery, onvalue=1, offvalue=0).place(x=700*screen_x_scale,y=70*screen_y_scale)

rollButton=Button(root, height=1, width=6, text="Roll", command=lambda: roll_my_dice())
rollButton.place(x=820*screen_x_scale,y=20*screen_y_scale)

clearButton=Button(root, height=1, width=6, text="Clear", command=lambda: clear_values())
clearButton.place(x=820*screen_x_scale,y=50*screen_y_scale)

predictButton=Button(root, height=1, width=6, text="Prediction", command=lambda: predict_my_dice())
predictButton.place(x=910*screen_x_scale,y=20*screen_y_scale)

predictFeild = Label(root, text='Pridiction')
predictFeild.place(x=700*screen_x_scale,y=310*screen_y_scale)

#allows the user to select between initive or using the DC and Radiobuttons
typeLabel = Text(root,height=box_height,width=box_width*2+5)
typeLabel.insert(INSERT,"Select between preset or input")
typeLabel.bindtags((str(text_stat_temp), str(root), "all"))
typeLabel.place(x=700*screen_x_scale,y=110*screen_y_scale)
typeBox = Combobox(root,state='readonly',values=["Initive","select relevent attributes"],height=box_height,width=5)
typeBox.place(x=700*screen_x_scale,y=125*screen_y_scale)

def only_numbers(char): # used for the validation of 
    return char.isdigit()
validation = root.register(only_numbers)

modLabelCount = Text(root,height=box_height,width=box_width*2+12)
modLabelCount.insert(INSERT,"Add any other dice count modifiers")
modLabelCount.bindtags((str(text_stat_temp), str(root), "all"))
modLabelCount.place(x=700*screen_x_scale,y=160*screen_y_scale)
modInputCount = Entry(root,width=5,validate="key", validatecommand=(validation, '%S'))
modInputCount.insert(INSERT,"0")
modInputCount.place(x=700*screen_x_scale,y=180*screen_y_scale)
modLabelValue = Text(root,height=box_height,width=box_width*2+12)
modLabelValue.insert(INSERT,"Add any number of additional successes")
modLabelValue.bindtags((str(text_stat_temp), str(root), "all"))
modLabelValue.place(x=700*screen_x_scale,y=205*screen_y_scale)
modInputValue = Entry(root,width=5,validate="key", validatecommand=(validation, '%S'))
modInputValue.insert(INSERT,"0")
modInputValue.place(x=700*screen_x_scale,y=225*screen_y_scale)


mainloop()
