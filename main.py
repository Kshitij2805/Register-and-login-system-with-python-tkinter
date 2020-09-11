from tkinter import*
from PIL import ImageTk
import about
import Registration
import login

class Home(object):
     def __init__(self,root):
         self.root=root

         self.bg_icon = ImageTk.PhotoImage(file="images\home.jpg")
         bg_lbl = Label(self.root, image=self.bg_icon,bg="black",state=DISABLED).pack()

         btn = Button(self.root, text="    Login", bg="lightblue",activebackground="lightblue", cursor="hand2",font=("time new roman", 15, "bold"),command=self.enter)
         btn.place(x=560, y=220, width=150, height=42)

         self.home = ImageTk.PhotoImage(file=r"images\sign-up-icon.png")
         home = Label(self.root, image=self.home, bg="lightblue").place(x=565, y=222)

         btn = Button(self.root, text="     Register", bg="lightblue",font=("time new roman", 15, "bold"),activebackground="lightblue", cursor="hand2", command=self.openRegister).place(x=750, y=220,  width=150,heigh=40)
         self.home1 = ImageTk.PhotoImage(file=r"images\reg.png")
         home1 = Label(self.root, image=self.home1, bg="lightblue").place(x=760, y=222)

         self.btn3Icon = PhotoImage(file='icons/info.png')
         self.aboutBtn = Button(self.root, text='    About Us      ', font='arial 12 bold',activebackground="lightblue",bg="lightblue",
                                command=about.main)
         self.aboutBtn.config(image=self.btn3Icon, compound=LEFT)
         self.aboutBtn.place(x=650, y=300)

     def openRegister(self):
         reg = Registration.Register()
         return
     def enter(self):
         lo = login.Login()
         return

def main():
    root = Tk()
    obj = Home(root)
    root.title("Travel and Tourism Mangement system")
    p1 = ImageTk.PhotoImage(file=r'images\beach.png')
    root.iconphoto(False,p1)
    root.geometry("1350x700+0+0")
    root.mainloop()

if __name__ == "__main__":
    main()