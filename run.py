def add_expense(expenses, description, amount):
    expenses.append({'description': description, 'amount': amount})
    print(f'Added expense: {description} Amount: {amount}')

def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['amount']
    return sum    

def show_budget_details(budget, expenses):
    print(f'Total Budget: {budget}')
    print('expenses:')
    for expense in expenses:
        print(f'- {expense['description']}: {expense['amount']}')
        print(f'Total Spent: {get_total_expenses(expenses)}')
        print(f'Remaining budget: ')
def main():
    """ main function """      
    print('Welcome to your budget app')
    """ Welcome message """
    initial_budget = float(input('Please enter your initial budget: '))
    """ Changes the input from string to float """
    budget = initial_budget
    expenses = []
    """ List of expenses provided by user """ 
    
    while True: 
        """ While loop to run until we manually break out """
        print('What would you like to do?')
        print('1. Add an expense')
        print('2. Show budget details')
        print('3. Exit')
        choice = input('Enter your choice (1/2/3): ')

        if choice == '1':
            description = input('Enter expense description: ')
            amount = float(input('Enter expense amount: '))
            """ Changes input from string to float """ 
            add_expense(expenses, description, amount)

        elif choice == '2':
            show_budget_details(budget, expenses)
            """ Shows budget details """
        elif choice == '3':
            print('Closing budget app, see you soon')
            break
            """ Closing the app """
        else: 
            print('Invalid choice, please try again')
            """ if input is something else then 1,2,3 """
main()