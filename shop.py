from termcolor import colored


class InsufficientFundsError(Exception):
    pass


items = {"bread": 50, "chips": 80, "milk": 120}
customer_money = 100

print(colored('Welcome to our shop!', 'cyan'))
while True:
    print("Here are the available items:- ")
    for item, price in items.items():
        print(f"{item}: £{price}")
    print("Please type 'exit' to leave the shop.")

    try:
        choice = input("What would you like to buy?:- ")
        if choice == "exit":
            print("Goodbye!")
            break
        elif choice not in items:
            raise ValueError("Invalid choice!")
        elif customer_money >= items[choice]:
            print(f"Here's your {choice}!")
            customer_money -= items[choice]
        else:
            attempts = 0
            while attempts < 3:
                additional_money = input("You do not have enough money. Do you have more? If so, how much? Type 0 to exit. ")
                if additional_money == '0':
                    print("Goodbye!")
                    exit()
                additional_money = int(additional_money)
                customer_money += additional_money
                if customer_money >= items[choice]:
                    print(f"Here's your {choice}!")
                    customer_money -= items[choice]
                    break
                else:
                    attempts += 1
            else:
                raise InsufficientFundsError("You do not have enough money for this item. Goodbye!")
    except ValueError as ve:
        print(ve)
    except InsufficientFundsError as ife:
        print(ife)
        break
    else:
        print(f"You have £{customer_money} left.")`
