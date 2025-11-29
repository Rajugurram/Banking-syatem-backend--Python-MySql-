import oracledb as ors
def deposit():
    try:
        connection = ors.connect("system/rroot@localhost/orcl")
        cour = connection.cursor()
        acno=int(input("ENTER ACCOUNT NUMBER :"))
        dep=int(input("ENTER AN AMOUNT TOBE DEPOSIT :"))
        quary = "update customers set balance=balance+%d where acno=%d" %(dep,acno)
        cour.execute(quary)
        connection.commit()
        print("*"*50)
        print("\t{} is credited from your account".format(dep))
        print("*" * 50)
    except ors.DatabaseError as db:
        print(db)
    except TypeError:
        print("Don't enter alfa numeric values")
