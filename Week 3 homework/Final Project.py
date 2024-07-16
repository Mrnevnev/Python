def read_user_info(file_name):
    userName = []
    passWord = []
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
                    userName.append(user)
                    passWord.append(pwd)
                    balances.append(bal)
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return userName, passWord, balances

def main():
    file_name = "UserInformtion.txt"  # Ensure this matches the actual file name exactly
    userName, passWord, balances = read_user_info(file_name)
    print("Usernames:", userName)
    print("Passwords:", passWord)
    print("Balances:", balances)

if __name__ == '__main__':
    main()