
import oracledb as orc
def pingenerate():
    try:
        connection = orc.connect("system/rroot@localhost/orcl")
        cour = connection.cursor()
        acno=int(input("ENTER YOUR ACCOUNT NUMBER :"))
        pin=int(input("GENERATE YOUR PIN :"))
        qry="update customers set pin=%d where acno=%d" %(pin,acno)
        cour.execute(qry)
        connection.commit()
        if cour.rowcount>0:
            print("PIN GENERATED SUCCESSFULLY !!!")
        else:
            print("Account not found")
    except orc.DatabaseError as db:
        print("DATABASE ERROR",db)
    except TypeError:
        print("Don't enter alfa numeric values")


def pinupdate():
    try:
        connection = orc.connect("system/rroot@localhost/orcl")
        cour = connection.cursor()
        acno = int(input("ENTER YOUR ACCOUNT NUMBER :"))
        pin = int(input("UPDATE YOUR PIN :"))
        qry = "update customers set pin=%d where acno=%d" % (pin, acno)
        cour.execute(qry)
        connection.commit()
        if cour.rowcount > 0:
            print("PIN UPDATED SUCCESSFULLY !!!")
        else:
            print("Account not found")
    except orc.DatabaseError as db:
        print("DATABASE ERROR", db)

    except TypeError:
        print("Don't enter alfa numeric values")

