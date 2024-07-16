def readUserInfo(file_name):
    """
    Reads the named file and appends the information.

    Args:
    file_name (str): The name of the file to read.

    Returns:
    tuple: A tuple containing lists of usernames, passwords, and balances.
    """
    username = []
    password = []
    balances = []
    try:
        with open(file_name, 'r') as fo:
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

def writeUserInfo(username, password, balances, file_name):
    with open(file_name, 'w') as fo:
        for i in range(len(username)):
            fo.write(f"Username: {username[i]}, Password: {password[i]}, Balance: {balances[i]}\n")

def main():
    """
    Main function of the program. Contains main menu and log in screen.
    """
    file_name = "UserInformation.txt"
    currentIndex = -1
    username, password, balances = readUserInfo(file_name)
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

def changeUser(usernames, passwords):
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    for i in range(len(usernames)):
        if entered_username == usernames[i] and entered_password == passwords[i]:
            return i
    print("Invalid username or password")
    return -1

if __name__ == '__main__':
    main()
