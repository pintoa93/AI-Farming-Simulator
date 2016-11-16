from tkinter import *
def add_cabbage_field(x,y, l, w,item):
    """ Top left conner of the farm is at coordinates (x,y)
        Creates a farm with the width of 'w' and length of 'l'
        l and w has to be in multiples of 10 """
    global existing_farms
    existing_farms = []
    for i in range(x,l+x,10):
        for k in range(y,w+y,10):
            main_canvas.create_image(i,k,image=item, anchor = NW)
    existing_farms.append([x,y,x+l,y+w])
    print(existing_farms)
root = Tk()
main_canvas = Canvas(width =600, height = 400, bg='white') #create canvas
main_canvas.pack(expand = YES, fill = BOTH)
cabbage_texture = PhotoImage(file="textures/cabbage.gif")
add_cabbage_field(10,0,110,100,cabbage_texture)
add_cabbage_field(100,200,110,210,cabbage_texture)
