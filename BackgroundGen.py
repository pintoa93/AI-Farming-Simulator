from tkinter import *
root = Tk()
root.title("Cabbage_patch_sim")
root.geometry("600x600")
root.configure(background="black")

background_image = PhotoImage(file="background.gif")

background = Label (root, image= background_image, bd=0)
background.pack()
