#78.right-angled triangle

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()


#79.inverted right-angled triangle

n = int(input("enter n : "))

for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


#80.right-aligned triangle

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()


#81.inverted right-aligned triangle

n = int(input("enter n : "))

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()


#82.pyramid

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()


#83.inverted pyramid

n = int(input("enter n : "))

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()


#84.diamond

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()


#85.hollow rectangle

rows = int(input("enter rows : "))
cols = int(input("enter columns : "))

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#86.hollow right-angled triangle

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j == 1 or j == i or i == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#87.sandglass

n = int(input("enter n : "))

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

for i in range(2,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
