
d = {
    '+' : lambda x,y: x+y,
    '-' : lambda x,y: x-y,
    '*' : lambda x,y: x*y,
    '/' : lambda x,y: x/y,
}

def collect_number():
    return int(input("Enter number: "))

def collect_operator():
    return input("Enter Operator(+, -, *, /): ")

def calculator():
    num1, num2 = collect_number(), collect_number()
    operator = collect_operator()
    return d[operator](num1, num2)

result = calculator()
print(result)


# Old code 
def run_old_version():
    num1 = int(input("Enter no. 1:"))
    num2 = int(input("Enter no. 2:"))
    num3 = input("Enter Your Operator(+,-,*,/): ")
    if(num3 =='+'):
        print(num1,'+',num2,'=',num1+num2)
    elif(num3=='-'):
        print(num1,'-',num2,'=',num1-num2)
    elif(num3=='*'):
        print(num1,'*',num2,'=',num1*num2)
    elif(num3=='/'):
        print(num1,'/',num2,'=',num1/num2)
    else:print('Enter Right Expression')