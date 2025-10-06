n=int(input("enter a number: "))
for row in range(n,0,-1):
    for col in range(n-row):
        print(" ",end="")
    for m in range(1,row+1):
       print("*",end=" ")
    print()
for row in range(1,n+1):
    for col in range(n-row):
        print(" ",end="")
    for m in range(1,row+1):
       print("*",end=" ")
    print()