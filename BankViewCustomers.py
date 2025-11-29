
import  oracledb as orc

def viewcustomer():
    try:
        connection = orc.connect("system/rroot@localhost/orcl")
        cour = connection.cursor()
        qry = "select *from customers"
        cour.execute(qry)
        re=cour.description
        print("*" * 100)
        for val in re:

            print("\t",val[0],end="\t")
        print()
        print("*"*100)
        res=cour.fetchone()
        for i in res:
            print("\t",i,end="\t")
    except orc.DatabaseError as db:
        print()
    except TypeError:
        print("Don't enter alfa numeric values")

def viewcustomers():
    try:
        connection = orc.connect("system/rroot@localhost/orcl")
        cour = connection.cursor()
        qry = "select *from customers"
        cour.execute(qry)
        re = cour.description
        print("*" * 100)
        for val in re:
            print("\t", val[0], end="\t")
        print()
        print("*" * 100)
        res = cour.fetchall()
        for i in res:
            for res in i:
                print("\t", res, end="\t")
            print()
    except orc.DatabaseError as db:
        print("DATABASE ERROR",db)
    except TypeError:
        print("Don't enter alfa numeric values")
