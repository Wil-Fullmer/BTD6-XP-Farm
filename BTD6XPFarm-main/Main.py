#Packages
import pyautogui as pg
import time
import keyboard as kb

#get mouse post for cords

'''
pg.position()
print(pg.position())
'''


#First We must note the postitions of the key Items inside of btd6
'''
    | Entity Spaces |
Menu Play: Point(x=830, y=919)
Expert Button: Point(x=1338, y=961)
Infernal: Point(x=484, y=570)
Easy: Point(x=600, y=407)
Deflation Mode: Point(x=1293, y=473)
Ok Button: Point(x=1020, y=750)
Rock 1: Point(x=803, y=367)
Rock 2: Point(x=807, y=715)
Sub Position: Point(x=1711, y=455)
Wizard Position: Point(x=1721, y=850)
Puddle Postion 1: Point(x=1199, y=239)
Puddle Postion 2: Point(x=477, y=842)
Next Button: Point(x=948, y=915)
Home Button: Point(x=700, y=856)
'''


# Navigates the menu into the game
def Menu_Navigate():
    time.sleep(5)#tab in time
    pg.click(x=830, y=919)
    time.sleep(.5)
    pg.click(x=1338, y=961)
    time.sleep(.5)
    pg.click(x=484, y=570)
    time.sleep(.5)
    pg.click(x=600, y=407)
    time.sleep(.5)
    pg.click(x=1293, y=473)
    time.sleep(4)
    pg.click(x=1020, y=750)

# Monkey Sub Upgrades\
def subUpgrades():
    kb.send(",")
    time.sleep(.1)
    kb.send(",")
    time.sleep(.1)
    kb.send("/")
    time.sleep(.1)
    kb.send("/")
    time.sleep(.1)
    kb.send("/")
    time.sleep(.1)
    kb.send("/")

# Monkey sub 1 placement
def subOne():
    kb.send("x")
    pg.click(x=1199, y=239)
    time.sleep(0.5)
    pg.click(x=1199, y=239)
    pg.click(x=1199, y=239)

    subUpgrades()
# Monkey sub 2 placement
def subTwo():
    kb.send("x")
    pg.click(x=477, y=842)
    time.sleep(0.5)
    pg.click(x=477, y=842)
    pg.click(x=477, y=842)
    subUpgrades()

#Monkey Wizard UPgrades
def WizUPgrades():
    kb.send(".")
    time.sleep(.1)
    kb.send(".")
    time.sleep(.1)
    kb.send(".")
    time.sleep(.1)
    kb.send("/")
    time.sleep(.1)
    kb.send("/")

#Monkey Wizard 1 Placement
def wizOne():
    kb.send("A")
    pg.click(x=803, y=367)
    time.sleep(.5)
    pg.click(x=803, y=367)
    pg.click(x=803, y=367)
    WizUPgrades()

#Monkey Wizard 2 Placement
def wizTwo():
    kb.send("A")
    pg.click(x=807, y=715)
    time.sleep(.5)
    pg.click(x=807, y=715)
    pg.click(x=807, y=715)
    WizUPgrades()

# Monkey placement
def Monkey_Placement():
    time.sleep(3)
    subOne()
    subTwo()
    wizOne()
    wizTwo()
    kb.send("space")
    time.sleep(0.1)
    kb.send("space")

#Monkey Menu Outro
def monkeyOutro():
    pg.click(x=948, y=915)
    time.sleep(1)
    pg.click(x=700, y=856)
    time.sleep(1)# this was originally 2

#Run Script
def scriptRun():
    Menu_Navigate()
    Monkey_Placement()
    time.sleep(370) #dived by clicks wanted = 370 to accept lvl up
    monkeyOutro()
# RUN SCRIPT
'''
---- GOTO GUI RENDER ----

for i in range(1000):
    scriptRun()
'''

'''
----GUI RENDER----
'''

# Dependencies and GUI Rendering
from tkinter import *

root = Tk()

root.iconbitmap('C:/Users/kakvl/PycharmProjects/BTD6XPFarm/Icon.ico')
root.title('BTD6 Farm V1')
root.geometry("300x200")
root.resizable(width=False,height=False)
root.config(bg = '#2c626c')

#storing data
def number():
    try:
       int(my_box.get())
       storage = int(my_box.get())


       # Running Script GUI
       def Execute_Script_Gui():
           # destorys original session
           root.destroy()

           # creates new session
           root2 = Tk()
           icon = PhotoImage(file='Icon.ico')
           root2.tk.call('wm', 'iconphoto', root2._w, icon)
           root2.title('Running...')
           root2.geometry("430x180")
           root2.resizable(width=False, height=False)
           root2.config(bg='#2c626c')
           my_label2 = Label(
               root2,
               text='Please Press Run Script.. \n \n '
                    'Then Tab Into BTD6\n \n'
                    'The Script Will Close \n Automatically When Complete',
               font=('Terminal', 13),
               padx=10,
               pady=10,
               bg='#2c626c',
               fg='#f9f7f6'
           )
           my_label2.pack(pady=5)

           def Run():
            for i in range(storage):
               scriptRun()
            root2.destroy()

           my_button2 = Button(
               root2,
               text="Run Script",
               font=('Terminal', 12),
               command=Run,


           )
           my_button2.pack(pady=5)


           mainloop()



       # Runs Script
       Execute_Script_Gui()






    except ValueError:
        answer.config(text = "Please Enter a Number", fg = '#f9f7f6',font = ('Terminal', 10))






# Creating Items
my_label = Label(
    root,
    text = 'Enter The Number of Times \nYou Wish to Run the Script',
    font = ('Terminal', 16),
    padx = 10,
    pady = 10,
    bg='#2c626c',
    fg = '#f9f7f6',
)
my_label.pack(expand=True)

my_box = Entry(
    root,
    font = ('Terminal', 13,)
)
my_box.pack(pady=20)

my_button = Button(
    root,
    text="Continue",
    font = ('Terminal', 12),
    command=number,
)
my_button.pack(pady=5)


answer = Label(root, text='', bg='#2c626c')
answer.pack(pady=5)

root.mainloop()


