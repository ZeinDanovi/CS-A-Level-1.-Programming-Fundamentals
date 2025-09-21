import random 


NumPasswords = int(input("Enter the number of passwords to generate: "))
LengthPassword = int(input("Enter the length of each password: "))
password = str()

for i in range(NumPasswords):
    for i in range(LengthPassword):
        password = password + chr(random.randint(33, 126))
    print(password)
    password = ""  # Reset password for the next iteration

