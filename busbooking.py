from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.Connection("Database.db")

c = conn.cursor()

c.execute(
    "CREATE Table IF NOT EXISTS BUS(OPERATOR text,BUS_TYPE text,D_FROM text,A_TO text,DATE text,DEP_TIME text,ARR_TIME text,FARE integer,SEATS integer)")
conn.commit()


splash_root = Tk()
splash_root.geometry("1000x1000")
splash_label = Label(splash_root, text="Python and DBS Project", font="Times 50 bold", relief="raised")
splash_label.pack()
img1 = PhotoImage(file="Python.png")
splash_image = Label(splash_root, image=img1).pack()
splash_label = Label(splash_root, text="Samarth Dubey", font="Times 30 bold")
splash_label.pack()
splash_label = Label(splash_root, text="191B304", font="Times 30 bold")
splash_label.pack()
splash_label = Label(splash_root, text="B9", font="Times 30 bold")
splash_label.pack()
def splashDestroy():
	splash_root.destroy()
splash_root.after(2000,splashDestroy)
splash_root.mainloop()

root = Tk()
root.geometry("1000x1000")
root_label = Label(root, text="BUS BOOKING SERVICE", fg="blue",font="Times 50 bold", relief="raised")
root_label.grid(columnspan=3,padx=100,pady=30)
img = PhotoImage(file="Bus.png")
root_image = Label(root, image=img).grid(columnspan=3,padx=100,pady=100)

def add_bus():
    add_root = Tk()
    global img2
    add_root.geometry("1000x1000")
    # img2 = PhotoImage(file="bus.png")
    # Label(add_root, image=img2).grid()
    add_root_label = Label(add_root, text="BUS BOOKING SERVICE", fg="blue",font="Times 50 bold", relief="raised")
    add_root_label.grid(padx=100,pady=30,columnspan=2)
    
    def detail():
        l1=Label(add_root,text="Operator ID").grid()
        e1=Entry(add_root)
        e1.grid(row=9,column=1)
        V=StringVar(add_root)
        V.set("All Types")
        choice=['A/C','Non-A/C','A/C Sleeper','Non-A/C Sleeper','All Types']
        l2=Label(add_root, text="Bus Type").grid()
        e2=OptionMenu(add_root, V, *choice)
        e2.grid(row=10,column=1)
        l3=Label(add_root,text="From Where").grid()
        e3=Entry(add_root)
        e3.grid(row=11,column=1)
        l4=Label(add_root,text="To Where").grid()
        e4=Entry(add_root)
        e4.grid(row=12,column=1)
        l5=Label(add_root,text="Date").grid()
        e5=Entry(add_root)
        e5.grid(row=13,column=1)
        l6=Label(add_root,text="Arrival Time").grid()
        e6=Entry(add_root)
        e6.grid(row=14,column=1)
        l6=Label(add_root,text="Departure Time").grid()
        e7=Entry(add_root)
        e7.grid(row=15,column=1)
        l7=Label(add_root,text="Fare").grid()
        e8=Entry(add_root)
        e8.grid(row=16,column=1)
        l7=Label(add_root,text="Seats").grid()
        e9=Entry(add_root)
        e9.grid(row=17,column=1)
        def Save():
            conn = sqlite3.connect('Database.db')
            c = conn.cursor()
            values =(e1.get(),V.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
            c.execute("""INSERT INTO BUS(OPERATOR,BUS_TYPE,D_FROM,A_TO ,DATE,DEP_TIME ,ARR_TIME ,FARE ,SEATS)
                          VALUES(?,?,?,?,?,?,?,?,?)""", values)
            values =(e1.get(),V.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
            conn.commit()
            row = c.fetchall()
            print(row)
            conn.close()
            add_root.destroy()
            messagebox.showinfo("DATA", "DATA SAVED")

        b2=Button(add_root,text="Save",command=Save).grid(row=18,column=1)
        

    Heading=Label(add_root,text="Bus Operator Detail Filling" ,font='Times 30 bold').grid(padx=100,pady=10,columnspan=2)
    l1=Label(add_root,text="Full Name").grid(row=5)
    e1=Entry(add_root)
    e1.grid(row=5,column=1)
    l2=Label(add_root,text="Contact Number").grid()
    e2=Entry(add_root)
    e2.grid(row=6,column=1)
    l3=Label(add_root,text="Address").grid()
    e3=Entry(add_root)
    e3.grid(row=7,column=1)
    def check():
        if(e1.get()=="" or e2.get()=="" or e3.get==""):
            add_root.destroy()
            messagebox.showinfo("error","Insert values")
        else:
            detail()
    b1=Button(add_root,text="Add Details",command=check).grid(row=8,column=1)
    
    
    add_root.mainloop()

def search_bus():
    search_root = Tk()
    search_root.geometry("1000x1000")
    search_root_label = Label(search_root, text="BUS BOOKING SERVICE", fg="blue",font="Times 50 bold", relief="raised")
    search_root_label.grid(padx=100,pady=30,columnspan=2)
    Heading=Label(search_root,text="Bus Details" ,font='Times 30 bold').grid(padx=100,pady=10,columnspan=2)

    V=StringVar(search_root)
    V.set("All Types")
    choice=['A/C','Non-A/C','A/C Sleeper','Non-A/C Sleeper','All Types']

    l1=Label(search_root, text="Type of Bus").grid(row=5,column=0)
    OptionMenu(search_root, V, *choice).grid(row=5,column=1)
    l2 = Label(search_root, text="From Where").grid(row=6,column=0)
    e1 = Entry(search_root)
    e1.grid(row=6,column=1)
    l3 = Label(search_root, text="Where to").grid(row=7,column=0)
    e2= Entry(search_root)
    e2.grid(row=7,column=1)
    l4= Label(search_root, text="Date").grid(row=8,column=0)
    e3= Entry(search_root)
    e3.grid(row=8,column=1)
    def bookingScreen():
        bookingScreen_root = Tk()
        bookingScreen_root.geometry("1000x1000")
        H1 = Label(bookingScreen_root, text="BUS BOOKING SERVICE", fg="blue",font="Times 50 bold", relief="raised")
        H1.grid(padx=100,pady=30,columnspan=11)
        H2=Label(bookingScreen_root,text="Booking Screen" ,font='Times 30 bold').grid(padx=100,pady=10,columnspan=11)
        aa=e1.get()
        bb=e2.get()
        cc=V.get()
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM BUS WHERE D_FROM= ? AND A_TO = ? AND BUS_TYPE = ?",(aa,bb,cc))
        conn.commit()
        ro=c.fetchall()
        l=int(0)
        w=int(3)
        for i in ro:
            l=int(0)
            for j in i:
                qwerty=Label(bookingScreen_root,text=j , bg="yellow")
                qwerty.grid(column=l,row=w,padx=4)  
                l=l+1
            w=w+1
            
        print(ro)
        conn.close()
        l1=Label(bookingScreen_root, text="Operator").grid(row=2,column=0)
        l2=Label(bookingScreen_root, text="Type").grid(row=2,column=1)
        l3=Label(bookingScreen_root, text="From").grid(row=2,column=2)
        l4=Label(bookingScreen_root, text="To").grid(row=2,column=3)
        l5=Label(bookingScreen_root, text="Date").grid(row=2,column=4)
        l6=Label(bookingScreen_root, text="Dept Time").grid(row=2,column=5)
        l7=Label(bookingScreen_root, text="Arr Time").grid(row=2,column=6)
        l8=Label(bookingScreen_root, text="Fare").grid(row=2,column=7)
        l9=Label(bookingScreen_root, text="Seats Availability").grid(row=2,column=8)
       
            
        def quit_booking():
            bookingScreen_root.destroy()
            
        HomeButton = Button(bookingScreen_root, text="Home", command=quit_booking).grid(columnspan=11,padx=100,pady=100)
        bookingScreen_root.mainloop()

    def check():
        if(e1.get()=="" or e2.get()=="" or e3.get==""):
            search_root.destroy()
            messagebox.showinfo("error","Insert values")
        else:
            bookingScreen()

    Button1 = Button(search_root, text="Find Buses", command=check).grid(column=1)
    def quit_search():
        search_root.destroy()
    HomeButton = Button(search_root, text="Home",fg="red", command=quit_search,padx=10,pady=10).grid(columnspan=2,padx=20,pady=20)
    
    search_root.mainloop()

add_button = Button(root, text="Add Bus", width=15, height=5, command=add_bus).grid(column=0,row=3)
search_button = Button(root, text="Search Bus", width=15, height=5, command=search_bus).grid(column=2,row=3)

root.mainloop()