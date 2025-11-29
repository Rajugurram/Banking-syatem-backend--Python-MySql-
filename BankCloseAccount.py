
import oracledb as ors
def accountclose():
    try:
        connection = ors.connect("system/rroot@localhost/orcl")
        cour = connection.cursor()
        acno = int(input("ENTER ACCOUNT NUMBER :"))
        quary = "delete customers where acno=%d" % (acno)
        cour.execute(quary)
        connection.commit()
        print("customer removed successfully!!!")
    except ors.DatabaseError as db:
        print("Customer dose't fount",db)
    except ValueError:
        print("do not enter alnum values!!!")
