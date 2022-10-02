from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("RAHDI")
root.iconbitmap('tkin.png')

my_img1 = ImageTk.PhotoImage(Image.open('images/s1.png'))
my_img2 = ImageTk.PhotoImage(Image.open('images/s2.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/s3.png'))
my_list = [my_img1, my_img2, my_img3]

status = Label(root, text='1 of ' + str(len(my_list)), bd=1, anchor=E, relief=SUNKEN)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(num):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image=my_list[num-1])

    button_forward = Button(root, text='>>', command = lambda: forward(num + 1))
    button_back = Button(root, text='<<', command=lambda: back(num-1))

    if num == 3:
        button_forward = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    status = Label(root, text=f'Image {num} of ' + str(len(my_list)), bd=1, anchor=E, relief=SUNKEN)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(num):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image=my_list[num-1])

    button_forward = Button(root, text='>>', command = lambda: forward(num + 1))
    button_back = Button(root, text='<<', command=lambda: back(num-1))

    if num == 1:
        button_back = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    
    status = Label(root, text=f'Image {num} of ' + str(len(my_list)), bd=1, anchor=E, relief=SUNKEN)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text='<<', command=back, state=DISABLED)
button_quit = Button(root, text='close', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()