class DataStorage:
    def __init__(self):
        # Dictionary to store user accounts with username as key and password as value
        self.accounts = {}

    def register_user(self, username, password):
        if username in self.accounts:
            return False  # Username already exists
        self.accounts[username] = password
        return True

    def validate_login(self, username, password):
        return username in self.accounts and self.accounts[username] == password

def main():
    storage = DataStorage()

    while True:
        print("\n--- Welcome to the Login System ---")
        print("1. Register a new account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            if storage.register_user(username, password):
                print("Registration successful!")
            else:
                print("Username already exists. Please choose a different one.")

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if storage.validate_login(username, password):
                print("Login successful! Hello, " + username)
            else:
                print("Invalid username or password. Please try again.")

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

