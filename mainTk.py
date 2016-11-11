from tkinter import *
from random import randint
import time
def move_widget(item, x, y):
    """Moves a widget(item) on the main canvas to the new coordinates(x,y)"""
    main_canvas.coords(item,x,y)
    main_canvas.update()
def plough_field(x,y, l, w):
    """ Top left conner of the farm is at coordinates (x,y)
        Creates a farm with the width of 'w' and length of 'l'
        l and w has to be in multiples of 10 """
    global ploughed_texture
    ploughed_texture = PhotoImage(file="textures/dirt.png")
    for i in range(x,l+x,10):
        for k in range(y,w+y,10):
            main_canvas.create_image(i,k,image=ploughed_texture, anchor = NW)
root = Tk()
icon = Image("photo", file="textures/tractor.png")  
root.tk.call('wm','iconphoto',root._w,icon) #Changes the application icon
main_canvas = Canvas(width =600, height = 400, bg='white') 
main_canvas.pack(expand = YES, fill = BOTH)
bck_img = PhotoImage(file="textures/background.gif") 
main_canvas.create_image(0,0,image=bck_img,anchor=NW) # Sets background of the window to grass 
tractor_img = PhotoImage(file="textures/tractor.png")
x=int(main_canvas['width'])
y=int(main_canvas['height'])
tractor1 = main_canvas.create_image(x/2,y/2,image=tractor_img, anchor = NW) 
t1,t2= main_canvas.coords(tractor1)
print(t1,t2)
rh= randint(8,12)
rw = randint(10,14)
print(rw)
plough_field(300,220,int(rw*10),int(rh*10))
mainloop()
