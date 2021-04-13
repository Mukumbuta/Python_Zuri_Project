
import random

import sys

from datetime import datetime

account_details_container = {} 

def init():
    
    print("Welcome to MukuSimz Bank")

    already_has_account = int(input("Do you have an account with us? \n1. Login \n2. Register\n"))

    if already_has_account == 1:
        login()

    elif already_has_account == 2:
        register()
 
    else:
        print("You have selected an invalid option")
        init()

def register():
    print("<<< Please register >>>")

    first_name = input("Enter your first name: \n")
    last_name  = input("Enter your last name: \n")
    email      = input("Enter your email address: \n")
    password   = input("Create your password: \n")

    account_number = str(account_number_generator())

    account_details_container[account_number] = [ first_name, last_name, email, password ]  
    
    print("Congratulations " + first_name + " " + last_name)
    print("Your account has been created successfully.")
    print("Below are your login details. Please keep them safe.")
    print("<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Account number: {}".format(account_number)) 
    print("Password: " + password)
    print("<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>")


    
    login()   
                
def login():
    print("<<<>>> Please login <<<>>>") 
    
    login_attempt_counter = 0
    login_attempt_limit   = 3
    
    while login_attempt_counter < login_attempt_limit:
        entered_account_number = input("Enter your account number: \n")
        entered_password       = input("Enter your password: \n")
        login_attempt_counter += 1
        
        for account_number,account_password in account_details_container.items():
            if (entered_account_number in account_number):
                if (entered_password in account_password[3]):
                    print("login successful!")
                    perform_banking_operations()
                    break
        else:
            print("Account number or pasword not found. Please try again.")
    else:
        print("Too many attempts. Try again after some time.")
        
def account_number_generator():
    return random.randrange(1111111111,9999999999)
    
def perform_banking_operations():
    
    date_time = datetime.now()
    print(date_time)

    print("Welcome!")
    print("What kind of transaction would you like to do?\n")
    print("1. Withdrawal \n2. Cash deposit \n3. Complaint \n4. Logout \n5. Exit")
    
    selected_option = int(input("Select your option: \n"))

    if(selected_option == 1):
        withdraw_transaction()
    
    elif(selected_option == 2):
        deposit_transaction()
    
    elif(selected_option == 3):
        receive_complaint()

    elif(selected_option == 4):
        print("Log out successful")

        login()

    elif(selected_option == 5):
        
        exit_confirmation = int(input("Are you sure you want to Exit? \n1. YES \n2. NO\n"))

        if(exit_confirmation == 1):
            print("Thank you for banking with MukuSimz Bank")
            sys.exit()

        elif(exit_confirmation == 2):
            perform_banking_operations()

        else:
            print("You have selected an invalid opton")

    else:
        print("You have selected an invalid option.")

def withdraw_transaction():
    current_balance = 3650.75
    print("Current balance: ${}".format(current_balance))
    requested_amount = int(input("Enter an amount you would like to withdraw: \n"))

    if requested_amount < current_balance:
        print("Withdraw of ${} successful".format(requested_amount))
        
        appreciate_customer()
    else:
        print("Transaction failed. Can't withdraw more than current balance.")

        perform_banking_operations()
        
def deposit_transaction():
    current_balance = 3650.75
    deposit_amount = int(input("Enter the amount you would like to deposit: \n"))
    current_balance += deposit_amount
    print("Deposit of ${} successful".format(deposit_amount))
    print("Your current balance is now ${}".format(current_balance))

    appreciate_customer()
    
def receive_complaint():
    input("What issue will you like to report? \n")
    print("Thank you for your feedback. Your complaint has been forwarded to the technical team.")

def appreciate_customer():
    print("Thank you for choosing NAMX Bank")

        
init()