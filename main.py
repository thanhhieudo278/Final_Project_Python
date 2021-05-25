from domains import Customer
from domains import Bill
from domains import Dataplan
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import mysql.connector


def Add_Customer():
    object = Customer.Customer()
    object.setCustomerInfo(cusid.get(), cusname.get(), numphone.get(), adrs.get())

    id = object.getCustomerInfo_id()
    name = object.getCustomerInfo_name()
    phonenumber = object.getCustomerInfo_phoneNumber()
    address = object.getCustomerInfo_address()

    if id == "":
        messagebox.showinfo("Add customer", "id can't be empty!")
    elif name == "":
        messagebox.showinfo("Add customer", "name can't be empty!")
    elif phonenumber == "":
        messagebox.showinfo("Add customer", "phonenumber can't be empty!")
    elif address == "":
        messagebox.showinfo("Add customer", "address can't be empty!")
    else:

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"

        )
        cursor = db.cursor()
        try:
            cursor.execute("""INSERT INTO Customer(Customer_id,Customer_name,Customer_phoneNumber,Customer_address)
                               VALUES (%s,%s, %s,%s)""", (id, name, phonenumber, address))
            db.commit()
            messagebox.showinfo("Add customer", "Success!")
        except:
            messagebox.showinfo("Add customer", "Something error!")
            db.rollback()
        db.close()

def Update_Customer():
    object = Customer.Customer()
    object.setCustomerInfo(cusid.get(), cusname.get(), numphone.get(), adrs.get())

    id = object.getCustomerInfo_id()
    name = object.getCustomerInfo_name()
    phonenumber = object.getCustomerInfo_phoneNumber()
    address = object.getCustomerInfo_address()

    if id == "":
        messagebox.showinfo("Update customer", "id can't be empty!")
    elif name == "":
        messagebox.showinfo("Update customer", "name can't be empty!")
    elif phonenumber == "":
        messagebox.showinfo("Update customer", "phonenumber can't be empty!")
    elif address == "":
        messagebox.showinfo("Update customer", "address can't be empty!")
    else:

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"

        )
        cursor = db.cursor()
        try:
            cursor.execute("""UPDATE Customer SET Customer_name = %s,Customer_phoneNumber =%s ,Customer_address= %s WHERE Customer_id = %s""",
                (name, phonenumber, address, id))

            db.commit()
            messagebox.showinfo("Update customer", "Success!")
        except:
            messagebox.showinfo("Update customer", "Something error!")
            db.rollback()
        db.close()



def Remove_Customer():
    object = Customer.Customer()
    object.setCustomerInfo(cusid.get(), cusname.get(), numphone.get(), adrs.get())
    id = object.getCustomerInfo_id()
    if id == "":
        messagebox.showinfo("Remove customer", "id can't be empty!")
    else:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"
        )
        cursor = db.cursor()
        try:
            cursor.execute("""DELETE FROM Customer WHERE Customer_id = %s """, (id,))
            db.commit()
            messagebox.showinfo("Add customer", "Success!")
        except:
            messagebox.showinfo("Add customer", "Something error!")
            db.rollback()
    db.close()


def Search_Customer():
    id = searchcustomer.get()
    if id == "":
        messagebox.showinfo("Search customer", "id can't be empty!")
    else:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"
        )
        cursor = db.cursor()
        try:
            cursor.execute("""SELECT * FROM Customer WHERE Customer_id = %s""", (id,))
            result = cursor.fetchall()
            for i in result:
                cusid.delete(0, END)
                cusid.insert(END, i[0])
                cusname.delete(0, END)
                cusname.insert(END, i[1])
                numphone.delete(0, END)
                numphone.insert(END, i[2])
                adrs.delete(0, END)
                adrs.insert(END, i[3])
            messagebox.showinfo("Search customer", "Success!")
        except:
            messagebox.showinfo("Search customer", "Something error!")
            db.rollback()
    db.close()


def Insert_Table_Customer():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="internet_service_information_management_system"
    )
    cursor = db.cursor()
    cursor.execute("""SELECT Customer_id ,Customer_name, Customer_phoneNumber, Customer_address FROM Customer """)
    customer = cursor.fetchall()

    for i in Table_customer.get_children():
        Table_customer.delete(i)
    for i, (Customer_id, Customer_name, Customer_phoneNumber, Customer_address) in enumerate(customer, start=1):
        Table_customer.insert("", "end", values=(Customer_id, Customer_name, Customer_phoneNumber, Customer_address))
    db.close()


def Add_Dataplan():
    object = Dataplan.Dataplan()
    object.setDataplanInfo(dataid.get(), dataname.get(), dataspeed.get(), price.get())
    id = object.getDataplanInfo_id()
    name = object.getDataplanInfo_name()
    speed = object.getDataplanInfo_speed()
    pricepermonth= object.getDataplanInfo_pricepermonth()



    if id == "":
        messagebox.showinfo("Add dataplan", "id can't be empty!")
    elif name == "":
        messagebox.showinfo("Add dataplan", "name can't be empty!")
    elif speed == "":
        messagebox.showinfo("Add dataplan", "speed can't be empty!")
    elif pricepermonth == "":
        messagebox.showinfo("Add dataplan", "price can't be empty!")
    else:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"

        )
        cursor = db.cursor()
        try:

            cursor.execute("""INSERT INTO dataPlan(dataPlan_id,dataPlan_name,dataPlan_speed,dataPlan_price_per_month)
                                    VALUES (%s,%s, %s,%s)""", (id, name, speed, pricepermonth))
            db.commit()
            messagebox.showinfo("Add dataplan", "Success!")
        except:
            messagebox.showinfo("Add dataplan", "Something error!")
            db.rollback()
        db.close()

def Update_Dataplan():
    object = Dataplan.Dataplan()
    object.setDataplanInfo(dataid.get(), dataname.get(), dataspeed.get(), price.get())
    id = object.getDataplanInfo_id()
    name = object.getDataplanInfo_name()
    speed = object.getDataplanInfo_speed()
    pricepermonth = object.getDataplanInfo_pricepermonth()
    if id == "":
        messagebox.showinfo("Update dataplan", "id can't be empty!")
    elif name == "":
        messagebox.showinfo("Update dataplan", "name can't be empty!")
    elif speed == "":
        messagebox.showinfo("Update dataplan", "speed can't be empty!")
    elif pricepermonth == "":
        messagebox.showinfo("Update dataplan", "price can't be empty!")
    else:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"

        )
        cursor = db.cursor()
        try:
            cursor.execute(
                """UPDATE dataPlan SET dataPlan_name=%s,dataPlan_speed=%s,dataPlan_price_per_month=%s WHERE dataPlan_id = %s""",
                (name, speed, pricepermonth, id))
            db.commit()
            messagebox.showinfo("Update dataplan", "Success!")
        except:
            messagebox.showinfo("Update dataplan", "Something error!")
            db.rollback()
        db.close()



def Remove_Dataplan():
    object = Dataplan.Dataplan()
    object.setDataplanInfo(dataid.get(), dataname.get(), dataspeed.get(), price.get())
    id = object.getDataplanInfo_id()
    if id == "":
        messagebox.showinfo("Remove dataplan", "id can't be empty!")
    else:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"
        )
        cursor = db.cursor()
        try:

            cursor.execute("""DELETE FROM dataPlan WHERE dataPlan_id = %s """, (id,))

            db.commit()
            messagebox.showinfo("Remove dataplan", "Success!")
        except:
            messagebox.showinfo("Remove dataplan", "Something Error!")

            db.rollback()
    db.close()


def Search_Dataplan():
    id = searchdata.get()
    if id == "":
        messagebox.showinfo("Search dataplan", "id can't be empty!")
    else:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"
        )

        cursor = db.cursor()
        try:
            cursor.execute("""SELECT * FROM dataPlan WHERE dataPlan_id = %s""", (id,))
            result = cursor.fetchall()
            for i in result:
                dataid.delete(0, END)
                dataid.insert(END, i[0])
                dataname.delete(0, END)
                dataname.insert(END, i[1])
                dataspeed.delete(0, END)
                dataspeed.insert(END, i[2])
                price.delete(0, END)
                price.insert(END, i[3])
            messagebox.showinfo("Search dataplan", "Success!")
        except:
            messagebox.showinfo("Search dataplan", "Something error!")
            db.rollback()
    db.close()


def Insert_Table_dataPlan():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="internet_service_information_management_system"
    )
    cursor = db.cursor()
    cursor.execute("""SELECT dataPlan_id,dataPlan_name, dataPlan_speed, dataPlan_price_per_month FROM dataPlan """)
    dataplan = cursor.fetchall()
    for i in Table_dataplan.get_children():
        Table_dataplan.delete(i)
    for i, (dataPlan_id, dataPlan_name, dataPlan_speed, dataPlan_price_per_month) in enumerate(dataplan, start=1):
        Table_dataplan.insert("", "end", values=(dataPlan_id, dataPlan_name, dataPlan_speed, dataPlan_price_per_month))
    db.close()


def Add_Bill():
    object = Bill.Bill()
    object.setBillInfor(idbill.get(), idcustomer.get(),iddata.get(), regdate.get(),drt.get(),ttl.get())

    billid = object.getBillInfo_Bill_id()
    customerid = object.getBillInfo_Bill_Customerid()
    dataplanid = object.getBillInfo_Bill_Dataplanid()
    registrationdate = object.getBillInfo_Bill_RegistrationDate()
    duration = object.getBillInfo_Bill_Duration()


    if billid == "":
        messagebox.showinfo("Add bill", "id of bill can't be empty!")
    elif customerid == "":
        messagebox.showinfo("Add bill", "id of customer can't be empty!")
    elif dataplanid == "":
        messagebox.showinfo("Add bill", "id of dataplan can't be empty!")
    elif registrationdate == "":
        messagebox.showinfo("Add bill", "Registrationdate can't be empty!")
    elif duration == "":
        messagebox.showinfo("Add bill", "Duration can't be empty!")

    else:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"

        )
        cursor = db.cursor()
        try:
            cursor.execute("""INSERT INTO Bill(Bill_id,Customer_id,DataPlan_id,Registration_date,Duration)
                        VALUES (%s,%s,%s,%s,%s)""",
                           (billid, customerid, dataplanid, registrationdate, duration))
            db.commit()
            messagebox.showinfo("Add bill", "Success!")
        except:
            messagebox.showinfo("Add bill", "Somthing error!")
            db.rollback()
        db.close()


def Update_Bill():
    object = Bill.Bill()
    object.setBillInfor(idbill.get(), idcustomer.get(), iddata.get(), regdate.get(), drt.get(), ttl.get())

    billid = object.getBillInfo_Bill_id()
    customerid = object.getBillInfo_Bill_Customerid()
    dataplanid = object.getBillInfo_Bill_Dataplanid()
    registrationdate = object.getBillInfo_Bill_RegistrationDate()
    duration = object.getBillInfo_Bill_Duration()


    if billid == "":
        messagebox.showinfo("Update bill", "id of bill can't be empty!")
    elif customerid == "":
        messagebox.showinfo("Update bill", "id of customer can't be empty!")
    elif dataplanid == "":
        messagebox.showinfo("Update bill", "id of dataplan can't be empty!")
    elif registrationdate == "":
        messagebox.showinfo("Update bill", "Registrationdate can't be empty!")
    elif duration == "":
        messagebox.showinfo("Update bill", "Duration can't be empty!")

    else:

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"

        )
        cursor = db.cursor()
        try:
            cursor.execute("""UPDATE Bill SET Customer_id=%s,DataPlan_id=%s,Registration_date=%s,Duration=%s WHERE Bill_id = %s""",
                (customerid, dataplanid, registrationdate, duration, billid))

            db.commit()
            messagebox.showinfo("Update bill", "Success!")
        except:
            messagebox.showinfo("Update bill", "Something error!")

            db.rollback()
        db.close()


def Remove_Bill():
    object = Bill.Bill()
    object.setBillInfor(idbill.get(), idcustomer.get(), iddata.get(), regdate.get(), drt.get(), ttl.get())

    billid = object.getBillInfo_Bill_id()
    customerid = object.getBillInfo_Bill_Customerid()
    dataplanid = object.getBillInfo_Bill_Dataplanid()

    if billid == "":
        messagebox.showinfo("Remove bill", "id of bill can't be empty!")
    elif customerid == "":
        messagebox.showinfo("Update bill", "id of customer can't be empty!")
    elif dataplanid == "":
        messagebox.showinfo("Update bill", "id of dataplan can't be empty!")
    else:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"
        )
        cursor = db.cursor()
        try:
            cursor.execute("""DELETE FROM Bill WHERE Bill_id=%s AND Customer_id=%s AND DataPlan_id=%s """, (billid,customerid, dataplanid,))
            db.commit()
            messagebox.showinfo("Remove bill", "Success!")
        except:
            messagebox.showinfo("Remove bill", "Somtheing error!")
            db.rollback()
    db.close()


def Search_Bill():
    object = Bill.Bill()
    object.setBillInfor(idbill.get(), idcustomer.get(), iddata.get(), regdate.get(), drt.get(), ttl.get())

    customerid = object.getBillInfo_Bill_Customerid()
    dataplanid = object.getBillInfo_Bill_Dataplanid()

    if customerid == "":
        messagebox.showinfo("Search bill", "id of customer can't be empty!")
    elif dataplanid == "":
        messagebox.showinfo("Search bill", "id of dataplan can't be empty!")
    else:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"
        )
        cursor = db.cursor()
        try:
            cursor.execute("""SELECT * FROM Bill WHERE Customer_id=%s AND DataPlan_id=%s""", (customerid, dataplanid,))
            result = cursor.fetchall()
            for i in result:
                idbill.delete(0, END)
                idbill.insert(END, i[0])
                idcustomer.delete(0, END)
                idcustomer.insert(END, i[1])
                iddata.delete(0, END)
                iddata.insert(END, i[2])
                regdate.delete(0, END)
                regdate.insert(END, i[3])
                drt.delete(0, END)
                drt.insert(END, i[4])
                ttl.delete(0, END)
                ttl.insert(END, i[5])

            messagebox.showinfo("Search bill", "Success!")
        except:
            messagebox.showinfo("Search bill", "Something Error!")
            db.rollback()
    db.close()



def Calculate_Total_Amount():
    object = Bill.Bill()
    object.setBillInfor(idbill.get(), idcustomer.get(), iddata.get(), regdate.get(), drt.get(), ttl.get())

    customerid = object.getBillInfo_Bill_Customerid()
    dataplanid = object.getBillInfo_Bill_Dataplanid()


    if customerid == "":
        messagebox.showinfo("Search bill", "id of customer can't be empty!")
    elif dataplanid == "":
        messagebox.showinfo("Search bill", "id of dataplan can't be empty!")
    else:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"
        )
        cursor = db.cursor()
        try:
            cursor.execute("""SELECT Duration FROM Bill WHERE Customer_id=%s AND DataPlan_id=%s""", (customerid, dataplanid,))
            durationtocalculate = cursor.fetchone()
            cursor.execute("""SELECT dataPlan_price_per_month FROM dataPlan WHERE  dataPlan_id=%s""", (dataplanid,))
            pricetocalculate= cursor.fetchone()
            total_amountcalculated = durationtocalculate[0]*pricetocalculate[0]
            cursor.execute("""UPDATE Bill SET total_amount=%s WHERE (SELECT Bill_id  WHERE Customer_id=%s AND DataPlan_id=%s)""", (total_amountcalculated,customerid, dataplanid,))
            db.commit()
            messagebox.showinfo("caculate total_amount ", "Success!")
        except:
            messagebox.showinfo("caculate total_amount ", "fail!")
        db.close()

def Insert_Table_Bill():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="internet_service_information_management_system"
    )

    cursor = db.cursor()
    cursor.execute("""SELECT Bill_id,Customer_id,DataPlan_id,Registration_date,Duration,total_amount FROM Bill """)
    bill = cursor.fetchall()
    for i in Table_bill.get_children():
        Table_bill.delete(i)
    for i, (Bill_id, Customer_id, DataPlan_id, Registration_date, Duration, total_amount) in enumerate(bill, start=1):
        Table_bill.insert("", "end",values=(Bill_id, Customer_id, DataPlan_id, Registration_date, Duration, total_amount))
    db.close()



def Write_Customer_Input():
    object = Bill.Bill()
    object.setBillInfor(idbill.get(), idcustomer.get(), iddata.get(), regdate.get(), drt.get(), ttl.get())

    billid = object.getBillInfo_Bill_id()
    customerid = object.getBillInfo_Bill_Customerid()
    dataplanid = object.getBillInfo_Bill_Dataplanid()

    if billid == "":
        messagebox.showinfo("Remove bill", "id of bill can't be empty!")
    elif customerid == "":
        messagebox.showinfo("Update bill", "id of customer can't be empty!")
    elif dataplanid == "":
        messagebox.showinfo("Search bill", "id of dataplan can't be empty!")
    else:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="internet_service_information_management_system"
        )
        cursor = db.cursor()
        try:
            cursor.execute("""SELECT * FROM Customer WHERE Customer_id = %s""", (customerid,))
            customerwrite = cursor.fetchone()
            cursor.execute("""SELECT * FROM dataPlan WHERE dataPlan_id = %s""", (dataplanid,))
            dataplanwrite = cursor.fetchone()
            cursor.execute("""SELECT * FROM Bill WHERE Customer_id=%s AND DataPlan_id=%s""", (customerid, dataplanid,))
            billwrite = cursor.fetchone()
            with open("information.txt", "x", encoding="utf-8") as f:
                f.write("------------------------------------------INTERNET PAYMENT REQUEST------------------------------------------\n")
                f.write("\n")
                f.write("*,Information of Customer: "+"\n")
                f.write("(id, name, phone number, address)"+"\n")
                f.write("\n")
                f.write("   %s" % (customerwrite, ) + "\n")
                f.write("\n")
                f.write("*,Dataplan information of Customer:"+"\n")
                f.write("(id,data plan you registered,speed,price per month(*1000VND):"+"\n")
                f.write("\n")
                f.write("   %s" % (dataplanwrite,) + "\n")
                f.write("\n")
                f.write("*,Bill information of Customer :"+"\n")
                f.write("(id bill, id customer, id dataplan, registration date, duration(month), total amount(*1000VND):"+"\n")
                f.write("\n")
                f.write("   %s" % (billwrite,)  + "\n")
                f.write("\n")
                f.write("\n")
                f.write("------------------------------------Please complete your payment in time!-----------------------------------" + "\n")
                f.write("-------------------------------------Thank you for choosing our service-------------------------------------"+ "\n")
                f.close()
            messagebox.showinfo("get bill ", "Success!")
        except:
            messagebox.showinfo("get bill ", "fail!")
    db.close()




#main
window = tk.Tk()
window.geometry("1530x800")
window.title("Internet Service Information Management System")
tk.Label(window, text="Internet Service Information Management System", font=("Times New Roman", 49),
         bg="#F1336E", fg="black").place(x=0, y=0, width=1560)
window.configure(background='#BBEDF2')
# CUSTOMER
tk.Label(window, text="Customer", font=("Times New Roman", 18),
         bg="#F1336E", fg="black").place(x=150, y=80, width=150)

tk.Label(window, text="ID", font=("Times New Roman", 14)).place(x=10, y=115, )
cusid = Entry(window, width=40)
cusid.place(x=10, y=135)

tk.Label(window, text="Name", font=("Times New Roman", 14)).place(x=10, y=160)
cusname = Entry(window, width=40)
cusname.place(x=10, y=180)

tk.Label(window, text="Phone", font=("Times New Roman", 14)).place(x=10, y=210)
numphone = Entry(window, width=40)
numphone.place(x=10, y=230)

tk.Label(window, text="Address", font=("Times New Roman", 14)).place(x=10, y=260)
adrs = Entry(window, width=40)
adrs.place(x=10, y=280)

tk.Label(window, text="ID to search", font=("Times New Roman", 14)).place(x=10, y=310)
searchcustomer = Entry(window, width=40)
searchcustomer.place(x=10, y=330)

tk.Button(window, text="ADD", command=lambda: [Add_Customer(),Insert_Table_Customer()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=350, y=120, width=100, height=40)

tk.Button(window, text="REMOVE", command=lambda:[Remove_Customer(),Insert_Table_Customer()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=350, y=190, width=100, height=40)

tk.Button(window, text="UPDATE", command=lambda: [Update_Customer(),Insert_Table_Customer()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=350, y=260, width=100, height=40)

tk.Button(window, text="SEARCH", command=lambda: [Search_Customer(),Insert_Table_Customer()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=350, y=330, width=100, height=40)

# DATAPLAN
tk.Label(window, text="Data Plan", font=("Times New Roman", 18),
         bg="#F1336E", fg="black").place(x=650, y=80, width=150)

tk.Label(window, text="Data ID", font=("Times New Roman", 14)).place(x=530, y=115, )
dataid = Entry(window, width=40)
dataid.place(x=530, y=135)

tk.Label(window, text="Data Name", font=("Times New Roman", 14)).place(x=530, y=160)
dataname = Entry(window, width=40)
dataname.place(x=530, y=180)

tk.Label(window, text="Speed", font=("Times New Roman", 14)).place(x=530, y=210)
dataspeed = Entry(window, width=40)
dataspeed.place(x=530, y=230)

tk.Label(window, text="Price (*1000 VND)", font=("Times New Roman", 14)).place(x=530, y=260)
price = Entry(window, width=40)
price.place(x=530, y=280)

tk.Label(window, text="ID to search", font=("Times New Roman", 14)).place(x=530, y=310)
searchdata = Entry(window, width=40)
searchdata.place(x=530, y=330)

tk.Button(window, text="ADD", command=lambda: [Add_Dataplan(),Insert_Table_dataPlan()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=840, y=120, width=100, height=40)

tk.Button(window, text="REMOVE", command=lambda: [Remove_Dataplan(),Insert_Table_dataPlan()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=840, y=190, width=100, height=40)

tk.Button(window, text="UPDATE", command=lambda: [Update_Dataplan(),Insert_Table_dataPlan()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=840, y=260, width=100, height=40)

tk.Button(window, text="SEARCH", command=lambda: [Search_Dataplan(),Insert_Table_dataPlan()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=840, y=330, width=100, height=40)

# BILL
tk.Label(window, text="Bill", font=("Times New Roman", 18),
         bg="#F1336E", fg="black").place(x=1200, y=80, width=150)

tk.Label(window, text="Bill ID", font=("Times New Roman", 12)).place(x=1100, y=110, )
idbill = Entry(window, width=40)
idbill.place(x=1100, y=130)

tk.Label(window, text="Customer ID", font=("Times New Roman", 12)).place(x=1100, y=150)
idcustomer = Entry(window, width=40)
idcustomer.place(x=1100, y=170)

tk.Label(window, text="Data ID", font=("Times New Roman", 12)).place(x=1100, y=190)
iddata = Entry(window, width=40)
iddata.place(x=1100, y=210)

tk.Label(window, text="Registration Date (YYYY-MM-DD)", font=("Times New Roman", 12)).place(x=1100, y=230)
regdate = Entry(window, width=40)
regdate.place(x=1100, y=250)

tk.Label(window, text="Duration (month)", font=("Times New Roman", 12)).place(x=1100, y=270)
drt = Entry(window, width=40)
drt.place(x=1100, y=290)

tk.Label(window, text="Total amount (*1000 VND)", font=("Times New Roman", 12)).place(x=1100, y=310)
ttl = Entry(window, width=40)
ttl.place(x=1100, y=330)

tk.Button(window, text="ADD", command=lambda: [Add_Bill(),Insert_Table_Bill()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=1400, y=120, width=100, height=40)

tk.Button(window, text="REMOVE", command=lambda: [Remove_Bill(),Insert_Table_Bill()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=1400, y=190, width=100, height=40)

tk.Button(window, text="UPDATE", command=lambda: [Update_Bill(),Insert_Table_Bill()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=1400, y=260, width=100, height=40)

tk.Button(window, text="SEARCH", command=lambda: [Search_Bill(),Insert_Table_Bill()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=1400, y=330, width=100, height=40)

tk.Button(window, text="CALCULATE AMOUNT", command=lambda: [Calculate_Total_Amount(),Insert_Table_Bill()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=1320, y=400, width=180, height=40)

tk.Button(window, text="GET BILL", command=lambda: [Write_Customer_Input()], font=("calibri bold", 14), bg="#F1336E", fg="white") \
    .place(x=1320, y=470, width=180, height=40)

# TABLE NAME

tk.Label(window, text="Customer", font=("Times New Roman", 21), bg="#DEEBF7", fg="#F1336E",
         anchor=tk.CENTER, width=13).place(x=0, y=385)
tk.Label(window, text="Data Plan", font=("Times New Roman", 21), bg="#DEEBF7", fg="#F1336E",
         anchor=tk.CENTER, width=13).place(x=0, y=514)
tk.Label(window, text="Bill", font=("Times New Roman", 21), bg="#DEEBF7", fg="#F1336E",
         anchor=tk.CENTER, width=13).place(x=0, y=643)


# TABLE
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", rowheight=25)
# CUSTOMER TABLE
tree_framecustomer = tk.Frame(window)
tree_framecustomer.pack(pady=20)
tree_scrollpro = tk.Scrollbar(tree_framecustomer)
tree_scrollpro.pack(side=tk.RIGHT, fill=tk.Y)

Table_customer = ttk.Treeview(tree_framecustomer, yscrollcommand=tree_scrollpro.set,
                              columns=("ID", "Name", "Phone", "Address"), show="headings", height=4)
Table_customer.column("ID", anchor=tk.CENTER, width=150)
Table_customer.column("Name", anchor=tk.W, width=400)
Table_customer.column("Phone", anchor=tk.CENTER, width=250)
Table_customer.column("Address", anchor=tk.CENTER, width=250)

Table_customer.heading("ID", text="ID", anchor=tk.CENTER)
Table_customer.heading("Name", text="Name", anchor=tk.CENTER)
Table_customer.heading("Phone", text="Phone", anchor=tk.CENTER)
Table_customer.heading("Address", text="Address", anchor=tk.CENTER)
Table_customer.pack()
tree_scrollpro.config(command=Table_customer.yview)
tree_framecustomer.place(x=200, y=385)

# DATA TABLE
tree_framedata = tk.Frame(window)
tree_framedata.pack(pady=20)
tree_scrollpro = tk.Scrollbar(tree_framedata)
tree_scrollpro.pack(side=tk.RIGHT, fill=tk.Y)

Table_dataplan = ttk.Treeview(tree_framedata, yscrollcommand=tree_scrollpro.set,
                              columns=("ID", "Name", "Speed", "Price"), show="headings", height=4)
Table_dataplan.column("ID", anchor=tk.CENTER, width=150)
Table_dataplan.column("Name", anchor=tk.W, width=400)
Table_dataplan.column("Speed", anchor=tk.CENTER, width=250)
Table_dataplan.column("Price", anchor=tk.CENTER, width=250)

Table_dataplan.heading("ID", text="ID", anchor=tk.CENTER)
Table_dataplan.heading("Name", text="Name", anchor=tk.CENTER)
Table_dataplan.heading("Speed", text="Speed", anchor=tk.CENTER)
Table_dataplan.heading("Price", text="Price", anchor=tk.CENTER)
Table_dataplan.pack()
tree_scrollpro.config(command=Table_dataplan.yview)
tree_framedata.place(x=200, y=514)

# BILL TABLE
tree_framebill = tk.Frame(window)
tree_framebill.pack(pady=20)
tree_scrollpro = tk.Scrollbar(tree_framebill)
tree_scrollpro.pack(side=tk.RIGHT, fill=tk.Y)

Table_bill = ttk.Treeview(tree_framebill, yscrollcommand=tree_scrollpro.set,
                          columns=("ID", "Customer ID", "Data ID", "Registration Date", "Duration", "Total"),
                          show="headings", height=4)
Table_bill.column("ID", anchor=tk.CENTER, width=115)
Table_bill.column("Customer ID", anchor=tk.W, width=190)
Table_bill.column("Data ID", anchor=tk.CENTER, width=190)
Table_bill.column("Registration Date", anchor=tk.CENTER, width=185)
Table_bill.column("Duration", anchor=tk.CENTER, width=185)
Table_bill.column("Total", anchor=tk.CENTER, width=185)

Table_bill.heading("ID", text="ID", anchor=tk.CENTER)
Table_bill.heading("Customer ID", text="Customer ID", anchor=tk.CENTER)
Table_bill.heading("Data ID", text="Data ID", anchor=tk.CENTER)
Table_bill.heading("Registration Date", text="Registration Date", anchor=tk.CENTER)
Table_bill.heading("Duration", text="Duration", anchor=tk.CENTER)
Table_bill.heading("Total", text="Total", anchor=tk.CENTER)
Table_bill.pack()
tree_scrollpro.config(command=Table_bill.yview)
tree_framebill.place(x=200, y=643)
Insert_Table_Customer()
Insert_Table_dataPlan()
Insert_Table_Bill()
window.mainloop()



