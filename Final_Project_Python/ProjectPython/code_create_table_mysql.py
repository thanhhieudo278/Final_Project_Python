import mysql.connector


def CreateDataBaseTableDataplan():
    # Open database connection
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="internet_service_information_management_system"
    )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Drop table if it already exist using execute() method
    cursor.execute("DROP TABLE IF EXISTS Dataplan")
    # Create table as per requirement
    cursor.execute("""
        CREATE TABLE Dataplan(
        dataPlan_id INT PRIMARY KEY,
        dataPlan_name VARCHAR(50),
        dataPlan_speed VARCHAR(50),
        dataPlan_price_per_month INT
        )""")





def CreateDataBaseTableBill():
    # Open database connection
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="internet_service_information_management_system"
    )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Drop table if it already exist using execute() method
    cursor.execute("DROP TABLE IF EXISTS Bill")
    # Create table as per requirement
    cursor.execute("""
        CREATE TABLE Bill(
        Bill_id INT PRIMARY KEY,
        Customer_id INT,
        DataPlan_id INT,
        Registration_date DATE,
        Duration INT,
        total_amount INT 
    )""")

def CreateDataBaseTableCustomer():
    # Open database connection
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="internet_service_information_management_system"
    )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Drop table if it already exist using execute() method
    cursor.execute("DROP TABLE IF EXISTS Customer")
    # Create table as per requirement
    cursor.execute("""
        CREATE TABLE Customer(
        Customer_id INT PRIMARY KEY,
        Customer_name VARCHAR(50),
        Customer_phoneNumber INT,
        Customer_address VARCHAR(100)
        )""")

CreateDataBaseTableCustomer()
CreateDataBaseTableDataplan()
CreateDataBaseTableBill()



