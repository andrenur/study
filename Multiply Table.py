# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *

def showTable():
   n = entry.get()
   two = int(n) * 2
   three= int(n)*3
   four= int(n)*4
   five= int(n)*5
   six= int(n)*6
   seven= int(n)*7
   eight= int(n)*8
   nine= int(n)*9
   ten= int(n)*10
   labelText1.set(n + ' x ' + '1 = ' + n)
   labelText2.set(n + ' x ' + '2 = ' + str(two))
   labelText3.set(n + ' x ' + '3 = ' + str(three))
   labelText4.set(n + ' x ' + '4 = ' + str(four))
   labelText5.set(n + ' x ' + '5 = ' + str(five))
   labelText6.set(n + ' x ' + '6 = ' + str(six))
   labelText7.set(n + ' x ' + '7 = ' + str(seven))
   labelText8.set(n + ' x ' + '8 = ' + str(eight))
   labelText9.set(n + ' x ' + '9 = ' + str(nine))
   labelText10.set(n + ' x ' + '10 = ' + str(ten))


root = Tk()
root.title('Multiply Table')

entry = Entry(root)
entry.pack()

Button(root, text= 'Show Table', command = showTable).pack()

labelText1 = StringVar()
labelText1.set('-------')
Label(root, textvariable = labelText1, bg = 'red').pack()

labelText2 = StringVar()
labelText2.set('-------')
Label(root, textvariable = labelText2, bg = 'green').pack()

labelText3 = StringVar()
labelText3.set('-------')
Label(root, textvariable = labelText3, bg = 'blue').pack()

labelText4 = StringVar()
labelText4.set('-------')
Label(root, textvariable = labelText4, bg = 'yellow').pack()

labelText5 = StringVar()
labelText5.set('-------')
Label(root, textvariable = labelText5, bg = 'orange').pack()

labelText6 = StringVar()
labelText6.set('-------')
Label(root, textvariable = labelText6, bg = 'white').pack()

labelText7 = StringVar()
labelText7.set('-------')
Label(root, textvariable = labelText7, bg = 'gray').pack()

labelText8 = StringVar()
labelText8.set('-------')
Label(root, textvariable = labelText8, bg = 'purple').pack()

labelText9 = StringVar()
labelText9.set('-------')
Label(root, textvariable = labelText9, bg = 'pink').pack()

labelText10 = StringVar()
labelText10.set('-------')
Label(root, textvariable = labelText10, bg = 'tan').pack()


root.mainloop()