from tkinter import *
root = Tk()
img = Image("photo", file="tractor_image.png")
root.tk.call('wm','iconphoto',root._w,img)
main_canvas = Canvas(width =1000, height = 800, bg='white')
main_canvas.pack(expand = YES, fill = BOTH)
tractor_pic = PhotoImage(file="tractor_image.png")
main_canvas.create_image(500,400,image=tractor_pic, anchor = NW)
mainloop()
