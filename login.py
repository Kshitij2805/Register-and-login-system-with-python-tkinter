from tkinter import*
# from tkinter import  ttk
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk
import Registration
import sqlite3

class Login(Toplevel):
     def __init__(self):
          Toplevel.__init__(self)
          self.title("LOGIN")
          self.geometry("1350x700+0+0")
          p1 = ImageTk.PhotoImage(file=r'images\dw.png')
          self.iconphoto(False, p1)
          self.config(bg="#262626")

          # ======================image=======================
          self.bg_icon = ImageTk.PhotoImage(file="images\see.png")
          bg_lbl = Label(self, image=self.bg_icon,bg="skyblue",bd=0).place(width=1500,height=200)



          self.lp_icon = ImageTk.PhotoImage(file=r"images\unnamed.png")
          lp_lbl = Label(self, image=self.lp_icon,bg="black",bd=0).place(x=100,y=270)


          # ===================register frame==================
          frame1 = Frame(self, bg="white",bd=2,relief=RIDGE)
          frame1.place(x=850, y=210, width=380, height=480)
          self.left = ImageTk.PhotoImage(file=r"images\dw.png")
          left = Label(self, image=self.left,bg="white").place(x=985, y=213)

          title = Label(frame1, text="LOGIN", font=("time new roman", 20, "bold"), bg="black",fg="white").place( x=80, y=105, width=200)


          # ========================entry===================================================
          # =======row1==============
          f_name = Label(frame1, text="username*", font=("time new roman", 15, "bold"), bg="white", fg="grey").place( x=80, y=165)



          self.txt_fname = Entry(frame1, font=("", 15), bg="lightgrey")
          self.txt_fname.place(x=80, y=205)

          # =======row4==============
          self.password = Label(frame1, text="password*", font=("time new roman", 15, "bold"), bg="white", fg="grey").place(x=80, y=245)


          self.txt_password = Entry(frame1,show="*", font=("", 15), bg="lightgrey")
          self.txt_password.place(x=80, y=285)


          self.btn_image = ImageTk.PhotoImage(file=r"images\login.jpg")
          btn = Button(frame1, image=self.btn_image, bg="white", bd=0, cursor="hand2",command=self.enter).place(x=100, y=340, width=190,  height=70)


          self.forgot = Button(frame1, text="Forgot Password?",command=self.forgot_password, font=("time new roman", 12, "bold"), bd=0,activebackground="white",activeforeground="#00759E", cursor="hand2",   bg="white", fg="#00759E").place(x=30, y=410)

          self.has= Label(frame1, text="|", font=("time new roman", 15, "bold"), bg="white",fg="black").place(x=180, y=408)

          self.do = Label(frame1, text="Don't have account?", font=("time new roman", 12), bg="white").place(x=190, y=410)

          self.signup = Button(frame1, text="Signup", font=("time new roman", 13, "bold"), bd=0,activebackground="white", activeforeground="#00759E", cursor="hand2", bg="white",  fg="#00759E", command=self.openRegister).place(x=220, y=430)

          #=====Animation====
          self.india1 = ImageTk.PhotoImage(file=r"images\india1.jpg")
          self.india2 = ImageTk.PhotoImage(file=r"images\india2.jpg")
          self.india3 = ImageTk.PhotoImage(file=r"images\india3.jpg")
          self.india4 = ImageTk.PhotoImage(file=r"images\india4.jpg")
          self.lbl_change_image = Label(self, bg="black")
          self.lbl_change_image.place(x=165, y=286, width=383, height=240)
          self.animation()
     def animation(self):
          self.india=self.india1
          self.india1 = self.india2
          self.india2 = self.india3
          self.india3 = self.india4
          self.india4 =self.india
          self.lbl_change_image.config(image=self.india)
          self.lbl_change_image.after(2000,self.animation)


     def enter(self):
          if  self.txt_fname.get()=="" or self.txt_password.get()=="" :
               messagebox.showerror("Error!","All Feild's are required",parent=self)

          else:
               try:
                    con = sqlite3.connect('database.db')
                    cur = con.cursor()
                    cur.execute(
                         "SELECT * FROM Registration Where f_name==? and p_word==? ",
                         (
                              self.txt_fname.get(),
                              self.txt_password.get()
                         ))
                    row=cur.fetchone()
                    if row==None:
                         messagebox.showerror("Error!", "Invalid Username or password", parent=self)
                    else:
                        messagebox.showinfo("information", "successfully login", parent=self)
                        self.destroy()
                        import Manage_Travel
                        return
                    con.close()
               except Exception as es:
                  messagebox.showerror("Error!", f"Error due to :{str(es)}", parent=self)



     def forgot_password(self):
          if self.txt_fname.get()=="":
               messagebox.showerror("Error!","please enter username",parent=self)
          else:
               try:
                    con = sqlite3.connect('database.db')
                    cur = con.cursor()
                    cur.execute("SELECT * FROM Registration Where f_name==?", (self.txt_fname.get(),))
                    row=cur.fetchone()
                    if row==None:
                         messagebox.showerror("Error!", "Invalid please enter valid username", parent=self)
                    else:
                         con.close()
                         self.root2 = Tk()
                         self.root2.title("Reset Password")
                         self.root2.geometry("500x500+350+110")
                         self.root2.resizable(0, 0)
                         self.root2.config(bg="lightgrey")

                         frame2 = Frame(self.root2, bg="white", bd=2, relief=RIDGE)
                         frame2.place(x=70, y=20, width=350, height=450)

                         title = Label(frame2, text="Change password", font=("time new roman", 18, "bold"), bg="red", fg="white").place(x=66, y=10)


                         question = Label(frame2, text="Questions*", font=("time new roman", 15, "bold"), bg="white",fg="grey").place(x=70, y=80)


                         self.cmb_quest = ttk.Combobox(frame2, font=("", 12), state="readonly", justify=CENTER)
                         self.cmb_quest['value'] = ( "--Select--", "Your pet name", "Your date of birth", "Your nickname")

                         self.cmb_quest.place(x=70, y=120, width=220, height=28)
                         self.cmb_quest.current(0)

                         self.ANS = Label(frame2, text="Answer*", font=("time new roman", 15, "bold"), bg="white",  fg="grey").place(x=70, y=170)


                         self.txt_ANS = Entry(frame2, font=("", 15), bg="lightgrey")
                         self.txt_ANS.place(x=70, y=200)

                         self.Npassword = Label(frame2, text="New Password*", font=("time new roman", 15, "bold"),bg="white", fg="grey").place(x=70, y=240)


                         self.txt_Npassword = Entry(frame2, font=("", 15), bg="lightgrey")
                         self.txt_Npassword.place(x=70, y=280)

                         self.forgot = Button(frame2, text="Reset Password", command=self.forgotp, font=("time new roman", 12, "bold"), bd=2, activebackground="white",   activeforeground="#00759E", cursor="hand2", bg="white", fg="#00759E").place(x=95, y=340)



               except Exception as es:
                  messagebox.showerror("Error!", f"Error due to :{str(es)}", parent=self)





     def forgotp(self):
          if   self.cmb_quest.get() == "--Select--" or self.txt_ANS.get()=="" or self.txt_Npassword.get()=="" :
               messagebox.showerror("Error!","All Feild's are required",parent=self.root2)
          else:
               try:
                    con = sqlite3.connect('database.db')
                    cur = con.cursor()
                    cur.execute("SELECT * FROM Registration Where f_name==?and s_question==? and a_nswer==?", (self.txt_fname.get(),self.cmb_quest.get(),self.txt_ANS.get()))
                    row = cur.fetchone()
                    if row == None:
                         messagebox.showerror("Error!", "Please enter correct answer and question", parent=self)
                    else:
                         cur.execute("UPDATE  Registration SET p_word==? Where f_name==?",
                                     ( self.txt_Npassword.get(),self.txt_fname.get()))
                         con.commit()
                         con.close()
                         messagebox.showinfo("information","Password change successfully",parent=self.root2)
               except Exception as es:
                  messagebox.showerror("Error!", f"Error due to :{str(es)}", parent=self)

          self.root2.destroy()


     def openRegister(self):
         reg = Registration.Register()
         self.destroy()

