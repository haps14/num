# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:05:46 2021

@author: Lenovo
"""
from tkinter import*

root = Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background = "silver")

  
bag = ["chocolate" , "juice" , "dress" , "money" , "medical kit" , "wallet" , "phone"]
random_number_sorted_list = Label(root)
bag_things = Label(root)
bag_things["text"] = " things : " + str(bag)

def randomlist() :
    randomlist = random.sample(range(1,7),1)
  
    randomlist.sort()
    random_number_sorted_list["text"] = "put the item :" + str(randomlist) + "th in bag"
    
    btn = Button(root , text = "Say what to put in thee bag", command=randomlist)
    btn.place(relx = 0.5, rely = 0.4 , anchor = CENTER)
    
    bag_things.place(relx = 0.5, rely = 0.5 , anchor = CENTER)
    random_number_sorted_list.place(relx=0.5 , rely=0.6 , anchor = CENTER)
    
    root.mainloop()