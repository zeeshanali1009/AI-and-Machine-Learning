def password_strength(password):
    if len(password) < 8:
        raise Exception("Error! Password must be more than 8 characters.")
    print("Password is strong!")

try:
    password = input("Enter the password: ")
    password_strength(password)
except Exception as e:
    print(e)
