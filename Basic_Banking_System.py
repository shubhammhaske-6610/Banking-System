#Create banking system
print("\nOptions:")
print("1.Add Users.")
print("2.Add Balance.")
print("3.Remove Balance.")
print("4.Print All Users.")
# An Empty list to store the list items
users = []
#repeatedly run the same line of code if progeram is to big....
while True:
    #choice from the user to add user,add balance,remove balance,print all users
    choice1 = int(input("Enter your choice: "))
    if choice1 == 1:
        #To take name from user
        x = input("Enter your name: ")
        #To take email from user
        y = input("Enter your email: ")
        #To take conctact from user
        z = input("Enter your contact: ")
        #To take account_number from user
        w = int(input("Enter your account number: "))
        #balance is already given to the account
        p = 2000 
        #made on variable for store all the inputs in list
        user = [x,y,z,w,p] 
        
        #the all inputs are store in list at the last because of append
        users.append(user)
        #using loop to print all items it at which were added
        for i in users:
            print(i) 
            
    elif choice1 == 4:
        for user in users:
            #printed the all inputs using their indexes
            print(f"Name: {user[0]}, Email: {user[1]}, Contact: {user[2]}, Account No: {user[3]},balance: {user[4]}")        
            
    elif  choice1 == 2:
        w = int(input("enter your account number:"))
        q = int(input("enter the balance:"))
        #to save the all inputs repeatedly        
        for user in users:
            #account no is equal to account no the who given by the user then it will see the index 'user[3]=w that is account no'
            if w == user[3]:
                #balance is 'user[4] and adition of default balance
                user[4]+=q
                print(user)
        
    elif  choice1 == 3:
        w = int(input("enter your account number:"))
        r = int(input("Enter amount to remove:"))        
        for user in users:
           if w == user[3]:
               #subtraction of balance from defalt set which is p that is user[4]
                user[4]-=r
                print(user)        
    else:
        #if user press instead of pressing 1,2,3,4 then the program will exit becauseof break functions
        print(exit) 
        break        