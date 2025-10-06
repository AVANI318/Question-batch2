n=int(input("enter number : "))
for row in range(1,n+1):
    for col in range(1,row+1):
        print("*",end=" ")
    for col in range(2*(n-row)):
        print(" ",end=" ")
    for col in range(1,row+1):
        print("*",end=" ")
    print()
for row in range(n-1,0,-1):
    for col in range(1,row+1):
        print("*",end=" ")
    for col in range(2*(n-row)):
        print(" ",end=" ")
    for col in range(1,row+1):
        print("*",end=" ")
    print()



