a = int(input("enter number 1:"))
b = int(input("enter number 2:"))
if (a%b==0):
    print("%d is divisible by %d" %(a,b))
elif (b%a==0):
    print("%d is divisible by %d" %(a,b))
else:
    print("%d is not divisible by %d" %(a,b))