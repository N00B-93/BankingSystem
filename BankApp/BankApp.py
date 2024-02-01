import os  # Module used for interacting with the operating system
import os.path  # Module used for working with file and directory paths
from time import sleep  # Function used for adding delays in program execution
from sys import exit  # Function used to exit the program
# Library for securely inputting passwords without displaying them
from pwinput import pwinput
# Functions for serializing/deserializing Python objects
from pickle import load, dump
from random import randint  # Function used to generate random integers
from datetime import datetime  # Class for working with dates and times


class Account:
    """
    Represents a bank account.

    Attributes:
    - __accountName (str): Name of the account holder.
    - __balance (float): Current balance in the account.
    - __accountNumber (int): Unique account number.

    Methods:
    - __init__(accountName, balance, accountNumber): Initializes the Account instance.
    - getAccountName(): Retrieves the account holder's name.
    - getAccountNumber(): Retrieves the account number.
    - getAccountBalance(): Retrieves the current balance.
    - setAccountBalance(balance): Sets the account balance.
    """

    def __init__(self, accountName, balance, accountNumber):
        """
        Initializes an instance of the Account class.

        Args:
        - accountName (str): Name of the account holder.
        - balance (float): Current balance in the account.
        - accountNumber (int): Unique account number.
        """
        self.__accountName = accountName
        self.__balance = balance
        self.__accountNumber = accountNumber

    def getAccountName(self):
        """Returns the account holder's name."""
        return self.__accountName

    def getAccountNumber(self):
        """Returns the account number."""
        return self.__accountNumber

    def getAccountBalance(self):
        """Returns the current balance."""
        return self.__balance

    def setAccountBalance(self, balance):
        """
        Sets the account balance.

        Args:
        - balance (float): New balance to be set.
        """
        self.__balance = balance


class Customer:
    """
    Represents a bank customer.

    Attributes:
    - __username (str): Username of the customer.
    - __firstname (str): First name of the customer.
    - __lastname (str): Last name of the customer.
    - __fullname (str): Full name of the customer.
    - __age (int): Age of the customer.
    - __sex (str): Gender of the customer.
    - __address (str): Address of the customer.
    - __stateOfOrigin (str): State of origin of the customer.
    - __nationality (str): Nationality of the customer.
    - __occupation (str): Occupation of the customer.
    - __email (str): Email address of the customer.
    - __phoneNumber (str): Phone number of the customer.
    - __nameOfNextOfKin (str): Name of the customer's next of kin.
    - __addressOfNextOfKin (str): Address of the customer's next of kin.
    - __phoneNumberOfNextOfKin (str): Phone number of the customer's next of kin.
    - __account (Account): Instance of the Account class associated with the customer.

    Methods:
    - getCustomerName(): Returns the full name of the customer.
    - getCustomerFirstName(): Returns the first name of the customer.
    - getCustomerLastName(): Returns the last name of the customer.
    - getCustomerAge(): Returns the age of the customer.
    - getCustomerSex(): Returns the gender of the customer.
    - getCustomerStateOfOrigin(): Returns the state of origin of the customer.
    - getCustomerNationality(): Returns the nationality of the customer.
    - getCustomerOccupation(): Returns the occupation of the customer.
    - getCustomerEmail(): Returns the email address of the customer.
    - getCustomerPhoneNumber(): Returns the phone number of the customer.
    - getCustomerNameOfNextOfKin(): Returns the name of the customer's next of kin.
    - getCustomerAddressOfNextOfKin(): Returns the address of the customer's next of kin.
    - getCustomerPhoneNumberOfNextOfKin(): Returns the phone number of the customer's next of kin.
    - getAccountBalance(): Returns the account balance associated with the customer.
    - getAccountNumber(): Returns the account number associated with the customer.
    - getCustomerAddress(): Returns the address of the customer.
    - getCustomerUsername(): Returns the username of the customer.
    - __str__(): Returns a string representation of the customer's details.
    """

    def __init__(
            self,
            username,
            firstname,
            lastname,
            fullname,
            age,
            sex,
            address,
            stateOfOrigin,
            nationality,
            occupation,
            email,
            phoneNumber,
            nameOfNextOfKin,
            addressOfNextOfKin,
            phoneNumberOfNextOfKin,
            account
    ):
        """
        Initializes a Customer object.

        Parameters:
        - username (str): Username of the customer.
        - firstname (str): First name of the customer.
        - lastname (str): Last name of the customer.
        - fullname (str): Full name of the customer.
        - age (int): Age of the customer.
        - sex (str): Gender of the customer.
        - address (str): Address of the customer.
        - stateOfOrigin (str): State of origin of the customer.
        - nationality (str): Nationality of the customer.
        - occupation (str): Occupation of the customer.
        - email (str): Email address of the customer.
        - phoneNumber (str): Phone number of the customer.
        - nameOfNextOfKin (str): Name of the customer's next of kin.
        - addressOfNextOfKin (str): Address of the customer's next of kin.
        - phoneNumberOfNextOfKin (str): Phone number of the customer's next of kin.
        - account (Account): Account object associated with the customer.
        """
        self.__username = username  # Username of the customer
        self.__firstname = firstname  # First name of the customer
        self.__lastname = lastname  # Last name of the customer
        self.__fullname = fullname  # Full name of the customer
        self.__age = age  # Age of the customer
        self.__sex = sex  # Gender of the customer
        self.__address = address  # Address of the customer
        self.__stateOfOrigin = stateOfOrigin  # State of origin of the customer
        self.__nationality = nationality  # Nationality of the customer
        self.__occupation = occupation  # Occupation of the customer
        self.__email = email  # Email address of the customer
        self.__phoneNumber = phoneNumber  # Phone number of the customer
        self.__nameOfNextOfKin = nameOfNextOfKin  # Name of the customer's next of kin
        # Address of the customer's next of kin
        self.__addressOfNextOfKin = addressOfNextOfKin
        # Phone number of the customer's next of kin
        self.__phoneNumberOfNextOfKin = phoneNumberOfNextOfKin
        self.__account = account  # Account object associated with the customer

    def getCustomerName(self):
        """
        Retrieves the full name of the customer.

        Returns:
        - str: Full name of the customer.
        """
        return self.__fullname

    def getCustomerFirstName(self):
        """
        Retrieves the first name of the customer.

        Returns:
        - str: First name of the customer.
        """
        return self.__firstname

    def getCustomerLastName(self):
        """
        Retrieves the last name of the customer.

        Returns:
        - str: Last name of the customer.
        """
        return self.__lastname

    def getCustomerAge(self):
        """
        Retrieves the age of the customer.

        Returns:
        - int: Age of the customer.
        """
        return self.__age

    def getCustomerSex(self):
        """
        Retrieves the gender of the customer.

        Returns:
        - str: Gender of the customer.
        """
        return self.__sex

    def getCustomerStateOfOrigin(self):
        """
        Retrieves the state of origin of the customer.

        Returns:
        - str: State of origin of the customer.
        """
        return self.__stateOfOrigin

    def getCustomerNationality(self):
        """
        Retrieves the nationality of the customer.

        Returns:
        - str: Nationality of the customer.
        """
        return self.__nationality

    def getCustomerOccupation(self):
        """
        Retrieves the occupation of the customer.

        Returns:
        - str: Occupation of the customer.
        """
        return self.__occupation

    def getCustomerEmail(self):
        """
        Retrieves the email address of the customer.

        Returns:
        - str: Email address of the customer.
        """
        return self.__email

    def getCustomerPhoneNumber(self):
        """
        Retrieves the phone number of the customer.

        Returns:
        - str: Phone number of the customer.
        """
        return self.__phoneNumber

    def getCustomerNameOfNextOfKin(self):
        """
        Retrieves the name of the customer's next of kin.

        Returns:
        - str: Name of the customer's next of kin.
        """
        return self.__nameOfNextOfKin

    def getCustomerAddressOfNextOfKin(self):
        """
        Retrieves the address of the customer's next of kin.

        Returns:
        - str: Address of the customer's next of kin.
        """
        return self.__addressOfNextOfKin

    def getCustomerPhoneNumberOfNextOfKin(self):
        """
        Retrieves the phone number of the customer's next of kin.

        Returns:
        - str: Phone number of the customer's next of kin.
        """
        return self.__phoneNumberOfNextOfKin

    def getAccountBalance(self):
        """
        Retrieves the account balance of the customer.

        Returns:
        - float: Account balance of the customer.
        """
        return self.__account.getAccountBalance()

    def getAccountNumber(self):
        """
        Retrieves the account number of the customer.

        Returns:
        - str: Account number of the customer.
        """
        return self.__account.getAccountNumber()

    def getCustomerAddress(self):
        """
        Retrieves the address of the customer.

        Returns:
        - str: Address of the customer.
        """
        return self.__address

    def getCustomerUsername(self):
        """
        Retrieves the username of the customer.

        Returns:
        - str: Username of the customer.
        """
        return self.__username

    def __str__(self):
        """
        Returns a formatted string representation of the Customer object.

        Returns:
        - str: Formatted string including customer details like first name, last name,
                age, sex, state of origin, nationality, occupation, email, phone number,
                next of kin details, account balance, and account number.
        """
        return (
            f"\n\nFirst Name: {self.getCustomerFirstName()}\n\nLast Name: {self.getCustomerLastName()}\n\nFull Name: "
            f"{self.getCustomerName()}\n\nAge: {self.getCustomerAge()}\n\nSex: {self.getCustomerSex()}\n\nState Of "
            f"Origin:"
            f"{self.getCustomerStateOfOrigin()}\n\nNationality: {self.getCustomerNationality()}\n\nOccupation: "
            f"{self.getCustomerOccupation()}\n\nEmail: {self.getCustomerEmail()}\n\nPhone Number: "
            f"{self.getCustomerPhoneNumber()}\n\nNext Of Kin Full Name: "
            f"{self.getCustomerNameOfNextOfKin()}\n\nAddress Of Next Of Kin: "
            f"{self.getCustomerAddressOfNextOfKin()}\n\nNext Of Kin's Phone Number: "
            f"{self.getCustomerPhoneNumberOfNextOfKin()}\n\nAccount Balance: $ "
            f"{self.__account.getAccountBalance()}\n\nAccount Number: {self.__account.getAccountNumber()}"
        )

    def withdraw(self):
        """
        Facilitates the withdrawal process for the customer.
        Requests and validates the withdrawal amount, updates the account balance,
        generates a receipt, writes transaction details to a file, and updates the customer object file.

        Returns:
        - None
        """
        # Display the current account balance
        print(f"\nYour current balance is: $ {self.__account.getAccountBalance()}")

        # Prompt for the withdrawal amount
        amount = eval(input("\nEnter Amount to be withdrawn: $ "))

        # Variable used to control the number of times a user can try to withdraw funds
        tries = 0

        # Validate the withdrawal amount
        while True:
            if amount <= self.__account.getAccountBalance() and amount != 0:
                break
            elif self.__account.getAccountBalance() < amount or amount == 0:
                if tries == 2:
                    print("\nInsufficient Balance or Invalid amount.\nEnter a valid amount or Deposit cash then try again.", sep="")
                    exit(0)
                print("\nInvalid Amount, Try again.")
                amount = eval(input("\nEnter Amount to be withdrawn: $ "))
            tries += 1

        # Get transaction description from the user
        transactionDescription = input("\nEnter transaction description: ")

        bankCharges = deductBankCharges(amount)

        # Simulate transaction processing delay
        print(f"\nPlease wait while your transaction is processing...", end="")
        sleep(2)

        # Update the account balance after withdrawal
        self.__account.setAccountBalance(
            self.__account.getAccountBalance() - (amount + bankCharges))

        # Display a successful withdrawal message
        print(f"\n\n$ {amount} successfully withdrawn!")

        # Create transaction details for the receipt
        transactionDetails = {
            'Amount': amount,
            'Transaction Type': 'Withdrawal',
            'Description': transactionDescription,
            'Bank Charges': bankCharges
        }

        # Generate receipt and print it
        receipt = generateReceipt(**transactionDetails)
        print(receipt)

        # Write the receipt to a file with the username
        writeReceipt(receipt, self.__username + '.txt')

        # Update the customer object file
        with open(self.__username + '.dat', 'wb') as fileHandler:
            dump(self, fileHandler)

        return

    def deposit(self):
        """
        Allows the customer to deposit money into their account.

        Displays the current balance, prompts for the amount to be deposited, and processes the deposit transaction.
        Updates the account balance, generates a receipt, and writes transaction details to a file.

        Returns:
        - None
        """
        # Initializes the variable tries
        tries = 0

        # Display current balance
        print(f"\nYour current balance is: $ {self.__account.getAccountBalance()}")

        # while loop that check validates uesr input and terminates the program after three unsuccessful tries.
        while tries != 3:
            try:
                # Prompt for deposit amount
                amount = eval(input("\nEnter Amount to be deposited: $ "))
                # Checks if amount entered is 0.
                if amount == 0:
                    print("\nInvalid amount, You can deposit $ 0.0")
                elif amount > 0:
                    break
            except NameError:
                print("\nInvalid input, try again")
            except Exception:
                print("\nInvalid input, try again")
            tries += 1

        # Terminates the program if the user enters invalid input thrice.
        if tries == 3:
            print("\nYour account has been Temporarily suspended, Try again Later.")
            exit(0)

        # Prompt for transaction description
        transactionDescription = input("\nEnter transaction description: ")

        # Simulate processing delay
        print(f"\nPlease wait while your transaction is processing...", end="")
        sleep(2)

        # Update account balance after deposit
        self.__account.setAccountBalance(
            self.__account.getAccountBalance() + amount)

        # Display successful deposit message
        print(f"\n\n$ {amount} successfully deposited!")

        # Prepare transaction details for receipt
        transactionDetails = {
            'Amount': amount,
            'Transaction Type': 'Cash Deposit',
            'Transaction Description': transactionDescription}

        # Generate receipt
        receipt = generateReceipt(**transactionDetails)
        print(receipt)

        # Write receipt to file associated with the customer
        writeReceipt(receipt, self.__username + '.txt')

        # Update customer data in a file
        with open(self.__username + '.dat', 'wb') as fileHandler:
            dump(self, fileHandler)

        return

    def onlineTransfer(self):
        """
        Facilitates an online transfer of funds to another user account.

        Initiates a transfer process by verifying the recipient's existence and validating available funds.
        Transfers the specified amount between accounts, generates receipts, and updates transaction details in files.

        Returns:
        - None
        """

        # Display current balance
        print(
            f"\nYour current balance is ${self.__account.getAccountBalance()}")

        # Prompt for recipient username
        recipientName = input("\nEnter recipient username: ")

        tries = 0
        # Try to find recipient in the system
        while tries < 3:
            if recipientName == self.__username:
                print(f"Invalid request. Can't send to self.")
                recipientName = input("\nEnter a valid recipient username: ")
                if tries == 2:
                    print("\nWe are sorry, can't send to self. Bye...")
                    exit(0)
            elif os.path.isfile(recipientName + '.dat'):
                break
            else:
                print(f"\nUser {recipientName} not found")
                recipientName = input("\nEnter a valid recipient username: ")
            tries += 1

            if tries == 3:
                print("\nUser not found, please provide a valid recipient username.")
                exit(0)

        # Load recipient's account information
        fileHandler = open(recipientName + '.dat', 'rb')
        recipient = load(fileHandler)
        fileHandler.close()

        # Prompt for transfer amount
        amount = eval(input("\nEnter amount to be transferred: $ "))

        tries = 0
        # Check for available funds
        while tries < 3:
            if self.__account.getAccountBalance() > amount:
                break
            print("\nInsufficient funds!")
            amount = eval(input("\nEnter amount to be transferred: $ "))
            tries += 1

            if tries == 3:
                print("\nInsufficient funds, Recharge your account and try again!")
                exit(0)

        # Prompt for transaction description
        transactionDescription = input("\nEnter Transaction Description: ")

        bankCharges = deductBankCharges(amount)

        # Simulate processing delay
        print(f"\nPlease wait while your transaction is processing...", end="")
        sleep(2)

        # Update recipient and sender account balances
        recipient.__account.setAccountBalance(
            amount + recipient.__account.getAccountBalance())
        self.__account.setAccountBalance(
            self.__account.getAccountBalance() - (amount + bankCharges))

        # Update sender's account information in a file
        with open(self.__username + '.dat', 'wb') as fileHandler:
            dump(self, fileHandler)

        # Update recipient's account information in a file
        with open(recipient.__username + '.dat', 'wb') as fileHandler:
            dump(recipient, fileHandler)

        # Prepare transaction details for receipt
        # transactionDetails = {
        #     'Amount': amount,
        #     'Transaction Type': 'Online Transfer',
        #     'Transaction Description': transactionDescription}

        # Generate and print receipt for sender
        transactionDetails = {
            'Amount': amount,
            'Transaction Type': 'Online Transfer - Debit',
            'Transaction Description': transactionDescription,
            'Bank Charges': bankCharges
        }
        receipt = generateReceipt(**transactionDetails)
        print(receipt)

        # Write receipt to sender's file
        writeReceipt(receipt, self.__username + '.txt')

        # Generate receipt for receiver
        transactionDetails = {
            'Amount': amount,
            'Transaction Type': 'Online Transfer - Credit',
            'Transaction Description': transactionDescription
        }
        receipt = generateReceipt(**transactionDetails)

        # Write receipt to recipient's file
        writeReceipt(receipt, recipientName + '.txt')

        return

    def buyAirtime(self):
        """
        Initiates the purchase of airtime for a selected mobile network.

        Displays current account balance, prompts the user to select a network, and specifies the amount to be
        purchased.
        Validates the amount against the available balance and prompts for the phone number.
        Deducts the
        purchased amount from the account balance, generates a receipt, and updates account information.

        Returns:
        - None
        """
        # Display current balance
        print(f"\nYour current balance is: ${self.__account.getAccountBalance()}")

        # Display network options
        print("\n1. MTN\t\t\t2. AIRTEL\t\t\t3. GLO")
        network = ''
        choice = input("\nSelect Network: ")

        # Validate network choice
        while choice not in ['1', '2', '3']:
            print("\nInvalid choice!")
            choice = input("\nSelect Network: ")

        # Assign network based on user choice
        match choice:
            case '1':
                network = 'MTN'
            case '2':
                network = 'AIRTEL'
            case '3':
                network = 'GLO'

        # Variable used to tracks the number of times a customer tries to purcahse airtime.
        tries = 0

        # Validate amount against account balance
        while True:
            try:
                # Prompt for the amount to be purchased
                amount = float(input("\nEnter Amount to be purchased: $ "))
                if tries == 2:
                    print("\nYour Account has been temporarily suspended, Try again later.")
                    exit(0)
                if amount > self.__account.getAccountBalance() or amount == 0.0:
                    print("\nInvalid Amount, Try again.")
                else:
                    break
            except ValueError:
                if tries == 2:
                    print("\nYour Account has been temporarily suspended, Try again later.")
                    exit(0)
                print("\nInvalid amount, Try again.")
            tries += 1
                
        # Prompt for phone number
        phoneNumber = input("\nEnter Phone Number: ")

        # Simulate processing delay
        print(f"\nPlease wait while your transaction is processing...", end="")
        sleep(2)

        bankCharges = deductBankCharges(amount)

        # Deduct the purchased amount from the account balance
        self.__account.setAccountBalance(
            self.__account.getAccountBalance() - (amount + bankCharges))

        # Display a successful purchase message
        print(f"\n\n$ {amount} airtime successfully purchased!")

        # Prepare transaction details for receipt
        transactionDetails = {
            'Amount': amount,
            'Transaction Type': 'Airtime Purchase',
            'Network': network,
            'Phone Number': phoneNumber,
            'Bank Charges': bankCharges
        }

        # Generate receipt
        receipt = generateReceipt(**transactionDetails)
        print(f"\n{receipt}")

        # Write receipt to user's file
        writeReceipt(receipt, self.__username + '.txt')

        # Update user's account information in a file
        with open(self.__username + '.dat', 'wb') as fileHandler:
            dump(self, fileHandler)

        return

    def printTransactionHistory(self):
        """
            Retrieves and displays the transaction history for the customer.

            Delays for 3 seconds to simulate the retrieval process.
            Retrieve the transaction history file based on the customer's username.
            Print the retrieved transaction history.

            Returns:
            - None
            """
        # Indicate that the script is retrieving transaction history
        print("\nRetrieving Transaction History...", end="")
        # Pause execution for 3 seconds to simulate retrieval time
        sleep(3)

        # Construct the path to the directory holding transaction details
        transactionDetailsDirectoryPath = os.path.join(
            os.getcwd(), "Customers_Transaction_Details")

        # Retrieve the username of the current customer
        transactionDetailsFileName = self.getCustomerUsername() + '.txt'

        # Combine a directory path and filename to create the file's complete
        # path
        transactionDetailsFilePath = os.path.join(
            transactionDetailsDirectoryPath, transactionDetailsFileName)

        # Read and display the contents of the transaction history file
        with open(transactionDetailsFilePath, 'r') as fileHandler:
            transactionHistory = fileHandler.read()
            print(transactionHistory)

        return

    def closeAccount(self, password):
        """
        Closes the customer's account permanently.

        Args:
        - password (str): The password to authenticate the account closure.

        Returns:
        - None

        This method prompts the user to confirm the account closure, removing associated
        files and updating credentials if confirmed. It cannot be undone.

        Steps:
        1. Ask the user for confirmation to close the account.
        2. If confirmed ('y'), delete the customer's data file ('<username>.dat').
        3. Removes the transaction history file associated with the account.
        4. Updates the list of usernames and passwords after removing the current user's credentials.
        5. Notifies the user of the successful account closure.
        """
        choice = input(
            "\nAre you sure you want to close your account?\n"
            "Account closure cannot be UNDONE! Type 'y' for yes or 'n' for no: ")
        if choice == 'n':
            return

        print("\nClosing your account...", end="")
        sleep(3)

        # Removing the customer's data file
        os.remove(self.__username + '.dat')

        # Removing the transaction history file associated with the account
        transactionDetailsDirectoryPath = os.path.join(
            os.getcwd(), "Customers_Transaction_Details")
        transactionDetailsFileName = self.getCustomerUsername() + '.txt'
        transactionDetailsFilePath = os.path.join(
            transactionDetailsDirectoryPath, transactionDetailsFileName)
        os.remove(transactionDetailsFilePath)

        # Updating the list of usernames and passwords
        fileHandler = open('usernames.txt')
        usernames = fileHandler.readlines()
        fileHandler.close()

        if (self.__username + '\n') in usernames:
            with open('usernames.txt', 'w') as fileHandler:
                # Removes the current username from the list of usernames
                usernames.remove(self.__username + '\n')
                [fileHandler.write(username) for username in usernames]

            fileHandler = open('passwords.txt')
            passwords = fileHandler.readlines()
            fileHandler.close()

            if (password + '\n') in passwords:
                with open('passwords.txt', 'w') as fileHandler:
                    # Removes the current password from the list of passwords
                    passwords.remove(password + '\n')
                    [fileHandler.write(password) for password in passwords]

        print("\n\nAccount has been successfully closed!")

        return

    def checkBalance(self):
        """
        Retrieves and displays the customer's current available balance.
        """
        print("\nRetrieving your current available balance...", end="")
        sleep(3)

        # Retrieves and prints the current balance
        print(f"\n\nYour current balance is ${self.__account.getAccountBalance()}")

        return


def deductBankCharges(amount):
    """
    Generates the bank's charges for a particular amount of money.
    Args:
        - amount: The amount to be transferred or withdrawn

    Returns:
        -int: The bank's charges for a particular amount of money'.
    """
    if amount < 5000:
        return 10.00
    elif 5001 <= amount <= 50000:
        return 26.00
    else:
        return 50.00


def generateReceipt(**kwargs):
    """
    Generates a transaction receipt based on the provided keyword arguments.

    Args:
    - **kwargs: Variable keyword arguments representing transaction details.

    Returns:
    - str: Transaction receipt string formatted with the provided transaction details.
    """

    # Capturing the current date and time
    now = datetime.now()

    # Convert the keyword arguments into a list of key-value pairs
    kwargs = list(kwargs.items())

    # Constructing the receipt based on the number of transaction details
    # provided
    if len(kwargs) == 3:  # For a simple receipt with three details
        return (
            f"\n***************************Transaction Receipt**************************\n"
            f"\t\t{kwargs[1][0]}: {kwargs[1][1]}\n"  # Detail 1
            f"\n\t\t{kwargs[2][0]}: {kwargs[2][1]}\n"  # Detail 2
            f"\n\t\t{kwargs[0][0]}: $ {kwargs[0][1]}\n"  # Detail 3 (amount)
            f"\n\t\tStatus: Successful\n"  # Transaction status
            # Date and time stamp
            f"\n\t\tDate: {now.strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"**************************************************************************\n"
        )
    elif len(kwargs) == 4:
        return (
            f"\n***************************Transaction Receipt**************************\n"
            f"\t\t{kwargs[1][0]}: {kwargs[1][1]}\n"  # Detail 1
            f"\n\t\t{kwargs[2][0]}: {kwargs[2][1]}\n"  # Detail 2
            f"\n\t\t{kwargs[0][0]}: $ {kwargs[0][1]}\n"  # Detail 3 (amount)
            f"\n\t\t{kwargs[3][0]}: $ {kwargs[3][1]}\n"
            f"\n\t\tStatus: Successful\n"  # Transaction status
            # Date and time stamp
            f"\n\t\tDate: {now.strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"**************************************************************************\n"
        )
    return (
        f"\n***************************Transaction Receipt**************************\n"
        f"\t\t{kwargs[1][0]}: {kwargs[1][1]}\n"  # Detail 1
        f"\n\t\t{kwargs[2][0]}: {kwargs[2][1]}\n"  # Detail 2
        f"\n\t\t{kwargs[0][0]}: $ {kwargs[0][1]}\n"  # Detail 3 (amount)
        f"\n\t\t{kwargs[3][0]}: {kwargs[3][1]}\n"  # Detail 4
        f"\n\t\t{kwargs[4][0]}: $ {kwargs[4][1]}\n"  # Detail 5
        f"\n\t\tStatus: Successful\n"  # Transaction status
        # Date and time stamp
        f"\n\t\tDate: {now.strftime('%d/%m/%Y %H:%M:%S')}\n"
        f"**************************************************************************\n"
    )


def openAccount():
    """
    Facilitates the creation of a new customer account in the bank system.

    Prompts the user for personal information, login credentials, and create a new customer account.

    Returns:
    None
    """

    print("\n\n\t\tWelcome to N00B'S BANK")
    print("\t\t(The One Customer Bank!)")

    response = input(
        "\nAre you 16 years old or above? ('y' for yes, 'n' for no): ")

    # Check user's age eligibility to open an account
    if response == 'n':
        print("\nYou can't open an Account if you're less than 16 years old!\n")
        exit(0)
    elif response != 'y':
        print("\nInvalid Input, Enter a valid Response.")
        exit(0)

    print("\t\t\n\nLogin Credentials")
    username = input("\nUsername: ")

    password = pwinput("\nPassword: ", '*')

    passwordCheck = pwinput("\nConfirm Password: ", '*')

    # Ensure the password matches the confirmation before proceeding
    while password != passwordCheck:
        password = pwinput("\nPassword: ", '*')
        passwordCheck = pwinput("Confirm Password: ", '*')

        if passwordCheck == password:
            break
        print("Password Mismatch!, Try again.")

    # Write username and password to their respective files
    if not os.path.isfile('usernames.txt'):
        fileHandler1 = open('usernames.txt', 'w')
        fileHandler1.write(username + "\n")
        fileHandler1.close()
    else:
        with open("usernames.txt", 'a') as fileHandler1:
            fileHandler1.write(username + '\n')

    if not os.path.isfile('passwords.txt'):
        fileHandler1 = open('passwords.txt', 'w')
        fileHandler1.write(password + "\n")
        fileHandler1.close()
    else:
        with open("passwords.txt", 'a') as fileHandler1:
            fileHandler1.write(password + '\n')

    print("\n\t\tPersonal Information")
    print("\nKindly fill the following fields with the correct details.")

    # Collect personal information from the user
    firstname = input("\nFirst Name: ")
    lastname = input("\nLast Name: ")
    fullname = lastname + ' ' + firstname
    age = input("\nAge: ")
    sex = input("\nSex: ")
    address = input("\nAddress: ")
    stateOfOrigin = input("\nState Of Origin: ")
    nationality = input("\nNationality: ")
    occupation = input("\nOccupation: ")
    email = input("\nEmail: ")
    phoneNumber = input("\nPhone Number: ")
    nameOfNextOfKin = input("\nNext Of Kin's Full Name: ")
    addressOfNextOfKin = input("\nNext Of Kin's Address: ")
    phoneNumberOfNextOfKin = input("\nNext Of Kin's Phone Number: ")

    # Generate an account number and create a new account for the customer
    accountNumber = randint(1000000000, 9999999999)
    account = Account(fullname, 0.0, accountNumber)

    # Create a Customer instance with provided details
    customer = Customer(
        username,
        firstname,
        lastname,
        fullname,
        age,
        sex,
        address,
        stateOfOrigin,
        nationality,
        occupation,
        email,
        phoneNumber,
        nameOfNextOfKin,
        addressOfNextOfKin,
        phoneNumberOfNextOfKin,
        account)

    # Create a directory to store transaction details if it doesn't exist
    transactionDetailsDirectoryPath = os.path.join(
        os.getcwd(), "Customers_Transaction_Details")
    if not os.path.isdir(transactionDetailsDirectoryPath):
        os.mkdir(transactionDetailsDirectoryPath, 0o777)

    # Store the customer object and initialize an empty transaction file
    with open(username + ".dat", 'wb') as fileHandler:
        dump(customer, fileHandler)

    transactionDetailsFileName = username + '.txt'

    transactionDetailsFilePath = os.path.join(
        transactionDetailsDirectoryPath,
        transactionDetailsFileName)
    with open(transactionDetailsFilePath, 'w') as fileHandler:
        pass

    print(f"\n\t\tCongrats {customer.getCustomerName()}\n\t\tYour Account has been created successfully!\n")

    print("\nRedirecting to the login page...", end='')
    sleep(3)
    return


def login():
    """
    Allows existing users to log in to their accounts by providing credentials.

    Prompts the user for their username and password to authenticate and grant access.

    Returns:
    tuple: A tuple containing the username and password if the login is successful.
    """
    print("\n\n\t\tLogin to your Account.")
    tries = 0

    username = input("\nUsername: ")

    password = pwinput("\nPassword: ", '*')

    try:
    # Read usernames and passwords from their respective files
        fileHandler1 = open("usernames.txt")
        usernames = fileHandler1.readlines()

        fileHandler2 = open("passwords.txt")
        passwords = fileHandler2.readlines()
    except IOError:
        print("\nLogin details not Found!\nEnsure Your login Credentials are correct or Open an Account.")
        exit(0)

    while True:
        # Validate user credentials
        if (username + '\n') in usernames and (password + '\n') in passwords:
            print("\nLogging in...", end="")
            sleep(2)
            print("\n\nLogged in Successfully!")
            print("\nRedirecting to main menu...", end="")
            sleep(3)
            fileHandler1.close()
            fileHandler2.close()
            return username, password
        else:
            tries += 1

            # Handle login attempts limit
            if tries == 3:
                print("\nYour Account has been Temporarily Suspended!")
                exit(0)

            print("\nTry again, Invalid username or password!")
            username = input("\nUsername: ")
            password = pwinput("\nPassword: ", '*')


def writeReceipt(receipt, fileName):
    """
    Writes the receipt details to a specified file in the transaction details directory.

    Args:
    receipt (str): The transaction receipt to be written to the file.
    fileName (str): The name of the file to which the receipt will be written.

    Returns:
    None
    """

    # Define the file path where the receipt will be stored
    transactionDetailsDirectoryPath = os.path.join(
        os.getcwd(), "Customers_Transaction_Details")
    transactionDetailsFilePath = os.path.join(
        transactionDetailsDirectoryPath, fileName)

    # Write the receipt to the specified file
    with open(transactionDetailsFilePath, 'a') as fileHandler:
        fileHandler.write(receipt)


def main():
    print("\n\n\t\tWelcome to N00B'S BANK")
    print("\t\t(The One Customer Bank!)")

    password = user = ''  # Initializing password and user variables

    # Prompts the user to select a choice.
    print("\n1. Login\n2. Open Account\n3. Exit", sep="")
    option = input("\nSelect an option: ")  # User input for choice selection

    # Loop that validates user input.
    while True:
        if option in ['1', '2', '3']:
            break  # Breaks loop if the entered option is valid
        # Re-prompt if input is invalid
        option = input("\nInvalid Input!\nSelect an option from 1-3: ")

    if option == '1':  # Case when user selects Login
        user, password = login()  # Invokes the login function to authenticate the user
    elif option == '2':  # Case when user selects Open Account
        openAccount()  # Invokes function to open a new bank account
        print('\n')
        user, password = login()  # Logs in the user after account creation
    elif option == '3':  # Case when user selects Exit
        print("\nExiting...", end="")
        sleep(3)
        # os.system('clear')
        exit(0)  # Exits the program

    # Opens the user's data file and loads their customer object
    fileHandler = open(user + '.dat', 'rb')
    customer = load(fileHandler)
    fileHandler.close()

    # Welcomes the user by their name
    print(f"\n\n\t\tWelcome {customer.getCustomerName()}")

    while True:  # Main menu loop
        print("\nMain Menu")

        print(
            '\n1. Deposit Funds\n2. Withdraw Funds\n3. Online Transfer\n4. Buy Airtime\n5. Print Account Details\n6. '
            'Check Balance\n7. Print Transaction History\n8. Close Account\n9. Exit')

        option = input("\nEnter a choice: ")  # User input for selected action

        while True:  # Loop to validate a selected option
            if option in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                break  # Breaks the loop if the selected option is valid
            # Re-prompt if input is invalid
            option = input("\nInvalid Input!\nSelect an option from 1-9: ")

        match option:
            case '1':
                # Calls the deposit method to add funds to the account
                customer.deposit()
                # Asks the user if they want to perform another transaction or
                # log off
                choice = input(
                    "\nWould you like to perform another transaction? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue  # Continues to the main menu loop for another action
                else:
                    print("\nLogging off...", end="")
                    sleep(3)
                    exit(0)  # Exits the program

            case '2':
                # Calls the Withdraw method to take funds out of the account
                customer.withdraw()
                # Asks the user if they want to perform another transaction or
                # log off
                choice = input(
                    "\nWould you like to perform another transaction? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue  # Continues to the main menu loop for another action
                else:
                    print("\nLogging off...", end="")
                    sleep(3)
                    exit(0)  # Exits the program
                    # ...

            case '3':
                # Initiates an online transfer process
                customer.onlineTransfer()
                # Asks the user if they want to perform another transaction
                # or log off
                choice = input(
                    "\nWould you like to perform another transaction? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue  # Continues to the main menu loop for another action
                else:
                    print("\nLogging off...", end="")
                    sleep(3)
                    exit(0)  # Exits the program

            case '4':
                # Allows the customer to buy airtime
                customer.buyAirtime()
                # Asks the user if they want to perform another transaction or
                # log off
                choice = input(
                    "\nWould you like to perform another transaction? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue  # Continues to the main menu loop for another action
                else:
                    print("\nLogging off...", end="")
                    sleep(3)
                    exit(0)  # Exits the program
            case '5':
                # Displays the customer's account details
                print("\nFetching account Information...", end="")
                sleep(3)
                print(customer.__str__())
                # Asks the user if they want to perform another transaction or
                # log off
                choice = input(
                    "\nWould you like to perform another transaction? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue  # Continues to the main menu loop for another action
                else:
                    print("\nLogging off...", end="")
                    sleep(3)
                    exit(0)  # Exits the program

            case '6':
                # Checks and displays the customer's account balance
                customer.checkBalance()
                # Asks the user if they want to perform another transaction or
                # log off
                choice = input(
                    "\nWould you like to perform another transaction? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue  # Continues to the main menu loop for another action
                else:
                    print("\nLogging off...", end="")
                    sleep(3)
                    exit(0)  # Exits the program

            case '7':
                # Prints the customer's transaction history
                customer.printTransactionHistory()
                # Asks the user if they want to perform another transaction or
                # log off
                choice = input(
                    "\nWould you like to perform another transaction? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue  # Continues to the main menu loop for another action
                else:
                    print("\nLogging off...", end="")
                    sleep(3)
                    exit(0)  # Exits the program

            case '8':
                # Closes the customer's account
                customer.closeAccount(password)
                exit(0)  # Exits the program

            case '9':
                print("\nLogging off...", end="")
                sleep(3)
                exit(0)  # Exits the program


if __name__ == "__main__":
    main()
