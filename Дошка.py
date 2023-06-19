from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import *
import tkinter as tk
import os

root = Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.config(bg = "#f2f3f5")
root.resizable(False, False)




current_x = 0
current_y = 0
img_x = 0
img_y = 0
i_w = 1
i_h = 1
color = "black"
def locale_xy(work):
     global current_x, current_y
     current_x = work.x
     current_y = work.y
def addline(work):
    global current_x, current_y
    canv.create_line((current_x,current_y,work.x,work.y), width=get_current_value(), fill=color, capstyle=ROUND, smooth=True)
    current_x, current_y = work.x, work.y
def show_color(new_color):
    global color
    color=new_color

def new_canvas():
    canv.delete("all")
    display_pallet()


def insertimg ():
    
    global f_img, filename,img_x, img_y, i_w, i_h
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetype=(("PNG file", "*.png"),("All file", "new.txt")))
    
    f_img = PhotoImage(file=filename)
    f_img = f_img.subsample(i_w, i_h)
    my_img = canv.create_image(180,50, image=f_img)
    
    img_x, img_y = 180,50
    img_resizer.place(x=230, y=530)
    img_value_label.place(x=227, y=555)
    root.bind('<B3-Motion>', my_callback)
    

def my_callback (event):
    global f_img, img_x, img_y, img_y, i_w, i_h
    
    f_img = PhotoImage(file=filename)
    f_img = f_img.subsample(i_w, i_h)
    my_img = canv.create_image(event.x,event.y, image=f_img)
    img_x, img_y = event.x,event.y
def my_img_resize (size):
    global f_img, img_y, i_w, i_h
    
    #print(int(round(get_img_size_value(),0)))
    s = round(float(size))
    i_w = s
    i_h = s
    f_img = PhotoImage(file=filename)
    
    f_img = f_img.subsample(i_w,i_h)
    my_img = canv.create_image( img_x, img_y, image=f_img)


#icon
img_icon = PhotoImage(file="logo.png")
root.iconphoto(False, img_icon)

#sidebar
color_box = PhotoImage(file="color section.png")
Label(root, image=color_box, bg = "#f2f3f5").place(x=10, y=20)


eraser = PhotoImage(file="eraser.png")
Button(root, image=eraser, bg = "#f2f3f5", command=new_canvas).place(x=30, y=400)

import_img = PhotoImage(file="addimage.png")
Button(root, image=import_img, bg = "#f2f3f5", command = insertimg).place(x=30, y=450)

colors = Canvas(root, bg = "#fff", width=37, height = 300, bd=0)
colors.place(x=30, y=60)

def display_pallet():
    id = colors.create_rectangle((10,10,30,30), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))
    
    id = colors.create_rectangle((10,40,30,60), fill="gray")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))
    
    id = colors.create_rectangle((10,70,30,90), fill="brown4")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))
    
    id = colors.create_rectangle((10,100,30,120), fill="red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))
    
    id = colors.create_rectangle((10,130,30,150), fill="orange")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))
    
    id = colors.create_rectangle((10,160,30,180), fill="yellow")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))
    
    id = colors.create_rectangle((10,190,30,210), fill="green")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))
    
    id = colors.create_rectangle((10,220,30,240), fill="blue")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))
    
    id = colors.create_rectangle((10,250,30,270), fill="purple")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))



display_pallet()

#main screen
canv = Canvas(root, bg = "white", width=930, height = 500, cursor="hand2")
canv.place(x=100, y=10)

canv.bind('<Button-1>', locale_xy)
canv.bind('<B1-Motion>', addline)


#Slider
current_value = tk.DoubleVar()
current_value.set(10)
img_size_value = tk.DoubleVar()
img_size_value.set(2)

def get_current_value():
    return "{: .2f}".format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())
    
def get_img_size_value():
    return "{}".format(round(img_size_value.get()))

def img_size_changed(event):
    img_value_label.configure(text=get_img_size_value())
    
    my_img_resize(get_img_size_value())

slider = ttk.Scale(root, from_ = 0, to = 100, orient = "horizontal", command = slider_changed, variable=current_value)
slider.place(x=30, y=530)
value_label = ttk.Label(root, text = get_current_value())
value_label.place(x=27, y=555)

img_resizer = ttk.Scale(root, from_ = 5, to = 1, orient = "horizontal", command = img_size_changed, variable=img_size_value)
img_value_label = ttk.Label(root, text = get_img_size_value())




root.mainloop()