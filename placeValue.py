a = int(input('enter number:'))
b = int(input('enter digit:'))
c = a%10
d = int((a % 100)/10)
e = int((a % 1000)/100)
if (b == c):
    print("%d is a 1 place" %(b))
elif (b == d):
    print("%d is a 10 place" %(b))
elif (b == e):
    print("%d is a 100 place" %(b))