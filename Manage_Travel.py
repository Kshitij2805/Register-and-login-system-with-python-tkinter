from tkinter import*
from PIL import ImageTk


class Manage_Travel:
     def __init__(self,root):
         self.root=root
         self.root.title("Manage")
         self.root.geometry("1350x700+0+0")
         self.root.config(bg="#01032E")

         self.root.bg_icon = ImageTk.PhotoImage(file=r"images\blue1.jpg")
         self.root.bg_lbl = Label(self.root, image=self.root.bg_icon,bg='#01032E',bd=0)
         self.root.bg_lbl.pack()

      #   self.title=Label(self.root,text='Mange',font=("time new roman", 20, "bold"), bg="red", fg="white").pack()


root=Tk()
obj=Manage_Travel(root)
root.mainloop()