class DataStorage:
    def __init__(self):
        self.accounts = {}

    def register_user(self, username, password, retyped_password):
        if username in self.accounts:
            return "Username already exists."
        if password == "":
            return "Password cannot be empty."
        if password != retyped_password:
            return "Passwords do not match."
        if len(username) < 5 or len(username) > 20 or ' ' in username:
            return "Invalid username format."
        if len(password) < 8 or len(password) > 12 or not any(char.isalpha() for char in password) or \
                not any(char.isdigit() for char in password) or not any(char in "!@#$%^&*" for char in password):
            return "Password does not meet complexity requirements."

        self.accounts[username] = password
        return "Registration successful!"

test_cases = [
    ("validUser123", "P@ss1234", "P@ss1234", "Registration successful!"),
    ("validUser123", "P@ss1234", "wrongpass", "Passwords do not match."),
    ("validUser123", "password", "password", "Password does not meet complexity requirements."),
    ("validUser123", "P@", "P@", "Password does not meet complexity requirements."),
    ("existingUser", "P@ss1234", "P@ss1234", "Username already exists."),
    ("new user", "P@ss1234", "P@ss1234", "Invalid username format."),
    ("validUser123", "", "", "Password cannot be empty.")
]

for idx, (username, password, retyped_password, expected) in enumerate(test_cases, start=1):
    storage = DataStorage()
    if idx == 5:
        storage.register_user("existingUser", "P@ss1234", "P@ss1234")
    result = storage.register_user(username, password, retyped_password)
    assert result == expected, f"Test Case {idx} Failed: Expected '{expected}', but got '{result}'."

print("All test cases passed successfully.")

