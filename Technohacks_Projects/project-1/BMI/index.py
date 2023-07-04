import tkinter  as tk
from tkinter import ttk
from PIL import Image,ImageTk

win=tk.Tk()
win.title("BMI Calculator")
win.geometry("470x580+300+200")
win.resizable(0,0)
win.configure(bg="#f0f1f5")
def BMI():
    h=float(Height.get())
    w=float(Weight.get())

    m=h/100
    bmi=round(float(w/m**2),1)
    print(bmi)
    lable1.config(text=bmi)

    if bmi<=20:
        lable2.config(text="Underweight")
        lable3.config(text="You have lower weight then normal human!")
    elif bmi >20 and bmi<=25:
        lable2.config(text="Normal")
        lable3.config(text="It indicate you are health!")
    elif bmi>25 and bmi<=30:
        lable2.config(text="OverWeight")
        lable3.config(text="It indicates that a person is \n slighty overweight!\n A  doctor may adivise to lose some \n weight for health reason!")
    else :
        lable2.config(text="Obes")
        lable3.config(text="Health may be at risk ,if they do not \n lose weight!")

#icon
image_icon=tk.PhotoImage(file="Images/icon.png")
win.iconphoto(False,image_icon)
#top
top=tk.PhotoImage(file="Images/top.png")
top_image=tk.Label(win,image=top,background='#f0f1f5')
top_image.place(x=-10,y=-10)

#bottom box
tk.Label(win,width=72,height=18,bg='lightblue').pack(side="bottom")

#two boxes
box=tk.PhotoImage(file="Images/box.png")
tk.Label(win,image=box).place(x=20,y=100)
tk.Label(win,image=box).place(x=240,y=100)

#scale
scale=tk.PhotoImage(file="Images/scale.png")
tk.Label(win,image=scale,bg="lightblue").place(x=0,y=310)

############# silder1 #############
current_val=tk.DoubleVar()
def get_current_value():
    return f" {current_val.get() :.1f}"
def silder_changed(event):
    Height.set(get_current_value())
    size=int(float(get_current_value()))
    img=(Image.open("Images/man.png"))
    resized_image=img.resize((50,10+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70,y=550-size)
    secondimage.image=photo2


style=ttk.Style()
style.configure("TScale",background="white")

silder=ttk.Scale(win,from_=0,to=220,orient='horizontal',style="TScale",command=silder_changed,variable=current_val)
silder.place(x=80,y=250)
################################

#@@@@@@@@@@@@@@ silder2 @@@@@@@@@@@@@@

current_val2=tk.DoubleVar()
def get_current_value2():
    return f" {current_val2.get():.2f}"
def silder_changed2(event):
    Weight.set(get_current_value2())

style2=ttk.Style()
style2.configure("TScale",background="white")

silder2=ttk.Scale(win,from_=0,to=200,orient='horizontal',style="TScale",command=silder_changed2,variable=current_val2)
silder2.place(x=300,y=250)

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#Entry box
Height=tk.StringVar(value="0.0")
Weight=tk.StringVar(value="0.0")
height=tk.Entry(win,textvariable=Height,width=5,bg="#fff",fg="#000",font="arial 50",bd=0,justify="center")
height.place(x=35,y=160)


weight=tk.Entry(win,textvariable=Weight,width=5,bg="#fff",fg="#000",font="arial 50",bd=0,justify="center")
weight.place(x=255,y=160)




#man image
secondimage=tk.Label(win,bg="lightblue")
secondimage.place(x=70,y=530)

tk.Button(win,text="View Report",width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=BMI).place(x=280,y=340)

lable1=tk.Label(win,font="arial 60 bold", bg="lightblue",fg="#fff")
lable1.place(x=125,y=305)


lable2=tk.Label(win,font="arial 20 bold", bg="lightblue",fg="#3b3a3a")
lable2.place(x=280,y=430)


lable3=tk.Label(win,font="arial 10 ", bg="lightblue")
lable3.place(x=200,y=500)


win.mainloop()