#import the regular expression library
import re

#Created the function to check the password confitions
def check_password_strength(password):

    #Password length check
    if len(password)<8:
        return False
    
    #Uppercase letter check
    if not re.search(r'[A-Z]',password):
        return False
    
    #Lowercase letter check
    if not re.search(r'[a-z]',password):
        return False
    
    #Atleast one number check
    if not re.search(r'\d',password):
        return False
    
    #Special charcter check
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        return False
    return True

password=input("enter the password:")

#Password stregnth check function called
Is_strong=check_password_strength(password)

if Is_strong:
    print("Password is strong")
else:
    print("Password is weak")