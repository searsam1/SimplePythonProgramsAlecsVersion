num1 = int(input("Enter no. 1:"))
num2 = int(input("Enter no. 2:"))
num3 = input("Enter Your Expresion: ")
if(num3 =='+'):
    print(num1,'+',num2,'=',num1+num2)
elif(num3=='-'):
    print(num1,'-',num2,'=',num1-num2)
elif(num3=='*'):
    print(num1,'*',num2,'=',num1*num2)
elif(num3=='/'):
    print(num1,'/',num2,'=',num1/num2)
else:print('Enter Right Expression')
