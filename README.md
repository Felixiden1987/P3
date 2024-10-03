# Budget Tracker App
This app is a great way of keeping track of your money. How much you have, and how much you have spent. 

You can start by adding a budget or add more to an existing budget (saved from last input).

You can add expenses and give it a category name like: Clothes, Groceries, Bills etc. 

You can choose to see your budget details such as: Total budget, expenses with categorys, total spent and the remaining budget. 

You can choose to add more income to the existing budget and see it calculated to your budget.

You can choose to delete all the values and start fresh with a new budget.

[Here is the live version of my project.](https://budget-tracker-app-44d16440587c.herokuapp.com/) 

![Responsice Mockup](https://github.com/Felixiden1987/P3/blob/main/images/Mockup.png)
## Features 

- The app starts by welcoming you to your budget app.
- Then the message: What would you like to do? 
- The user is given 5 options to choose from:
  
![Start](https://github.com/Felixiden1987/P3/blob/main/images/Startup.png)

- Let's say that the user want's to add an income to their budget by typing 4 and pressing Enter.
- Then adding 10000 to their budget that already had 10000 to begin with.
- Then it will look like this:

![](https://github.com/Felixiden1987/P3/blob/main/images/choice4after.png)

- Let's say that the user want's to add an expense, the user types 1 and presses Enter.
- Next step is to type what your expense description is and press Enter
- Now you can add the amount your expense had and press Enter

![choice 1](https://github.com/Felixiden1987/P3/blob/main/images/choice1.png)

- Let's say that the user want's to see their budget after adding an expense.
- The user will then type 2 and press Enter
- Now the user clearly see's what's left of the budget and how much is spent on what. 

![Show budget](https://github.com/Felixiden1987/P3/blob/main/images/19500.png)

- Let's say that the user want's to delete the budget with the expenses to start fresh.
- Then the user will type 3 and press Enter
- Now the user can enter the amount of their new budget and press Enter

![](https://github.com/Felixiden1987/P3/blob/main/images/choice3.png)

- Let's say that the user want's to see that their budget has been updated
- User types 2 and presses Enter
- And now the budget is 2500 with 0 spent.

![](https://github.com/Felixiden1987/P3/blob/main/images/choice2after.png)

- Let's say that the user want's to exit the app
- User types 5 and hits Enter
- A goodbye message is printed and it's shutting down

![](https://github.com/Felixiden1987/P3/blob/main/images/choice5.png)
## Future Features 
- A reset every month on payday (25th).
- A fixed income value that is logged in every month on the 25th. The user only needs to add expenses made. 

## Data Model

- 1: Key-value data model: The expenses are stored in a list of dictionaries, where each dictionary represents an expense with a description and an amount. 
- 2: Json data structure: The application makes use of JSON (JavaScript Object Notation) for saving and loading budget data to and from a file. The data structure that is saved to a JSON file consists of:

  - initial_budget: A float representing the total initial budget.
  - expenses: A list of expense dictionaries.
- 3: Summary, the data model utilized in this code is a list of dictionaries, leveraging a key-value data structure to represent expenses, and it utilizes JSON for persistent storage. The processing logic is predominantly procedural, focusing on functional operations to manage the budget. 
## Testing
I have manually tested this project by doing the following: 

- Passed the code through a PEP8 linter and confirmed there are no problems.
- Given invalid inputs, like strings where numbers are expected.
- Tested in my local terminal and in the Code Institute Heroku terminal. 

## Bugs 
### Solved bugs 
- When i deployed my app i got an error that it couldn't find my "budget_data.json" file, i changed it to a relative path and now it works.
### Unsolved bugs
- No bugs found.
## Validator testing 
- PEP8
  - No errors were returned from pep8ci.herokuapp.com
## Deployment 
- Steps for deployment
  - Create a new Heroku app.
  - Go to settings and set the var config to key: PORT and value: 8000.
  - Set the buildpacks to Python and NodeJS in that order.
  - Link the Heroku app to the Github repository.
  - Click on deploy.

## Credits
- Code Institute for the deployment terminal
- Youtube channel "Internet made coder" https://www.youtube.com/watch?v=4TZ1K8EHT2M for the basic setup code for the app. Iv'e then altered the code and added more functions like "add income to existing budget" & "Delete previous budget and start a new budget" 
