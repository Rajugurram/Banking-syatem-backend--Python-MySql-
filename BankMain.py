from BankAccountOpen import openaccount
from BankPinGenerateUpdate import pinupdate,pingenerate
from BankDeposit import deposit
from BankWithDraw import withdraw
from BankViewCustomers import viewcustomer,viewcustomers
from Menu import menu
from BankSearchCustomer import searchcustomer
from BankCloseAccount import accountclose


menu()
ch=int(input("ENTER YOUR CHOICE :"))
match(ch):
    case 1:
        openaccount()
    case 2:
        pingenerate()
    case 3:
        pinupdate()
    case 4:
        deposit()
    case 5:
        withdraw()
    case 6:
        searchcustomer()
    case 7:
        viewcustomer()
    case 8:
        viewcustomers()
    case 9:
        accountclose()
    case _:
        print("PLEASE SELECT FROM ABOVE OPTIONS")



