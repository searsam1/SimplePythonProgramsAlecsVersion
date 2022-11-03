char=input("enter your character:")
if (char>='A' and char<= 'Z'):
     print('UPPERCASE')
elif (char>= 'a' and char<='z'):
     print('LOWERCASE')
elif((char>='0') and (char<='9')):
     print("this is a number.")
else:
     print("this is possibly a special character.")