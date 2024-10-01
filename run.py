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
            add_expense(description, amount)

        elif choice == '2':
            show_budget_details(budget, expenses)

        elif choice == '3':
            print('Closing budget app, see you soon')
            break
        else: 
            print('Invalid choice, please try again')
main()