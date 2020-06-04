factorial=1
num=int(input("Enter number"))
if num<0:
    print("Number is negative")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("Factorial of given number is",factorial)