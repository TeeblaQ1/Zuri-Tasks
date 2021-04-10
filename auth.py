# ATM MOCKUP TASK (USING FUNCTIONS)
# The major improvement added is that code keeps running until the user chooses to exit and \
# Account Number always start with 22.
# Other improvement includes: checks if it is a digit before converting to an integer
# Option to register when at the login page
# Displays account number after login


# Import modules
import random
import datetime

# Create a dictionary database
database = {}

# Create Initialization Function
def startApp():
    print('''=========== ZuriBank ============
===== Made by Devs for Devs =====''')
    actions = '''
What would you like to do?
1. Already have an account? Type 1 to Login
2. Do not have an account? Type 2 to Register with us
3. Wanna exit the app? Type 3

Enter your input here: 
'''
    while True:
        userAction = input(actions)
        if userAction.isdigit():  # Checks if the user types in a digit before converting to integer to avoid errors
            userAction = int(userAction)

            if userAction == 1:
                login()
                break
            elif userAction == 2:
                register()
                break
            elif userAction == 3:
                exit()
            else:
                print("Invalid option selected")
                
        else:
            print("You're expected to type in a digit, please retry")

# Create Login Function
def login():
    greetings = '''
*************** Welcome Back *****************
********* Please proceed to Login ************
Do not have an account?
Type 'register' to create an eazyCoder account.
'''
    print(greetings)
    # userLogin is the account number from user
    # userPassword is the password from user
    while True:
        loginPrompt = 'Input your account number or type "register" to create an account \n'
        userLogin = input(loginPrompt)
        
        if userLogin.isdigit():
            userLogin = int(userLogin)
            for accountNumber, userDetails in database.items():
                if userLogin == accountNumber:
                    userPassword = input('Please enter your password \n')
                    if userPassword == userDetails[3]:
                        print('\nLogin Successful! \n')
                        bankOperation(accountNumber, userDetails)
                        break
                    else:
                        print('Invalid password')
                        
                else:
                    print('Invalid Account Number')

        elif userLogin.lower() == "register":  # Gives the user an option to register from the login page
            register()
            break
        
        else:
            print('Unrecognised user input')

# Create Register Function
def register():
    print('''
==== ==== ==== ====
Registration Portal
==== ==== ==== ====
''')
    email = input("Email Address:\t")
    firstName = input("First Name:\t")
    lastName = input("Last Name:\t")
    password = input("Password:\t")

    # Generate Account Number
    accountNumber = accountGenerator()

    # Update database with the details
    database[accountNumber] = [firstName, lastName, email, password]

    print(f'''
==== == ==== == ==== == ==== == ==== == ==== == ==== == ====
Your ZuriBank eazyCoder Account Has Been Created Successfully
==== == ==== == ==== == ==== == ==== == ==== == ==== == ====

Your Account Number is {accountNumber}
You'd need it for all your transactions. Keep it safe.
''')
    while True:
        userAction = input('Would you like to login? Type 1 to login or 2 to exit\n')
        if userAction.isdigit():
            userAction = int(userAction)
            if userAction == 1:
                login()
                break
            elif userAction == 2:
                exit()
            else:
                print('Invalid Option Selected')
                continue
        else:
            print('Type in a digit')
            continue
    

# Create BankOperations Function
def bankOperation(number, user):
    print(f'''===========================
Welcome, {user[0]} {user[1]}
===========================''')
    print(f'Account Number: {number}')
    e = datetime.datetime.now()
    print('===========================')
    print(e.strftime("Date: %a, %b %d, %Y\nTime: %H:%M:%S"))
    print('===========================')
    prompt = '''
These are the available options:
1. Withdrawal
2. Cash Deposit
3. Complaint
4. Logout
5. Exit

Please select an option (by typing the digit):\t
'''
    while True:
        userAction = input(prompt)
        if userAction.isdigit():
            userAction = int(userAction)
            
            if userAction == 1:
                withdrawal()
            elif userAction == 2:
                deposit()
            elif userAction == 3:
                complaint()
            elif userAction == 4:
                logout()
                break
            elif userAction == 5:
                exit()
            else:
                print("Invalid option selected, please select from 1 to 5\n")
                continue
        else:
            print("You're expected to type a digit")
            continue

# Create Logout Function
def logout():
    userAction = input('''You have been logged out succesfully!
Would you like to login? Type 1
Type any other key to exit
''')
    if userAction == '1':
        login()
    else:
        exit()

# Create withdrawal function
def withdrawal():
    while True:
        amount = input("How much would you like to withdraw? \n")
        if amount.isdigit():
            amount = int(amount)
            print("Take your cash")
            break
        else:
            print("Please type the amount in digits")

# Create deposit function
def deposit():
    current_balance = input("How much would you like to deposit? \n")
    if current_balance.isdigit():
        print("Deposit successful! Your current balance is %s" % current_balance)
    else:
        print("Please type the amount in digits")

# Create complaint function
def complaint():
    complaint = input("What issue will you like to report? \n")
    print("Thank you for contacting us!")

# Create Account Number Generator
def accountGenerator():
    # Account starts with 22 and is ten digits e.g. 22XXXXXXXX
    suffixNumber = random.randint(10000000, 99999999)
    numberSum = str(22) + str(suffixNumber)
    return int(numberSum)
    
startApp()
