from tkinter import *
import time
def move_widget(item, x, y):
    ### Moves a widget(item) on the main canvas to the new coordinates(x,y)###
    main_canvas.coords(tractor1,x,y)
    main_canvas.update()
root = Tk()
icon = Image("photo", file="tractor_image.png")
root.tk.call('wm','iconphoto',root._w,icon)
main_canvas = Canvas(width =600, height = 400, bg='white')
main_canvas.pack(expand = YES, fill = BOTH)
tractor_img = PhotoImage(file="tractor_image.png")
tractor1 = main_canvas.create_image(0,0,image=tractor_img, anchor = NW)
t1,t2= main_canvas.coords(tractor1)
print(t1,t2)
for i in range(0,600,1):
    move_widget(tractor1, t1+i,t2)
    time.sleep(0.01)
mainloop()
