balance= 500

while True:
    withdrawal=input("How much do you want to withdraw? (type exit to quit): ")
    if withdrawal == 'exit': 
        break
    elif withdrawal>balance:
        print("insufficient funds so try again")
    elif withdrawal<=balance:
        new_balance = balance - withdrawal
        print(f"New balance: ${new_balance}")
    else:
        print("invalid")
