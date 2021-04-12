class Budget:
    """
    This is my Zuri Task Budget App
    Made by devs for devs
    """

    def __init__(self, food, clothing, entertainment):
        """
        These are the initializing parameters
        :param food:
        :param clothing:
        :param entertainment:
        """
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment

    def check_balance(self, category):
        if category.lower() == "food":
            return f"Your food budget is NGN {self.food}."
        elif category.lower() == "clothing":
            return f"Your clothing budget is NGN {self.clothing}."
        elif category.lower() == "entertainment":
            return f"Your entertainment budget is NGN {self.entertainment}."
        else:
            return "You can only check balance for food, clothing or entertainment"

    def deposit(self, category, amount):
        if category.lower() == "food":  # lower() is used in case the parameter is given without being case-sensitive
            self.food += amount
            return f"Your deposit of NGN {amount} to the food budget was successful. \
Your food budget is now NGN {self.food}."
        elif category.lower() == "clothing":
            self.clothing += amount
            return f"Your deposit of NGN {amount} to the clothing budget was successful. \
Your clothing budget is now NGN {self.clothing}."
        elif category.lower() == "entertainment":
            self.entertainment += amount
            return f"Your deposit of NGN {amount} to the entertainment budget was successful. \
Your entertainment budget is now NGN {self.entertainment}."
        else:
            return "You can only deposit into food, clothing or entertainment."

    def withdraw(self, category, amount):
        if category.lower() == "food":
            if amount <= self.food:  # To check for sufficient balance before making withdrawal
                self.food -= amount
                return f"Your withdrawal of NGN {amount} from the food budget was successful. \
Your food budget is now NGN {self.food}."
            else:
                return "Insufficient funds"
        elif category.lower() == "clothing":
            if amount <= self.clothing:
                self.clothing -= amount
                return f"Your withdrawal of NGN {amount} from the clothing budget was successful. \
Your clothing budget is now NGN {self.clothing}."
            else:
                return "Insufficient funds"
        elif category.lower() == "entertainment":
            if amount <= self.entertainment:
                self.entertainment -= amount
                return f"Your withdrawal of NGN {amount} from the entertainment budget was successful. \
Your entertainment budget is now NGN {self.entertainment}."
            else:
                return "Insufficient funds"
        else:
            return "You can only withdraw from food, clothing or entertainment."

    def transfer(self, source, destination, amount):
        available_params = ["food", "clothing", "entertainment"]  # for use in check user's input when method is called
        if (source.lower() in available_params) and (destination.lower() in available_params):
            withdraw_able = self.withdraw(source, amount)  # Check if withdrawal took place
            if withdraw_able == "Insufficient funds":  # the value it returns if withdrawal does not take place
                return "Unable to transfer. Insufficient funds"
            else:  # withdrawal must have taken place
                self.deposit(destination, amount)
                return f"Your transfer of NGN {amount} from {source} to {destination} was successful."
        else:  # if user's source or destination input is not in the budget created
            return "You can only transfer in between the available budgets: food, clothing, entertainment"


def int_input(prompt=""):
    """
    For use in place of input() if you want the user to keep retrying until an integer has \
been submitted.
    :param prompt: It has prompt attribute similar to the built-in input() function
    :return: It returns the integer value when the user has finally typed an integer
    """
    while True:
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            break
        else:
            print("Type in digits!")
    return value


def option_converter(prompt=""):
    """
    option_converter is for use in collection user option in integer and converting into the respective string needed \
for operation
    :param prompt: It collects prompt because it uses the int_input() function which requires a prompt
    :return: It returns teh respective string value needed for operation.
    """
    while True:
        option = int_input(prompt)
        if option == 1:
            option = "food"
            break
        elif option == 2:
            option = "clothing"
            break
        elif option == 3:
            option = "entertainment"
            break
        else:
            print("Not an option")
    return option


try:
    welcome_prompt = f"""
{"= ==" * 6}
This is Zuri Budget App
{"= ==" * 6}
You can close the app at any time with Ctrl + D
Please enter your budget as prompted below
"""
    action_prompt = f"""
What would you like to do? These are the available options:
1. Check balance
2. Deposit
3. Withdraw
4. Transfer

Type in the number behind your desired option
"""
    category_prompt = """
Which of the categories?
1. Food
2. Clothing
3. Entertainment

Type in the number behind your desired option
"""
    print(welcome_prompt)
    usr_food = int_input('How much is your budget for food?\t')
    usr_clothing = int_input('How much is your budget for clothing?\t')
    usr_entertainment = int_input('How much is your budget for entertainment?\t')
    budget = Budget(food=usr_food, clothing=usr_clothing, entertainment=usr_entertainment)
    print("\nHurray! Your budget has been created!")
    while True:
        action = int_input(action_prompt)
        if action == 1:
            usr_category = option_converter("CHECK BALANCE:" + category_prompt)
            print(budget.check_balance(usr_category))
        elif action == 2:
            usr_category = option_converter("DEPOSIT: " + category_prompt)
            usr_amount = int_input("How much would you like to deposit?\t")
            print(budget.deposit(usr_category, usr_amount))
        elif action == 3:
            usr_category = option_converter("WITHDRAWAL: " + category_prompt)
            usr_amount = int_input("How much would you like to withdraw?\t")
            print(budget.withdraw(usr_category, usr_amount))
        elif action == 4:
            usr_from = option_converter("FROM: " + category_prompt)
            usr_to = option_converter("TO: " + category_prompt)
            usr_amount = int_input("How much would you like to transfer?\t")
            print(budget.transfer(usr_from, usr_to, usr_amount))
        else:
            print("Not a valid option")

except EOFError:
    print("\nBudget App Closed. Bye!")
