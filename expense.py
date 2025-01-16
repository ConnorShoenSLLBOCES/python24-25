def add_expens(expenses, category, amount):
    if category not in expenses:
        expenses[category] = []
    expenses[category].append(amount)
    return expenses

def get_total_expens(expenses):
    return sum(sum(amounts) for amounts in expenses.values())

def get_cat_sum(expenses):
    return {category: sum(amounts) for category, amounts in expenses.items()}

def diaplay_expen_rep(expenses):
    print ("\n--- Expense Report ---")
    category_sum = get_cat_sum(expenses)
    total_expens = get_total_expens(expenses)
    for category, total_expens in category_sum.items():
        print (f"{category}: ${total:.2f}")
    print (f"Total Expenses: ${total_expens:.2f}")

expenses = {}

while True:
    print ("##############################")
    print ("##                          ##")
    print ("##    My Expense Tracker    ##")
    print ("##                          ##")
    print ("##############################")
    print ("\n")
    print ("############ Menu ############")
    print ("\n\n")
    print ("1.) Add Expense")
    print ("################")
    print ("2.) View Total Expenses")
    print ("################")
    print ("3.) View Expense Report")
    print ("################")
    print ("4.) Quit\n")

    choice = input("Enter your choice: \n")

    if choice == "1":
        category = input ("Enter the expense category (ex: Food, Transport, Utilities, ect.): ")
        amount = float (input("Enter the expense ammount: "))
        expenses = add_expens(expenses, category, amount)
        print ("Expense added succesfully!")

    elif choice == "2":
        total = get_total_expens(expenses)
        print (f"Total expenses so far: ${total:.2f}")

    elif choice == "3":
        diaplay_expen_rep(expenses)

    elif choice == "4":
        break

    else:
        print ("Invalid Choice, try again, moron.")