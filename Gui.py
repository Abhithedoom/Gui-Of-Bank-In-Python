from tkinter import *
import mysql.connector
from mysql.connector import Error
import random


class windowclass():
    def __init__(self, master):
        self.master = master
        self.btn = Button(master, text=" User Register ", width="20", height="5", bg="red", font="30", fg="White",
                          command=self.command)
        # self.btn.pack()
        self.btn1 = Button(master, text=" User Login ", width="20", height="5", bg="red", font="30", fg="White",
                           command=self.command1)
        # self.btn.pack()
        self.btn.place(x=150, y=50)
        self.btn1.place(x=150, y=200)

    def command(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("500x500")
        app = Demo2(toplevel)

    def command1(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("500x500")
        app = Demo3(toplevel)


class Demo2:
    def __init__(s, master):
        s.master = master
        s.ty = Label(master, text='Account Type :', font='30', fg='red')
        s.name1 = Label(master, text='Name :', font='30', fg='red')
        s.email1 = Label(master, text='Email :', font='30', fg='red')
        s.phone = Label(master, text='Phone :', font='30', fg='red')
        s.amount1 = Label(master, text='Amount :', font='30', fg='red')
        s.v = StringVar()

        s.R1 = Radiobutton(master, text="Saving", padx=20, variable=s.v, value="saving")
        s.R2 = Radiobutton(master, text="Current", padx=20, variable=s.v, value="current")

        s.name2 = Entry(master, width=30, bd=4)
        s.email2 = Entry(master, width=30, bd=4)
        s.phone2 = Entry(master, width=30, bd=4)
        s.amount2 = Entry(master, width=30, bd=4)

        s.b1 = Button(master, text='add', command=s.Add)
        s.ty.place(x=100, y=20)
        s.name1.place(x=100, y=80)
        s.email1.place(x=100, y=110)
        s.phone.place(x=100, y=140)
        s.amount1.place(x=100, y=180)
        s.R1.place(x=100, y=50)
        s.R2.place(x=300, y=50)

        s.name2.place(x=300, y=80)
        s.email2.place(x=300, y=110)
        s.phone2.place(x=300, y=140)
        s.amount2.place(x=300, y=180)
        s.b1.place(x=100, y=200)

    def Add(self):

        # acty3=self.ty2.get()
        name3 = self.name2.get()
        email3 = self.email2.get()
        phone3 = self.phone2.get()
        amount3 = self.amount2.get()
        R11 = self.v.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="abhi",
            database="e"
        )
        mycursor = mydb.cursor()

        try:

            i = random.randint(0000, 9999)
            sql = "INSERT INTO bankatm1(pin, acty, name, email, phone, amount) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (i, R11, name3, email3, phone3, amount3)
            mycursor.execute(sql, val)
            mydb.commit()
        except Error as e:
            print("not", e)

        self.master.withdraw()
        self.master.destroy()
        root = Tk()
        root.title("window")
        root.geometry("500x500")
        app = Demo3(root)
        root.mainloop()


class Demo3:
    s = 0

    def __init__(s, master):
        s.master = master
        s.acno = Label(master, text='Account No :', font='30', fg='red')
        s.pin = Label(master, text='Pin :', font='30', fg='red')

        s.acno2 = Entry(master, width=30, bd=4)
        s.pin2 = Entry(master, width=30, bd=4)
        s.acno.place(x=100, y=80)
        s.pin.place(x=100, y=110)

        s.b1 = Button(master, text='Login', command=s.log)
        s.acno2.place(x=300, y=80)
        s.pin2.place(x=300, y=110)
        s.b1.place(x=100, y=200)
        s.b1 = Button(master, text='Exit', command=s.close_windows)
        s.b1.place(x=200, y=200)

    def log(self):
        s = 0
        # acty3=self.ty2.get()
        acno3 = self.acno2.get()
        pin3 = self.pin2.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="abhi",
            database="e"
        )
        mycursor = mydb.cursor()

        try:

            i = random.randint(0000, 9999)
            mycursor.execute('SELECT amount FROM bankatm1 WHERE acno = %s and pin = %s' % (acno3, pin3))

            am = mycursor.fetchall()
            if len(am) > 0:
                s = 1

        except Error as e:
            print("not", e)

        if s == 1:
            self.master.withdraw()
            self.master.destroy()
            print("login")

            root = Tk()
            root.title("window")
            root.geometry("500x500")
            app = Demo4(root)
            root.mainloop()

        else:

            self.master.withdraw()
            toplevel = Toplevel(self.master)
            toplevel.geometry("500x500")
            app = Demo3(toplevel)

    def close_windows(self):
        self.master.destroy()


class Demo4:
    s = 0

    def __init__(s, master):
        s.master = master
        s.b1 = Button(master, text='Balance', command=s.balance)
        s.b1.place(x=100, y=100)

        s.b1 = Button(master, text='Withdraw', command=s.withdraw)
        s.b1.place(x=100, y=200)
        s.b2 = Button(master, text='Deposit', command=s.deposit)
        s.b2.place(x=100, y=300)

        s.b2 = Button(master, text='logout', command=s.logout)
        s.b2.place(x=100, y=400)

    def balance(s):
        s.master.withdraw()
        s.master.destroy()
        root = Tk()
        root.title("window")
        root.geometry("500x500")
        app = balance(root)
        root.mainloop()

    def withdraw(s):
        s.master.withdraw()
        s.master.destroy()
        root = Tk()
        root.title("window")
        root.geometry("500x500")
        app = Withdraw(root)
        root.mainloop()

    def deposit(s):
        s.master.withdraw()
        s.master.destroy()
        root = Tk()
        root.title("window")
        root.geometry("500x500")
        app = deposit(root)
        root.mainloop()

    def logout(self):
        self.master.withdraw()
        self.master.destroy()
        root = Tk()
        root.title("window")
        root.geometry("500x500")
        app = Demo3(root)
        root.mainloop()


class Withdraw:

    def __init__(s, master):
        s.master = master
        s.pin1 = Label(master, text='Pin :', font='30', fg='red')

        s.pin2 = Entry(master, width=30, bd=4)
        s.pin1.place(x=100, y=80)
        s.pin2.place(x=300, y=80)

        s.acno = Label(master, text='Enter Amount :', font='30', fg='red')

        s.acno2 = Entry(master, width=30, bd=4)
        s.acno.place(x=100, y=120)

        s.b1 = Button(master, text='Withdraw', command=s.log)
        s.acno2.place(x=300, y=120)
        s.b1.place(x=100, y=200)

    def log(self):

        pin3 = self.pin2.get()
        acno3 = self.acno2.get()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="abhi",
            database="e"
        )
        mycursor = mydb.cursor()

        try:

            mycursor.execute('SELECT amount FROM bankatm1 WHERE pin = %s' % (pin3))

            am = mycursor.fetchall()
            am1 = 0
            for x in am:
                am1 = x
            amount1 = acno3
            if int(amount1) > int(am1[0]):

                print("balance")
            else:
                a = int(am1[0]) - int(amount1)
                print(a)
                up1 = mydb.cursor()
                sql = "UPDATE bankatm1 SET amount = %s WHERE pin = %s"
                val = (a, pin3)
                up1.execute(sql, val)
                mydb.commit()
        except Error as e:
            print("not", e)
        self.master.withdraw()
        self.master.destroy()
        root = Tk()
        root.title("window")
        root.geometry("500x500")
        app = Demo4(root)
        root.mainloop()


class balance:

    def __init__(s, master):
        s.master = master
        s.pin1 = Label(master, text='Pin :', font='30', fg='red')

        s.pin2 = Entry(master, width=30, bd=4)
        s.pin1.place(x=100, y=80)
        s.pin2.place(x=300, y=80)

        s.acno = Label(master, text='Enter Amount :', font='30', fg='red')

        s.acno2 = Entry(master, width=30, bd=4)
        s.acno.place(x=100, y=120)

        s.b1 = Button(master, text='Show Balance', command=s.log)
        s.acno2.place(x=300, y=120)
        s.b1.place(x=100, y=200)

    def log(self):

        pin3 = self.pin2.get()
        acno3 = self.acno2.get()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="abhi",
            database="e"
        )
        mycursor = mydb.cursor()

        try:

            mycursor.execute('SELECT amount FROM bankatm1 WHERE pin = %s' % (pin3))

            am = mycursor.fetchall()
            am1 = 0
            for x in am:
                am1 = x
            amount1 = acno3
            if int(amount1) > int(am1[0]):

                print("balance")
            else:
                a = int(am1[0]) - int(amount1)
                print(a)
                up1 = mydb.cursor()
                sql = "UPDATE bankatm1 SET amount = %s WHERE pin = %s"
                val = (a, pin3)
                up1.execute(sql, val)
                mydb.commit()
        except Error as e:
            print("not", e)
        self.master.withdraw()
        self.master.destroy()
        root = Tk()
        root.title("window")
        root.geometry("500x500")
        app = Demo4(root)
        root.mainloop()


class deposit:

    def __init__(s, master):
        s.master = master
        s.pin1 = Label(master, text='Pin :', font='30', fg='red')

        s.pin2 = Entry(master, width=30, bd=4)
        s.pin1.place(x=100, y=80)
        s.pin2.place(x=300, y=80)

        s.acno = Label(master, text='Enter Amount :', font='30', fg='red')

        s.acno2 = Entry(master, width=30, bd=4)
        s.acno.place(x=100, y=120)

        s.b1 = Button(master, text='Deposit', command=s.log)
        s.acno2.place(x=300, y=120)
        s.b1.place(x=100, y=200)

    def log(self):

        pin3 = self.pin2.get()
        acno3 = self.acno2.get()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="abhi",
            database="e"
        )
        mycursor = mydb.cursor()

        try:

            mycursor.execute('SELECT amount FROM bankatm1 WHERE pin = %s' % (pin3))

            am = mycursor.fetchall()
            am1 = 0
            for x in am:
                am1 = x
            amount1 = acno3
            a = int(am1[0]) + int(amount1)
            print(a)
            up1 = mydb.cursor()
            sql = "UPDATE bankatm1 SET amount = %s WHERE pin = %s"
            val = (a, pin3)
            up1.execute(sql, val)
            mydb.commit()
        except Error as e:
            print("not", e)
        self.master.withdraw()
        self.master.destroy()
        root = Tk()
        root.title("window")
        root.geometry("500x500")
        app = Demo4(root)
        root.mainloop()  


root = Tk()
root.title("window")
root.geometry("500x500")
cls = windowclass(root)
root.mainloop()
