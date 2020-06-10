num = int(input("Enter a number"))
n1, n2 = 0, 1
count = 0
if num <= 0:
   print("Enter only positive number")
elif num == 1:
   print("Fibonacci series")
   print(n1)
else:
   print("Fibonacci series:")
   while count < num:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1