import oracledb as ors

def withdraw():
    try:
        connection = ors.connect("system/rroot@localhost/orcl")
        cour = connection.cursor()
        acno=int(input("ENTER ACCOUNT NUMBER :"))
        wit=int(input("ENTER AN AMOUNT TOBE WITHDRAW :"))
        quary = "update customers set balance=balance-%d where acno=%d" %(wit,acno)

        cour.execute(quary)
        connection.commit()
        print("*"*50)
        print("\t{} is debeted from your account".format(wit))
        print("*" * 50)
    except ors.DatabaseError as db:
        print(db)
    except TypeError:
        print("Don't enter alfa numeric values")
