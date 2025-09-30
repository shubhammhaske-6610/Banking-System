import mysql.connector
import datetime
from tabulate import tabulate

print("1. Add Account.")
print("2. Check Account.")
print("3. Add Balance.")
print("4. Remove Balance.")
print("5. Update Phone Number.")
print("6. Delete Account.")
print("7. View Transaction History.")
print("8. Transfer Amount.")
print("9. Exit.")

cnx = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="Banking_system"
)

mycursor = cnx.cursor()

# Create banks table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS banks (
    Name VARCHAR(100),
    Email VARCHAR(255),
    Phone VARCHAR(100),
    Account VARCHAR(120) PRIMARY KEY,
    Balance DECIMAL(10,2)
)
""")

# Create transaction_history table with fixed column names
mycursor.execute("""
CREATE TABLE IF NOT EXISTS transaction_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Account VARCHAR(20),
    FromAccount VARCHAR(20),
    ToAccount VARCHAR(20),
    type ENUM('credit', 'debit'),
    Amount DECIMAL(10,2),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

while True:
    try:
        choice = int(input("Enter a choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
        continue

    if choice == 1:
        a = input("Enter Name: ")
        b = input("Enter Email: ")
        c = input("Enter Phone Number: ")
        d = input("Enter Account Number: ")
        e = float(input("Enter Balance to add: "))
        sql = "INSERT INTO banks (Name, Email, Phone, Account, Balance) VALUES (%s, %s, %s, %s, %s)"
        val = (a, b, c, d, e)
        mycursor.execute(sql, val)
        cnx.commit()
        print("Account added successfully.")

    elif choice == 2:
        a1 = input("Enter Account Number to check: ")
        sql1 = "SELECT * FROM banks WHERE Account = %s"
        mycursor.execute(sql1, (a1,))
        result = mycursor.fetchall()
        if result:
            headers = [i[0] for i in mycursor.description]
            print(tabulate(result, headers=headers, tablefmt='grid'))
        else:
            print("Account not found.")

    elif choice == 3:
        now = datetime.datetime.now()
        d = input("Enter Account Number to add balance: ")
        e = float(input("Enter balance to add: "))
        mycursor.execute("SELECT Name FROM banks WHERE Account = %s", (d,))
        result = mycursor.fetchone()

        if result:
            name = result[0]
            mycursor.execute("UPDATE banks SET Balance = Balance + %s WHERE Account = %s", (e, d))
            cnx.commit()

            mycursor.execute("""
                INSERT INTO transaction_history (Name, Account, type, Amount, timestamp)
                VALUES (%s, %s, 'credit', %s, %s)
            """, (name, d, e, now))
            cnx.commit()

            print(f"Added balance {e} to Account {d}")
        else:
            print("Account not found.")

    elif choice == 4:
        now = datetime.datetime.now()
        d = input("Enter Account Number to remove balance: ")
        e = float(input("Enter balance to remove: "))
        mycursor.execute("SELECT Name, Balance FROM banks WHERE Account = %s", (d,))
        result = mycursor.fetchone()

        if result:
            name, current_balance = result
            if float(current_balance) < e:
                print("Insufficient balance.")
            else:
                mycursor.execute("UPDATE banks SET Balance = Balance - %s WHERE Account = %s", (e, d))
                cnx.commit()

                mycursor.execute("""
                    INSERT INTO transaction_history (Name, Account, type, Amount, timestamp)
                    VALUES (%s, %s, 'debit', %s, %s)
                """, (name, d, e, now))
                cnx.commit()

                print(f"Removed balance {e} from Account {d}")
        else:
            print("Account not found.")

    elif choice == 5:
        new_phone = input("Enter New Phone Number: ")
        old_phone = input("Enter Old Phone Number to Update: ")
        sql2 = "UPDATE banks SET Phone = %s WHERE Phone = %s"
        mycursor.execute(sql2, (new_phone, old_phone))
        cnx.commit()
        print(f"Updated phone number from {old_phone} to {new_phone}")

    elif choice == 6:
        a = input("Enter Account Number to delete: ")
        sql = "DELETE FROM banks WHERE Account = %s"
        mycursor.execute(sql, (a,))
        cnx.commit()
        print(f"{mycursor.rowcount} record(s) deleted.")

    elif choice == 7:
        acc = input("Enter Account Number to view transaction history: ")
        mycursor.execute("SELECT * FROM transaction_history WHERE Account = %s ORDER BY timestamp DESC", (acc,))
        history = mycursor.fetchall()
        if history:
            headers = [i[0] for i in mycursor.description]
            print("Transaction History:")
            print(tabulate(history, headers=headers, tablefmt='grid'))
        else:
            print("No transactions found for this account.")

    elif choice == 8:
        now = datetime.datetime.now()
        sender = input("Enter Sender's Account Number: ")
        receiver = input("Enter Receiver's Account Number: ")
        amount = float(input("Enter amount to transfer: "))

        mycursor.execute("SELECT Name, Balance FROM banks WHERE Account = %s", (sender,))
        sender_result = mycursor.fetchone()

        mycursor.execute("SELECT Name FROM banks WHERE Account = %s", (receiver,))
        receiver_result = mycursor.fetchone()

        if sender_result and receiver_result:
            sender_name, sender_balance = sender_result
            receiver_name = receiver_result[0]
            if float(sender_balance) < amount:
                print("Insufficient balance in sender's account.")
            else:
                # Update balances
                mycursor.execute("UPDATE banks SET Balance = Balance - %s WHERE Account = %s", (amount, sender))
                mycursor.execute("UPDATE banks SET Balance = Balance + %s WHERE Account = %s", (amount, receiver))

                # Insert into transaction history
                mycursor.execute("""
                    INSERT INTO transaction_history (Name, Account, type, Amount, FromAccount, ToAccount, timestamp)
                    VALUES (%s, %s, 'debit', %s, %s, %s, %s)
                """, (sender_name, sender, amount, sender, receiver, now))

                mycursor.execute("""
                    INSERT INTO transaction_history (Name, Account, type, Amount, FromAccount, ToAccount, timestamp)
                    VALUES (%s, %s, 'credit', %s, %s, %s, %s)
                """, (receiver_name, receiver, amount, sender, receiver, now))

                cnx.commit()
                print(f"Successfully transferred {amount} from {sender} to {receiver}")
        else:
            print("One or both accounts not found.")

    elif choice == 9:
        print("Exiting the banking system.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 9.")

mycursor.close()
cnx.close()
