num1 = int(input("enter num.1:"))
num2 = int(input("enter num.2:"))
num3 = int(input("enter num.3:"))
if ((num1>num2) and (num1>num3)):
    if (num2>num3):
        print("num.1: %d, num2: %d, num3: %d"%(num1,num2,num3))
elif ((num2>num1) and (num2>num3)):
    if(num1>num3):
        print("num.2: %d, num1: %d, num3: %d"%(num2,num1,num3))
elif ((num3>num2) and (num3>num1)):
    if(num2>num1):
        print("num.3: %d, num.2: %d, num.1: %d"%(num3,num2,num1))
else:
    print ("can't compare as two or more entered values are identical")
