# num1 = int(input("Enter number: "))
# if (num1 %2 ==0):
#     print("EVEN NUMBER")
# else:
#     print("ODD NUMBER")

# use num1 % 2 instead of num1 %2 == 0
# and flip the even odd from your function
def even_odd_0(n):
    # if n % 2 is not 0,
    if n % 2:
        print("ODD")
    else:
        print("even")

def odd_even_1(n):
    # binary is sums of powers of 2. 
    # Therefore, to get any odd number, 
    # the first bit must be 1 if its an odd number. 

    # 2^0 = 1, so all odd numbers come from this. 
    # 4 is 100 in binary. 5 is 101, because it adds the 
    # 1 to 4 to make it odd. 
    if bin(n)[-1] == "1":
        return "odd"
    return "even"

print(odd_even_1(13))
