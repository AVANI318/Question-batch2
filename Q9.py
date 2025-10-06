a=4
n = 2 * a - 1
for i in range(n):
    for j in range(n):
        print(a - min(i, j, n - 1 - i, n - 1 - j), end="")
    print()