from tkinter import*
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox


import sqlite3



class Register(Toplevel):
     def __init__(self):
         Toplevel.__init__(self)
         self.title("Registration Windows")
         self.geometry("1350x700+0+0")


         # ======================image=======================
         self.bg_icon = ImageTk.PhotoImage(file="images\paris.jpg")
         bg_lbl = Label(self, image=self.bg_icon).pack()
         self.left = ImageTk.PhotoImage(file=r"images\run.jpg")
         left = Label(self, image=self.left).place(x=100, y=100, width=400, height=520)

         # ===================register frame==================
         frame1 = Frame(self, bg="white",bd=2,relief=RIDGE)
         frame1.place(x=500, y=100, width=700, height=520)

         title = Label(frame1, text="REGISTER HERE", font=("time new roman", 20, "bold"), bg="black", fg="white").place(
             x=185, y=10, width=300)
         # ========================entry===================================================
         # =======row1==============
         f_name = Label(frame1, text="First Name*", font=("time new roman", 15, "bold"), bg="white", fg="grey").place(
             x=70, y=80)
         self.txt_fname = Entry(frame1, font=("", 15), bg="lightgrey")
         self.txt_fname.place(x=70, y=110)

         self.l_name = Label(frame1, text="Last Name*", font=("time new roman", 15, "bold"), bg="white", fg="grey").place(
             x=390, y=80)
         self.txt_lname = Entry(frame1, font=("", 15), bg="lightgrey")
         self.txt_lname.place(x=390, y=110, width=250)
         # =======row2==============
         self.contact = Label(frame1, text="Phone Number*", font=("time new roman", 15, "bold"), bg="white",
                         fg="grey").place(x=70, y=160)
         self.txt_contact = Entry(frame1, font=("", 15), bg="lightgrey")
         self.txt_contact.place(x=70, y=190)

         self.email = Label(frame1, text="Email Address*", font=("time new roman", 15, "bold"), bg="white", fg="grey").place(
             x=390, y=160)
         self.txt_email = Entry(frame1, font=("", 15), bg="lightgrey")
         self.txt_email.place(x=390, y=190, width=250)
         # =======row3==============
         question = Label(frame1, text="Questions*", font=("time new roman", 15, "bold"), bg="white", fg="grey").place( x=70, y=240)

         self.cmb_quest = ttk.Combobox(frame1, font=("", 12), state="readonly", justify=CENTER)
         self.cmb_quest['value'] = ("--Select--", "Your pet name", "Your date of birth", "Your nickname")
         self.cmb_quest.place(x=70, y=270, width=220, height=28)
         self.cmb_quest.current(0)

         self.answer = Label(frame1, text="Answer*", font=("time new roman", 15, "bold"), bg="white", fg="grey").place(x=390,  y=240)

         self.txt_answer = Entry(frame1, font=("", 15), bg="lightgrey")
         self.txt_answer.place(x=390, y=270, width=250)
         # =======row4==============
         self.password = Label(frame1, text="Password*", font=("time new roman", 15, "bold"), bg="white", fg="grey").place( x=70, y=320)

         self.txt_password = Entry(frame1, font=("", 15), bg="lightgrey")
         self.txt_password.place(x=70, y=349)

         self.cpassword = Label(frame1, text="Comfirm password*", font=("time new roman", 15, "bold"), bg="white",fg="grey").place(x=390, y=320)

         self.txt_cpassword = Entry(frame1, font=("", 15), bg="lightgrey")
         self.txt_cpassword.place(x=390, y=349, width=250)
         # =============checkbox=========
         self.var_chk=IntVar()
         self.chk = Checkbutton(frame1, text="I Agree All Terms & Condition", bg="white",variable=self.var_chk, onvalue=1, offvalue=0)
         self.chk.place(x=70,y=385)

         self.btn_image = ImageTk.PhotoImage(file=r"images\button.jpg")
         btn=Button(frame1, image=self.btn_image, bg="white", bd=0, cursor="hand2",command=self.register)
         btn.place(x=280, y=420, width=170, height=80)




         self.btn = Button(self, text="Home", font=("time new roman", 15, "bold"), bd=1, cursor="hand2",activebackground="lightblue",
                      bg="skyblue", fg="black", command=self.destroy).place(x=210, y=520, width=190, height=50)
         self.home = ImageTk.PhotoImage(file=r"images\home-icon.png")
         home = Label(self, image=self.home, bg="skyblue").place(x=240, y=530)

     def register(self):
         if self.txt_fname.get() == "" or self.cmb_quest.get() == "--Select--" or self.txt_lname.get() == "" or  self.txt_email.get() == "" or self.txt_contact.get() == "" or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
             messagebox.showerror("Error!", "All Feild's are required",parent=self)

         elif self.txt_cpassword.get() != self.txt_password.get():
             messagebox.showerror("Error!", "password are not same",parent=self)
         elif '@gmail.com' not in self.txt_email.get() or self.txt_email.get() == "":
             messagebox.showerror('Login error', "PLease Write the Valid Email",parent=self)
         elif len(self.txt_contact.get()) != 10:
             messagebox.showerror('Login error', "PLease Write the Valid phone", parent=self)
         elif self.var_chk.get() == 0:
             messagebox.showerror("Error!", "please agree term & condition",parent=self)
         else:
             try:
                 con = sqlite3.connect('database.db')
                 cur = con.cursor()
                 cur.execute("SELECT * FROM Registration Where e_address==?and p_number==?",
                             ( self.txt_contact.get(),
                                 self.txt_email.get()))
                 row = cur.fetchone()
                 if row!=None:
                     messagebox.showerror("Error!", "user already exist with these phone number and email,please try again with different phone number and email.", parent=self)
                 else:
                      cur.execute("INSERT INTO Registration (f_name ,l_name,p_number,e_address,s_question,a_nswer,p_word)  VALUES(?,?,?,?,?,?,?)",
                                 (
                                   self.txt_fname.get(),
                                   self.txt_lname.get(),
                                   self.txt_contact.get(),
                                   self.txt_email.get(),
                                   self.cmb_quest.get(),
                                   self.txt_answer.get(),
                                   self.txt_password.get()
                                     ))
                      con.commit()
                      con.close()

                      messagebox.showinfo("information", "successfully Register", parent=self)

             except Exception as es:
                 messagebox.showerror("Error!", f"Error due to :{str(es)}", parent=self)


         self.clear()

     def clear(self):
         self.txt_fname.delete(0, END)
         self.txt_lname.delete(0, END)
         self.txt_password.delete(0, END)
         self.txt_cpassword.delete(0, END)
         self.txt_contact.delete(0, END)
         self.txt_email.delete(0, END)
         self.txt_answer.delete(0, END)
         self.cmb_quest.current(0)
         self.chk.deselect()

