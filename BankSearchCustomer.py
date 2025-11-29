import oracledb as ors
def searchcustomer():
    try:
        connection = ors.connect("system/rroot@localhost/orcl")
        cour = connection.cursor()
        acno = int(input("ENTER ACCOUNT NUMBER :"))
        quary = "select *from customers where acno=%d" % (acno)
        cour.execute(quary)
        connection.commit()
        print("-" * 100)
        res = cour.fetchone()
        print("*" * 100)
        if res:
            print("\n--- CUSTOMER DETAILS ---")
            print("Account No : {}".format(res[0]))
            print("PIN        : {}".format(res[1]))
            print("Name       : {}".format(res[2]))
            print("Bank Name  : {}".format(res[3]))
            print("Balance    : {}".format(res[4]))
            print("Open Date  : {}".format(res[5]))
        else:
            print("CUSTOMER NOT FOUND!")
    except ors.DatabaseError as db:
        print(db)
    except TypeError:
        print("Don't enter alfa numeric values")

