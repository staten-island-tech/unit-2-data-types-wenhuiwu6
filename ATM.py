balance= 500

while True :
    do_you=input("Do you want to withdraw? (type exit to quit or yes to continue): ")
    if do_you == 'exit': 
        break
    how_much= input("How much do you want to withdraw?: ")
    withdrawl = int(how_much)
    if withdrawl > balance:
        print("insufficient funds so try again")
    if withdrawl <= balance:
        new_balance = balance - withdrawl
        print(f"New balance: ${new_balance}")
    else:
        print("invalid")
