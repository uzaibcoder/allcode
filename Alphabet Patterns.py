#98.alphabet triangle (row repeat)

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()


#99.alphabet triangle (sequential)

n = int(input("enter n : "))
ch = 65

for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end=" ")
        ch = ch + 1
    print()


#100.reverse alphabet triangle

n = int(input("enter n : "))

for i in range(n,0,-1):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()


#101.right-aligned alphabet triangle

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")

    for j in range(i):
        print(chr(64+i),end=" ")

    print()


#102.alphabet pyramid (centered)

n = int(input("enter n : "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")

    for j in range(1,i+1):
        print(chr(64+j),end=" ")

    for j in range(i-1,0,-1):
        print(chr(64+j),end=" ")

    print()
