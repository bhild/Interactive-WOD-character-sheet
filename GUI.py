from tkinter import *
import random
from tkinter.ttk import Combobox
from operator import itemgetter

def update_value_attribute(a,b,n):
    attribute_values[a][b] = int(n)
def update_value_ablity(a,b,n):
    abilities_values[a][b] = int(n)
def update_value_virtue(a,n):
    ten_point_values_max[a] = int(n)
def update_value_10s(a,n,comboboxM):
    if int(n) > ten_point_values_max[a]:
         ten_point_values[a] = ten_point_values_max[a]
    else:
         ten_point_values[a] = int(n)
    
    comboboxM.set(ten_point_values[a])
def update_value_10s_MAX(a,n):
    ten_point_values_max[a] = int(n)
def update_value_health(a,n):
    health_value = health_values_name.index(n)

root=Tk()
root.title("WOD 1st edition character sheet (Hunter)")
screen_x_scale = int(root.winfo_screenwidth()/1512)
screen_y_scale = int(root.winfo_screenheight()/982)
box_width = 13*screen_x_scale
box_height = 1*screen_y_scale
root.geometry(str(int(1000*screen_x_scale))+"x"+str(int(900*screen_y_scale)))

attribute_names = [["Strength","Dexterity","Stamina"],["Charisma","Manipulation","Appearance"],
                   ["Perception","Intelligence","Wits"]]#this stores the name of each attrubtue to popuplate the UI
attribute_values = [[0,0,0],[0,0,0],[0,0,0]]#this stores the value of each attrubtue for later use
for i in range(3):#this loop creates the attribute names and feilds
    for j in range(3):

        text_stat_temp = Text(root,height=box_height,width=box_width)#this line and the following create the attribute titles and values
        text_stat_temp.insert(INSERT,attribute_names[i][j])
        text_stat_temp.bindtags((str(text_stat_temp), str(root), "all"))
        text_stat_temp.place(x=(i*230+20)*screen_x_scale,y=(j*30+50)*screen_y_scale)
        comboboxT = Combobox(root,state='readonly',values=[0,1,2,3,4,5],height=box_height,width=1,exportselection=0)
        comboboxT.place(x=(i*230+35+box_width*6)*screen_x_scale,y=(j*30+50)*screen_y_scale)
        comboboxT.bind("<<ComboboxSelected>>", lambda event,i=i,j=j: update_value_attribute(i,j,event.widget.get()))
        comboboxT.set(0)
abilities_names = [["Acting","Alertness","Athletics","Brawl","Doge","Empathy","Intimidation","Leadership","Streetwise","Subtrafuge"]#talents
                   ,["Animal Ken","Drivfe","Etiquette","Firearms","Melle","Music","Repair","Security","Stelth","Surival"]#Skills
                   ,["Bureaucracy","Computer","Finance","Investigation","Law","Linguistics","Medicine","Occult","Pilitics","Science"]#knowlages
                   ]#this stores the name of each abilities to popuplate the UI
abilities_values = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]#this stores the value of each abilities for later use

for i in range(3):#this loop creates the attribute names and feilds
    for j in range(10):
        text_stat_temp = Text(root,height=box_height,width=box_width)#this line and the following create the attribute titles and values
        text_stat_temp.insert(INSERT,abilities_names[i][j])
        text_stat_temp.bindtags((str(text_stat_temp), str(root), "all"))
        text_stat_temp.place(x=(i*230+20)*screen_x_scale,y=(j*30+50+120)*screen_y_scale)
        comboboxT = Combobox(root,state='readonly',values=[0,1,2,3,4,5],height=box_height,width=1)
        comboboxT.place(x=(i*230+35+box_width*6)*screen_x_scale,y=(j*30+50+120)*screen_y_scale)
        comboboxT.bind("<<ComboboxSelected>>", lambda event,i=i,j=j: update_value_ablity(i,j,event.widget.get()))
        comboboxT.set(0)
virtue_names = ["Conscience","Self-Control","Courage"]
virtue_values = [0,0,0]
ten_point_names = ["Humanity","Willpower","Faith"]
ten_point_values = [0,0,0]
ten_point_values_max = [0,0,0]
health_values_name = ["Healthy","Bruised","Hurt","Injured","Wounded","Mauled","Crippled","Incapacitated"]
health_value = 0
for i in range(3):
        text_stat_temp = Text(root,height=box_height,width=box_width)#this line and the following create the virtue titles and values
        text_stat_temp.insert(INSERT,virtue_names[i])
        text_stat_temp.bindtags((str(text_stat_temp), str(root), "all"))
        text_stat_temp.place(x=(i*230+20)*screen_x_scale,y=(50+440)*screen_y_scale)
        comboboxT = Combobox(root,state='readonly',values=[0,1,2,3,4,5],height=box_height,width=1)
        comboboxT.place(x=(i*230+35+box_width*6)*screen_x_scale,y=(50+440)*screen_y_scale)
        comboboxT.bind("<<ComboboxSelected>>", lambda event,i=i: update_value_virtue(i,event.widget.get()))
        comboboxT.set(0)
for i in range(3):
        text_stat_temp = Text(root,height=box_height,width=box_width)#this line and the following create the virtue titles and values
        text_stat_temp.insert(INSERT,ten_point_names[i])
        text_stat_temp.bindtags((str(text_stat_temp), str(root), "all"))
        text_stat_temp.place(x=(i*230+20)*screen_x_scale,y=(80+440)*screen_y_scale)
        comboboxT = Combobox(root,state='readonly',values=[0,1,2,3,4,5,6,7,8,9,10],height=box_height,width=1)
        comboboxT.place(x=(i*230+35+box_width*6)*screen_x_scale,y=(80+440)*screen_y_scale)
        comboboxM = Combobox(root,state='readonly',values=[0,1,2,3,4,5,6,7,8,9,10],height=box_height,width=1)
        comboboxM.place(x=(i*230+70+box_width*6)*screen_x_scale,y=(80+440)*screen_y_scale)
        comboboxT.bind("<<ComboboxSelected>>", lambda event,i=i: update_value_10s_MAX(i,event.widget.get()))
        comboboxM.bind("<<ComboboxSelected>>", lambda event,i=i,comboboxM=comboboxM: update_value_10s(i,event.widget.get(),comboboxM))
        comboboxT.set(0)
healthTextBox = Text(root,height=box_height,width=box_width)#this line and the following create the virtue titles and values
healthTextBox.insert(INSERT,"health")
healthTextBox.bindtags((str(text_stat_temp), str(root), "all"))
healthTextBox.place(x=(+20)*screen_x_scale,y=(110+440)*screen_y_scale)
healthComboBox = Combobox(root,state='readonly',values=health_values_name,height=box_height,width=8)
healthComboBox.place(x=(35+box_width*6)*screen_x_scale,y=(110+440)*screen_y_scale)
healthComboBox.bind("<<ComboboxSelected>>", lambda event,i=i: update_value_health(i,event.widget.get()))
healthComboBox.set(health_values_name[0])
mainloop()
