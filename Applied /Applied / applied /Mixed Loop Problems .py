#65.multiplication table

n = int(input("enter n : "))

for i in range(1,11):
    print(n,"x",i,"=",n*i)


#66.sum of even and odd numbers

n = int(input("enter n : "))
even = 0
odd = 0

for i in range(1,n+1):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print("sum of even numbers =",even)
print("sum of odd numbers =",odd)


#67.armstrong number

n = int(input("enter n : "))
temp = n
digits = len(str(n))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10

if sum == n:
    print("armstrong number")
else:
    print("not an armstrong number")


#68.largest and smallest digit

n = int(input("enter n : "))

largest = 0
smallest = 9

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    n = n // 10

print("largest digit =",largest)
print("smallest digit =",smallest)


#69.factors of a number

n = int(input("enter n : "))

for i in range(1,n+1):
    if n % i == 0:
        print(i,end=" ")


#70.perfect number

n = int(input("enter n : "))
sum = 0

for i in range(1,n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("perfect number")
else:
    print("not a perfect number")


#71.decimal to binary

n = int(input("enter decimal number : "))
binary = ""

if n == 0:
    binary = "0"

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

print("binary =",binary)


#72.binary to decimal

n = input("enter binary number : ")
decimal = 0
power = 0

for i in n[::-1]:
    decimal = decimal + int(i) * (2 ** power)
    power = power + 1

print("decimal =",decimal)


#73.count and average until -1

sum = 0
count = 0

while True:
    n = float(input("enter number (-1 to stop) : "))

    if n == -1:
        break

    sum = sum + n
    count = count + 1

if count > 0:
    print("count =",count)
    print("average =",sum/count)
else:
    print("no numbers entered")


#74.sin series

import math

x = float(input("enter x : "))
n = int(input("enter number of terms : "))

sum = 0

for i in range(n):
    power = 2*i + 1
    term = x ** power / math.factorial(power)

    if i % 2 == 0:
        sum = sum + term
    else:
        sum = sum - term

print("sum =",sum)


#75.palindrome using recursion

def palindrome(s,start,end):
    if start >= end:
        return True

    if s[start] != s[end]:
        return False

    return palindrome(s,start+1,end-1)

s = input("enter string : ")

if palindrome(s,0,len(s)-1):
    print("palindrome")
else:
    print("not palindrome")


#76.count vowels using recursion

def vowels(s,n):
    if n == 0:
        return 0

    if s[n-1].lower() in "aeiou":
        return 1 + vowels(s,n-1)
    else:
        return vowels(s,n-1)

s = input("enter string : ")

print("number of vowels =",vowels(s,len(s)))


#77.increasing and decreasing using recursion

def numbers(n):
    if n == 0:
        return

    numbers(n-1)
    print(n,end=" ")

n = int(input("enter n : "))

numbers(n)

for i in range(n-1,0,-1):
    print(i,end=" ")
