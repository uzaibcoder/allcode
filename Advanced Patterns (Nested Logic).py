#103.butterfly pattern

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    for j in range(2*(n-i)):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    for j in range(2*(n-i)):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()


#104.hollow diamond inside rectangle

n = int(input("enter n : "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end=" ")
        elif i == j or i+j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#105.number diamond

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()


#106.zigzag pattern

n = int(input("enter n : "))

for i in range(3):
    for j in range(n):
        if (i+j) % 4 == 0 or (i == 1 and j % 4 == 2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#107.spiral number matrix (4x4)

n = 4
a = [[0]*n for i in range(n)]

num = 1
top = 0
bottom = n-1
left = 0
right = n-1

while top <= bottom and left <= right:

    for i in range(left,right+1):
        a[top][i] = num
        num += 1
    top += 1

    for i in range(top,bottom+1):
        a[i][right] = num
        num += 1
    right -= 1

    for i in range(right,left-1,-1):
        a[bottom][i] = num
        num += 1
    bottom -= 1

    for i in range(bottom,top-1,-1):
        a[i][left] = num
        num += 1
    left += 1

for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()


#108.right arrow pattern

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


#109.X pattern

n = int(input("enter n : "))

for i in range(n):
    for j in range(n):
        if i == j or i+j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#110.plus pattern

n = int(input("enter n : "))
mid = n // 2

for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#111.heart shape pattern

n = int(input("enter n : "))

for i in range(n//2,n//2+1):
    for j in range(n):
        if j == 1 or j == n//2-1 or j == n//2+1 or j == n-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(n):
    for j in range(n):
        if j == i or j == n-i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#112.square with diagonals marked

n = int(input("enter n : "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end=" ")
        elif i == j or i+j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
