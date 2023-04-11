import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def sqlex():
				mydb=mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="ims")
				mycursor2=mydb.cursor()
				sql=T.get(1.0, "end-1c")
				mycursor2.execute(sql)
				y=mycursor2.fetchall()
				output_sql=Label(root,text=y,wraplength=150)#customer 150 #selects 70
				output_sql.place(x=1000,y=580)


def GetValue(event):
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    row_id = listbox.selection()[0]
    select = listbox.set(row_id)
    e1.insert(0,select['pid'])
    e2.insert(0,select['pname'])
    e3.insert(0,select['p_stock'])
    e4.insert(0,select['price'])
    e5.insert(0,select['bid'])
    e6.insert(0,select['cid'])
    e7.insert(0,select['sid'])


def Insert():
    pid=e1.get()
    pname=e2.get()
    p_stock=e3.get()
    price=e4.get()
    bid=e5.get()
    cid=e6.get()
    sid=e7.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="ims")
    mycursor=mysqldb.cursor()
    
    try:
        sql = "INSERT into product (pid,pname,p_stock,price,bid,cid,sid) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (pid,pname,p_stock,price,bid,cid,sid)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information","Record inserted successfully.")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e1.focus_set()
    
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def Update():
    pid=e1.get()
    pname=e2.get()
    p_stock=e3.get()
    price=e4.get()
    bid=e5.get()
    cid=e6.get()
    sid=e7.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="ims")
    mycursor=mysqldb.cursor()

    try:
        sql = "UPDATE product SET pname=%s,p_stock=%s,price=%s,bid=%s,cid=%s,sid=%s where pid=%s"
        val = (pname,p_stock,price,bid,cid,sid,pid)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information","Record updated successfully.")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e1.focus_set()
    
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def Delete():
    pid = e1.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="ims")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "Delete from product where pid = %s"
       val = (pid,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleted successfully...")
 
       e1.delete(0,END)
       e2.delete(0,END)
       e3.delete(0,END)
       e4.delete(0,END)
       e5.delete(0,END)
       e6.delete(0,END)
       e7.delete(0,END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()



def show():
    mysqldb = mysql.connector.connect(host="localhost",user="root",password="",database="ims")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT pid,pname,p_stock,price,bid,cid,sid FROM product")
    records = mycursor.fetchall()
    print(records)

    for i,(pid,pname,p_stock,price,bid,cid,sid) in enumerate(records ,start=1):
        listbox.insert("","end",values=(pid,pname,p_stock,price,bid,cid,sid))
        mysqldb.close()

root = Tk()
root.geometry("1500x800")
global e1
global e2
global e3
global e4
global e5
global e6
global e7

tk.Label(root,text="Inventory Management System",fg='black',font=(None,20)).place(x=600,y=5)
tk.Label(root,text="Brand ID's are 1.APPLE,2.SAMSUNG,3.SONY,4.LG,5.ONE PLUS,6.PANASONIC",fg='black',font=(None,20)).place(x=400,y=70)
tk.Label(root,text="CATEGORY ID'S are 1.MOBILES,2.TV,3.SPEAKERS,4.LAPTOP,5.SPARE ACC",fg='black',font=(None,20)).place(x=400,y=135)

Label(root,text="Enter Product ID").place(x=10,y=10)
Label(root,text="Enter Product name").place(x=10,y=40)
Label(root,text="Enter Product stock").place(x=10,y=70)
Label(root,text="Enter Product Price").place(x=10,y=100)
Label(root,text="Enter Brand id").place(x=10,y=130)
Label(root,text="Enter Category id").place(x=10,y=160)
Label(root,text="Enter Store/Supplier id").place(x=10,y=190)

e1 = Entry(root)
e1.place(x=150,y=10)

e2 = Entry(root)
e2.place(x=150,y=40)

e3 = Entry(root)
e3.place(x=150,y=70)

e4 = Entry(root)
e4.place(x=150,y=100)

e5 = Entry(root)
e5.place(x=150,y=130)

e6 = Entry(root)
e6.place(x=150,y=160)

e7 = Entry(root)
e7.place(x=150,y=190)

Button(root,text="Insert",command=Insert,height=3,width=12).place(x=30,y=250)
Button(root,text="Update",command=Update,height=3,width=12).place(x=140,y=250)
Button(root,text="Delete",command=Delete,height=3,width=12).place(x=250,y=250)
tk.Label(root, text="Enter the query below", fg="red", font=(None, 20)).place(x=5, y=600)

T = Text(root, height = 3, width = 100)
T.place(x=5,y=640)

butn=Button(root,text="Submit",command=sqlex)
butn.place(x=850,y=650)

tk.Label(root,text="Output:",fg="blue", font=(None, 15)).place(x=850,y=600)



cols = ('pid','pname','p_stock','price','bid','cid','sid')
listbox = ttk.Treeview(root,columns=cols,show='headings')

for col in cols:
    listbox.heading(col,text=col)
    listbox.grid(row=1,column=0,columnspan=2)
    listbox.place(x=70,y=350)

show()
listbox.bind('<Double-Button-1>',GetValue)

root.mainloop()


