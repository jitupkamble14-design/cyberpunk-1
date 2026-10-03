isAccountCreated = False;
def Create_Account():
  isAccountCreated = True;
  global Ac_No,PIN,Balance,Ac_Holder_Name
  Ac_Holder_Name = (input("Enter your name : "))  
  Mo_No = int(input("Enter your mobile no. : "))  
  PIN = int(input("Set your account PIN : "))
  Balance = int(input("Enter how much money you have to deposit now : ")) 
  import random
  Ac_No = random.randint(100000, 999999)
  print("Your Account No. is:", Ac_No)
def Deposit_Money():
 global Ac_No,PIN,Balance,Ac_Holder_Name 
 Account_no = int(input("\nEnter your account no :"))
 pin = int(input("Enter your account PIN : "))
 if(isAccountCreated):
    if(pin == PIN and Account_no == Ac_No):    
        Deposit = int(input("Enter ammount for deposit: "))
        Balance = Balance + Deposit
        print("Now your bank balance is : ", Balance)
    else:
        print("Invalid PIN or Account Number or No account identified.")
 else:
    print("!No Account exist")
def Withdraw_Money():
 global Ac_No,PIN,Balance,Ac_Holder_Name
 Account_no = int(input("\nEnter your account no :"))
 pin = int(input("Enter your account PIN : "))
 if(isAccountCreated):
    if(pin == PIN and Account_no == Ac_No):
        Withdraw = int(input("Enter ammount for Withdraw: "))
        if (Withdraw <= Balance):
            Balance = Balance - Withdraw
            print("Successfuly withdraw the money now your bank balance is : ", Balance)
        else:
            print("You does not have enough money to withdraw.")
    else:
        print("Invalid PIN.")
 else:
    print("!No Account exist")
def Check_Balance():
 global Ac_No,PIN,Balance,Ac_Holder_Name
 Account_no = int(input("\nEnter your account no :"))
 pin = int(input("Enter your account PIN : "))
 if(isAccountCreated):
    if(pin == PIN and Account_no == Ac_No):
        print("Your account number is : ", Ac_No)
        print("Account holder name is : ", Ac_Holder_Name)
        print("Now your account balance : ", Balance)
 else:
    print("!No Account exist")  
def Exit_the_bank():
  print("\nThank you for visiting us.")
def main():
 while True:
  choice = int(input("\nEnter your choice : \n1. Creat Account \n2. Deposit Money \n3. Withdraw Money \n4. Show Balance \n5. Exit\n\n"))
  match choice:
   case 1:
     Create_Account();
   case 2:
     Deposit_Money();
   case 3:
     Withdraw_Money();
   case 4:
     Check_Balance();
   case 5:
     Exit_the_bank();
     break;
   case _:
     print("Invalid Choice.")
main()
