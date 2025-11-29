import oracledb as ors
from datetime import datetime

def openaccount():
    while (True):
        try:
            connection = ors.connect("system/rroot@localhost/orcl")
            cour = connection.cursor()
            acno = int(input("ENTER ACCOUNT NO :"))
            pin="null"
            name = input("ENTER CUSTOMER NAME :")
            bname = input("ENTER BANK NAME :")
            balance=int(input("ENTER AN AMOUNT :"))
            dt = datetime.now()
            res = dt.strftime("%m/%d/%Y, %H:%M:%S")
            quary = "insert into customers values(%d,%s,'%s','%s',%d,'%s')" % (acno, pin, name, bname, balance, str(res))
            cour.execute(quary)
            connection.commit()
            print("RECORDS INSERTED SUCESSFULLY!!")
            ch=input("ADD ONE MORE RECORD yes/no =")
            if ch.lower()=="no":
                break


        except ors.DatabaseError as db:
            print("customer exist!!!", db)


