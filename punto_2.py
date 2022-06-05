
def validate_pin(password):
    for i in password:
        if (i >= '0' and i <= '9') and ((len(str(password))) == 4 or (len(str(password))) == 6):
            i = "True"
        else:
            i= "False"
    print(i)
print("Enter a password:")
password = input()
validate_pin(password)

