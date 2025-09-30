# Banking System Projects

This repository contains **two Python-based banking system projects**:

1. **Basic Banking System** – Simple version using Python lists  
2. **Advanced Banking System** – Full-featured version using MySQL database  

Both projects provide a **console-based interface** to manage accounts and transactions, suitable for learning and practicing Python programming and database management.


---

## 1. Basic Banking System

**Description:**  
A simple banking system for beginners to learn Python programming concepts and list-based data management.

**Features:**

- Add new users/accounts with default balance  
- Deposit money to an account  
- Withdraw money from an account  
- Print all users and account details  

**Technologies Used:**  

- Python 3.x  
- Lists to store user data  
Run the Python script:
python main.py
Add User:
Enter your name: Shubham Mhaske
Enter your email: shubhammhaske661@gmail.com
Enter your contact: 7798127360
Enter your account number: 1001

Add Balance:
Enter your account number: 1001
Enter the balance: 500

Remove Balance:
Enter your account number: 1001
Enter amount to remove: 200

Print All Users:
Name: Shubham, Email: shubhammhaske661@gmail.com, Contact: 1234567890, Account No: 1001, Balance: 2300

## 2. Advanced Banking System

Description:
An advanced banking system that uses MySQL to store account information and transaction history. Suitable for simulating real-world banking operations.

Features:

Add Account – Create a new account with Name, Email, Phone, Account Number, and Initial Balance

Check Account – View account details

Add Balance – Deposit money and record transactions

Remove Balance – Withdraw money with sufficient balance check

Update Phone Number – Update account phone number

Delete Account – Permanently remove an account

View Transaction History – See all transactions for a specific account

Transfer Amount – Send money between accounts with transaction history

Exit – Close the application

Technologies Used:

Python 3.x

MySQL (for storing accounts and transaction history)

tabulate (to display tables in the console)

Database Setup:

Install MySQL and create a database named Banking_system.

The project automatically creates the required tables (banks and transaction_history) when run.

Install required packages:

pip install mysql-connector-python tabulate


Run the Python script:

python advanced_banking_system.py


Add Account:

Enter Name: Shubham Mhaske
Enter Email: shubhammhaske661@gmail.com
Enter Phone Number: 7798127360
Enter Account Number: 1001
Enter Balance to add: 5000
Account added successfully.


Transfer Money:

Enter Sender's Account Number: 1001
Enter Receiver's Account Number: 1002
Enter amount to transfer: 2000
Successfully transferred 2000 from 1001 to 1002

