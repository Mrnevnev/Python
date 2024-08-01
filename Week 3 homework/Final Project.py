def readUserInfo(fileName):
    """
    Reads the named file and appends the information.

    Args:
    fileName (str): The name of the file to read.

    Returns:
    tuple: A tuple containing lists of usernames, passwords, and balances.
    """
    username = []
    password = []
    balances = []
    try:
        with open(fileName, 'r') as fo:
            lines = fo.readlines()
            for line in lines:
                # Split line into components based on spaces
                parts = line.strip().split()
                if len(parts) == 3:
                    user = parts[0]
                    pwd = parts[1]
                    bal = float(parts[2])
                    username.append(user)
                    password.append(pwd)
                    balances.append(bal)
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return username, password, balances

def writeUserInfo(username, password, balances, fileName):
    with open(fileName, 'w') as fo:
        for i in range(len(username)):
            fo.write(f"Username: {username[i]}, Password: {password[i]}, Balance: {balances[i]:.2f}\n")

def main():
    """
    Main function of the program. Contains main menu and log in screen.
    """
    fileName = "UserInformtion.txt"
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
            break
        else:
            print("Invalid option. Please try again.")


def displayBalance(username, balance):
    """
    Displays the balance amount of the logged-in user.

    Args:
    username (str): The username of the logged-in user.
    balance (float): The balance of the logged-in user.
    """
    print(f"Username: {username}, Balance: {balance:.2f}")


def depositMoney(username, balances, currentIndex):
    """
    Deposits amount given by user to account and displays the updated balance.

    Args:
    username (str): The username of the logged-in user.
    balances (list): The list of balances of all users.
    currentIndex (int): The index of the current user in the list.
    """
    while True:
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount < 0:
                print("Negative amount entered. Please enter a positive amount.")
            else:
                balances[currentIndex] += amount
                print(f"New balance for {username} is {balances[currentIndex]:.2f}")
                return
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")


def withdrawMoney(username, balances, currentIndex):
    """
    Withdraws amount given by user from account and displays the updated balance.

    Args:
    username (str): The username of the logged-in user.
    balances (list): The list of balances of all users.
    currentIndex (int): The index of the current user in the list.
    """
    while True:
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount < 0:
                print("No negative numbers. Please enter a positive amount.")
            elif amount > balances[currentIndex]:
                print("Not enough money for withdrawal. Please enter a smaller amount.")
            else:
                balances[currentIndex] -= amount
                print(f"New balance for {username} is {balances[currentIndex]:.2f}")
                return
        except ValueError:
            print("Invalid amount entered. Please enter a numerical value.")


def changeUser(usernames, passwords):
    """
    Change user function that lets you change accounts upon successful log-in information.
    Displays the balance amount of the logged-in user.

    Args:
    usernames (list): The list of usernames of all users.
    passwords (list): The list of passwords of all users.

    Returns:
    int: The index of the logged-in user in the list, or -1 if login fails.
    """
    entered_username = input("Enter your user name: ")
    entered_password = input("Enter your password: ")
    for i in range(len(usernames)):
        if entered_username == usernames[i] and entered_password == passwords[i]:
            return i
    print("Invalid username and password")
    return -1

if __name__ == '__main__':
    main()