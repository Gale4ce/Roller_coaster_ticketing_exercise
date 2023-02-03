Welcome_message = (input("Welcome to TBX bank, please enter you User ID"))

def User_Ian_Gale():
    Username = "Ian Gale"
    User_id = int(input())
    if User_id == int(12345):
        print (f"Hello {Username} please enter your pin")
    else:
        print("Wrong user ID, you have been logged out");
        exit(0)

    pin = int(input())
    if pin == int(7878):
        print("Please enter withdraw amount")
    else:
        print("Wrong pin, you have been logged out");
        exit(0)

    Withdraw_amount = int(input())
    if Withdraw_amount > int(500):
        print(f"Dear {Username} withdraw for {Withdraw_amount} is in progress\n")
    else:
        print("Invalid amount, you have been logged out");
        exit(0)

    opening_bal = int(1000000)
    closing_bal = opening_bal - Withdraw_amount
    print(f"Your current account balance is {closing_bal}")

    return
User_Ian_Gale()





