import sqlite3
import random as r
class Bank:
    print("Welcome To The Bank")

    def __init__(self):
        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()
        # print("Sqlite3 Connected")

    def CreateAccount(self):
        self.c.execute("""create table if not exists Bank(
            account_name text,
            acc_num interger,
            balance interger

        )""")
        # self.c.execute("drop table Bank") 
        # if you want to delete the whole table then use this line yo
        n1 = input("Enter Your First Name Sir:- ").upper()
        n2 = input("Enter Your Second Name:- ").upper()
        
        if n1.isalpha() and not n1.isspace() and n2.isalpha() and not n2.isspace():
            name = n1+' '+n2
            num = r.randint(10000000,99999999)
            amount = 0
            self.c.execute("insert into Bank values(?,?,?)",(name,num,amount))
            print(f"Your {name} Account Got Created Successfully...!")
            print(f"Please Note Down Your Account Number {num}")
            self.con.commit()        
            self.c.execute("select * from Bank")
            print(self.c.fetchall())
            self.con.close()
        else:
            print("Enter Valid Name, Try Again....!")

           
    def Open_Account(self):
        a_num = int(input("Tell me Your Account Number:- "))
        check = True
        flag = False
        for a,b,c in self.c.execute("select * from Bank"):
            if b == a_num:
                check = False
                flag = True
                val = c
                na = a
                print("(d)-Deposit")
                print("(w)-Withdraw")
                print("(c)-Check Balance")
                ope = input("Enter any of the operation (c)/(d)/(w):- ")
        if flag and (ope =='d' and 'D'):
            dep = int(input("Enter the Amount to Deposit:- "))
            deposit = dep + val
            self.c.execute("update Bank set balance = ?  where acc_num = ? ",(deposit,a_num))
            self.con.commit()
            print(f"Ammount Deposited {dep} $, Available Balance is {deposit} $")
            self.c.execute("select * from Bank")
            print(self.c.fetchall())
            # self.con.close()
        if flag and (ope == 'w' or ope == 'W'):
            wit = int(input("Enter the Amount Withdraw:- "))
            if val > 0 and val >= wit:
                withdraw_bal = val - wit
                self.c.execute("Update Bank set balance = ? where acc_num = ?",(withdraw_bal,a_num))
                self.con.commit()
                print(f"Withdraw {wit} $ , done successfully...! Available balance {withdraw_bal}$" )
                self.c.execute("select * from Bank")
                print(self.c.fetchall())
                # self.con.close()
            else:    
                print("Low Balance")
        
        if flag and (ope == 'c' or ope =='c'):
            print(f"Hello {na}, Your Account Balance is {val} $")
        
        if check:
            print("Invalid Account Number..!")



bk = Bank()
print("(c).Create Account")
print("(o)-Open Account")
op = input("Enter Your choice (c)/(o):-")
if op == 'c' or op == 'c':
    bk.CreateAccount()
elif op == 'o' or op == 'o':
    bk.Open_Account()


