from tkinter import *
import random
from tkinter.ttk import Combobox

root=Tk()
root.title("WOD 1st edition character sheet")
screen_x_scale = int(root.winfo_screenwidth()/1512)
screen_y_scale = int(root.winfo_screenheight()/982)
box_width = 12*screen_x_scale
box_height = 1*screen_y_scale
root.geometry(str(int(700*screen_x_scale))+"x"+str(int(900*screen_y_scale)))

attribute_names = [["Strength","Dexterity","Stamina"],["Charisma","Manipulation","Appearance"],
                   ["Perception","Intelligence","Wits"]]#this stores the name of each attrubtue to popuplate the UI
attribute_values = [[0,0,0],[0,0,0],[0,0,0]]#this stores the value of each attrubtue for later use
for i in range(3):#this loop creates the attribute names and feilds
    for j in range(3):
        text_stat_temp = Text(root,height=box_height,width=box_width)#this line and the following create the attribute titles and values
        text_stat_temp.insert(INSERT,attribute_names[i][j])
        text_stat_temp.bindtags((str(text_stat_temp), str(root), "all"))
        text_stat_temp.place(x=(i*230+20)*screen_x_scale,y=(j*30+50)*screen_y_scale)
        comboboxT = Combobox(root,state='readonly',values=[0,1,2,3,4,5],height=box_height,width=1)
        comboboxT.place(x=(i*230+30+box_width*5)*screen_x_scale,y=(j*30+50)*screen_y_scale)

mainloop()