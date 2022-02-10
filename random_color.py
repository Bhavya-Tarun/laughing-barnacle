from tkinter import*
import random
root=Tk()
root.title("Dictionary")
root.geometry("600x400")

dictionary = {"color": ["maroon1","lawn green","magenta2",
                        "purple1","springgreen2","chocolate1", 
                        "deep pink","cyan"]}

def change():
    random_no=random.randint(0, 7)
    print(dictionary["color"][random_no])
    root.configure(background=dictionary["color"][random_no])
    
btn= Button(root, text="Change into random color", command=change)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()