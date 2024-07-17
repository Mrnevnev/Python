def readUserInfo(fileName):
    """
    Reads the named file and appends the information.

    Args:
    userName = A list that holds the usernames.
    passWord = [] A list that hold the passwords for each user.
    balances = [] A list that holds the balances of each user.


    Returns:
    username, password, balances
    """
    username = []
    password = []
    balances = []
    try:
        with open(fileName, 'r') as fo:
            lines = fo.readlines()
            for line in lines:
                # Strip newline and split on ', ' to get the parts
                parts = line.strip().split(', ')
                if len(parts) == 3:
                    # Split on ': ' to get key-value pairs and extract values
                    user = parts[0].split(': ')[1]
                    pwd = parts[1].split(': ')[1]
                    bal = float(parts[2].split(': ')[1])
                    username.append(user)
                    password.append(pwd)
                    balances.append(bal)
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return username, password, balances

def writeUserInfo(username, password, balances, fileName):
    fo = open(fileName, 'w')
    for i in range(len(username)):
        fo.write(f"Username: {username[i]}, Password: {password[i]}, Balance: {balances[i]}\n")
    fo.close()

def main():
    """
    Main function of the program. Contains main menu and log in screen.

    Args:
        username, password, balances uses the readUserInfo function to copy the information from the file.

    """
    fileName = "UserInformation.txt"
    currentIndex = -1
    username, password, balances = readUserInfo(fileName)
    while True:
        if currentIndex == -1:
            currentIndex = changeUser(username, password)
            if currentIndex == -1:
                continue
        print("Type D to deposit money\n"
              "Type W to withdraw money\n"
              "Type B to display Balance\n"
              "Type C to change user\n"
              "Type E to exit")
        option = input("Enter your choice: ").upper()
        if option == 'D':
            depositMoney(username[currentIndex], balances, currentIndex)
        elif option == 'W':
            withdrawMoney(username[currentIndex], balances, currentIndex)
        elif option == 'B':
            displayBalance(username[currentIndex], balances[currentIndex])
        elif option == 'C':
            currentIndex = changeUser(username, password)
        elif option == 'E':
            writeUserInfo(username, password, balances, fileName)
            quit()
        else:
            print("Invalid option. Please try again.")

def displayBalance(username, balance):
    print(f"Username: {username}, Balance: {balance}")

def depositMoney(username, balances, currentIndex):
    amount = float(input("Enter the amount to deposit: "))
    balances[currentIndex] += amount
    print(f"New balance for {username} is {balances[currentIndex]}")
    return balances

def changeUser(usernames, passwords):
    entered_username = input("Enter your user name: ")
    entered_password = input("Enter your password: ")
    for i in range(len(usernames)):
        if entered_username == usernames[i] and entered_password == passwords[i]:
            return i
    print("Invalid username and password")
    return -1

def withdrawMoney(username, balances, currentIndex):
    amount = float(input("Enter the amount to withdraw: "))
    balances[currentIndex] -= amount
    print(f"New balance for {username} is {balances[currentIndex]}")
    return balances

if __name__ == '__main__':
    main()