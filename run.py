import json

""" Borrowed code, see readme """


def add_expense(expenses, description, amount):
    expenses.append({'description': description, 'amount': amount})
    print(f'Added expense: {description} Amount: {amount}')


""" Borrowed code, see readme """


def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['amount']
    return sum


""" Borrowed code, see readme """


def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)


""" Borrowed code, see readme """


def show_budget_details(budget, expenses):
    print(f'Total Budget: {budget}')
    print('expenses:')
    for expense in expenses:
        print(f'- {expense['description']}: {expense['amount']}')
    print(f'Total Spent: {get_total_expenses(expenses)}')
    print(f'Remaining budget: {get_balance(budget, expenses)}')


""" Borrowed code, see readme """


def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['initial_budget'], data['expenses']
        """ Try to grab initial budget & expenses """
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []
        """ If file not found, return default values, 0 and empty list """


""" Borrowed code, see readme """


def save_budget_details(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }

    with open(filepath, 'w') as file:
        json.dump(data, file, )


def reset_expenses(expenses):
    expenses.clear()
    """ Resets all expenses to 0 """

    """ Borrowed but altered code in this last section, see readme """


def main():
    """ main function """
    print('Welcome to your budget app')
    """ Welcome message """
    filepath = 'budget_data.json'
    """ Defines the path to the json file """
    initial_budget, expenses = load_budget_data(filepath)
    budget = initial_budget

    while True:
        print('\nWhat would you like to do?')
        print('\n1. Add an expense')
        print('2. Show budget details')
        print('3. Delete previous budget & start a new budget')
        print('4. Add income to existing budget')
        print('5. Exit')
        choice = input('\nEnter your choice (1/2/3/4/5): ')

        if choice == '1':
            description = input('Enter expense description: ')
            try:
                """
                Wrapped the conversion of user inputs
                to float inside try blocks
                """
                amount = float(input('Enter expense amount: '))
                add_expense(expenses, description, amount)
            except ValueError:
                print("That's not a number, please try again.")
                """
                If the input cannot be converted to a float.
                Prints the message "That's not a number, please try again."
                """

        elif choice == '2':
            show_budget_details(budget, expenses)

        elif choice == '3':
            reset_expenses(expenses)
            try:
                """
                Wrapped the conversion of user inputs
                to float inside try blocks
                """
                initial_budget = float(input('Enter your initial budget: '))
                budget = initial_budget
                save_budget_details(filepath, initial_budget, expenses)
            except ValueError:
                print("That's not a number, please try again.")
                """
                If the input cannot be converted to a float.
                Prints the message "That's not a number, please try again."
                """

        elif choice == '4':
            try:
                """
                Wrapped the conversion of user inputs
                to float inside try blocks
                """
                additional_amount = float(input('Enter amount to new budget:'))
                budget += additional_amount
                initial_budget += additional_amount
                save_budget_details(filepath, initial_budget, expenses)
                print(f'Added {additional_amount}. New budget: {budget}')
            except ValueError:
                print("That's not a number, please try again.")
                """
                If the input cannot be converted to a float.
                Prints the message "That's not a number, please try again."
                """

        elif choice == '5':
            save_budget_details(filepath, initial_budget, expenses)
            print('Closing budget app, see you soon')
            break
        else:
            print('Invalid choice, please try again')
            """ If input is anything except numbers 1-5 """


main()
