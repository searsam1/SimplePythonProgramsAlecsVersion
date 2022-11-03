num1 = int(input("Enter no.1:"))
num2 = int(input("Enter no.2:"))
num3 = int(input("Enter no.3:"))

if ((num1>num2) & (num1>num3)):
    print("%d is the greatest number out of the three." %(num1))
elif ((num2>num1) & (num2>num3)):
      print("%d is the greatest number out of the three." %(num2))
elif ((num3>num1) & (num3>num2)):
     print("%d is the greatest number out of the three." %(num3))
elif ((num1==num2) & (num2==num3)):
    print("all numbers are equal.")