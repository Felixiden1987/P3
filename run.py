import json
def add_expense(expenses, description, amount):
    expenses.append({'description': description, 'amount': amount})
    print(f'Added expense: {description} Amount: {amount}')

def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['amount']
    return sum    

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f'Total Budget: {budget}')
    print('expenses:')
    for expense in expenses:
        print(f'- {expense['description']}: {expense['amount']}')
        print(f'Total Spent: {get_total_expenses(expenses)}')
        print(f'Remaining budget: {get_balance(budget, expenses)}')

def load_budget_data(filepath):
    try: 
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['initial_budget'], data['expenses']

    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []        
    """ If file not found, return default values, 0 and empty list """

def save_budget_details(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }

    with open(filepath, 'w') as file:
        json.dump(data, file, )

def reset_expenses(expenses):
    expenses.clear()
    """ Reset all expenses to 0 """

def main():
    """ main function """      
    print('Welcome to your budget app')
    """ Welcome message """
    
    filepath = '/workspaces/P3/budget_data.json'
    """ Defines the path to the json file """
    initial_budget, expenses = load_budget_data(filepath)
    budget = initial_budget
    
    while True: 
        """ While loop to run until we manually break out """
        print('\nWhat would you like to do?')
        print('\n1. Add an expense')
        print('2. Show budget details')
        print('3. Update/Clear previous budget')
        print('4. Exit')
        choice = input('\nEnter your choice (1/2/3/4): ')

        if choice == '1':
            description = input('Enter expense description: ')
            amount = float(input('Enter expense amount: '))
            """ Changes input from string to float """ 
            add_expense(expenses, description, amount)

        elif choice == '2':
            show_budget_details(budget, expenses)
            """ Shows budget details """
            
        elif choice == '3':
            reset_expenses(expenses)  
            """ Resets all expenses""" 
            initial_budget = float(input('Enter your initial budget: '))
            budget = initial_budget  
            """ Update the budget variable to reflect the new input """
            save_budget_details(filepath, initial_budget, expenses)  
            """ Save the updated budget and expenses """
            
        elif choice == '4':
            save_budget_details(filepath, initial_budget, expenses)
            print('Closing budget app, see you soon')
            break
            """ Closing the app """
        else: 
            print('Invalid choice, please try again')
            """ if input is something else then 1,2,3,4 """
main()