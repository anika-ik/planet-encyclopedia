from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root= Tk()
root.title("planet encyclopedia")
root.geometry("500x500")
root.configure(background= "lightblue")

mercury= ImageTk.PhotoImage(Image.open("mercury.jpg"))
venus= ImageTk.PhotoImage(Image.open("venus.jpg"))
earth= ImageTk.PhotoImage(Image.open("earth.jpg"))

label_planet= Label(root, text= "Planet: ", font=(20), bg="blue", fg= "white")
label_planetname= Label(root, font=("courier", 18, "bold"), bg="blue", fg= "white")
label_planetimage= Label(root, bg="gold2", highlightthickness= 5, borderwidth=2, relief= SOLID)
label_gravity_radius= Label(root, font=("castellar"), bg= "red")
label_info= Label(root, font=("courier", 10, "bold"), bg= "lightgrey", wraplength= 500)

planets= ["mercury","venus","earth"]
selectedvalue= StringVar()
dropdown= ttk.Combobox(root, values= planets, textvariable= selectedvalue)

def planetinfo():
    planet= selectedvalue.get()
    if planet == "mercury" :
        label_planetname['text'] = "mercury"
        label_planetimage['image'] = mercury
        label_gravity_radius['text']= "gravity: 3.7 m/s2 \n Radius: 2439.7 km "
        label_info['text']= "mercury is the smallest planet in our solar system. it is just a little bigger than earth's moon"
    elif planet == "venus" :
        label_planetname['text'] = "venus"
        label_planetimage['image'] = venus
        label_gravity_radius['text']= "gravity: 8.87 m/s2 \n Radius: 6051.8 km "
        label_info['text']= "venus is the brightest object in the sky after the sun and the moon and sometimes looks like a bright star in the morning or evening sky"
    elif planet == "earth" :
        label_planetname['text'] = "earth"
        label_planetimage['image'] = earth
        label_gravity_radius['text']= "gravity: 9.807 m/s2 \n Radius: 6371 km "
        label_info['text']= "earth is the only place in the known universe confirmed to host life and its the only one known for sure to have liquid water on its surface"


dropdown.place(relx=0.5, rely=0.1, anchor= CENTER)

btn= Button(root, text= "show planet info", command= planetinfo)
btn.place(relx= 0.5, rely= 0.2, anchor= CENTER)

label_planet.place(relx= 0.2, rely= 0.1, anchor= CENTER)
label_planetname.place(relx= 0.5, rely=0.3, anchor= CENTER)
label_planetimage.place(relx= 0.5, rely= 0.5, anchor= CENTER)
label_gravity_radius.place(relx= 0.5, rely= 0.8, anchor= CENTER)
label_info.place(relx=0.5, rely=0.9, anchor= CENTER)

root.mainloop()