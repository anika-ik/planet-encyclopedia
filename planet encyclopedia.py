from tkinter import *
root= Tk()
root.title("planet encyclopedia")
root.geometry("500x500")
root.configure(background= "lightblue")

label_planet= Label(root, text= "Planet: ", font=(20), bg="blue", fg= "white")
label_planetname= Label(root, font=("courier", 18, "bold"), bg="blue", fg= "white")
label_planetimage= Label(root, bg="gold2", highlightthickness= 5, borderwidth=2, relief= SOLID)
label_gravity_radius= Label(root, font=("castellar"), bg= "red")
label_info= Label(root, font=("courier", 10, "bold"), bg= "lightgrey", wraplength= 500)

def planetinfo():
    print("hey")
    
btn= Button(root, text= "show planet info", command= planetinfo)
btn.place(relx= 0.5, rely= 0.2, anchor= CENTER)

label_planet.place(relx= 0.2, rely= 0.1, anchor= CENTER)
label_planetname.place(relx= 0.5, rely=0.3, anchor= CENTER)
label_planetimage.place(relx= 0.5, rely= 0.5, anchor= CENTER)
label_gravity_radius.place(relx= 0.5, rely= 0.8, anchor= CENTER)
label_info.place(relx=0.5, rely=0.9, anchor= CENTER)

root.mainloop()