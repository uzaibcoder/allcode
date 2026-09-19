#88.number triangle row-wise

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#89.sequential number triangle

n = int(input("enter n : "))
num = 1

for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num = num + 1
    print()


#90.floyd's triangle

n = int(input("enter n : "))
num = 1

for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num = num + 1
    print()


#91.1-0 alternating triangle

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(i):
        if (i+j) % 2 == 0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()


#92.pascal's triangle

n = int(input("enter n : "))

for i in range(n):
    num = 1

    for j in range(i+1):
        print(num,end=" ")
        num = num * (i-j) // (j+1)

    print()


#93.number pyramid

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")

    for j in range(1,i+1):
        print(j,end=" ")

    for j in range(i-1,0,-1):
        print(j,end=" ")

    print()


#94.inverted number triangle

n = int(input("enter n : "))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#95.column-wise incrementing

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(j + (i-1)*n,end=" ")
    print()


#96.reverse number triangle

n = int(input("enter n : "))

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


#97.binary number triangle

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(i):
        if j % 2 == 0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
