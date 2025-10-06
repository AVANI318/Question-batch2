a = int(input("Enter your amount: "))
currency = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
for i in currency:  
    count = a // i
    if count > 0:
        print(count, "x", i)
        a = a % i