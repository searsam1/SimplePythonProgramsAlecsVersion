char=input("enter your character:")
if (char>='A' and char<= 'Z'):
     print('UPPERCASE')
elif (char>= 'a' and char<='z'):
     print('LOWERCASE')
elif(char>'10'):
     print("you've entered a number with more than one digit")
elif((char>='0') and (char<='9')):
     print("this is a number.")
else:
     print("this could be a special character.")
