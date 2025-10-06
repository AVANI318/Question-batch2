import cmath
a=int(input("a :"))
b=int(input("b :"))
c=int(input("c :"))
d = cmath.sqrt(b**2 - 4*a*c)
r1=(-b+d)/(2*a)
r2=(-b-d)/(2*a)
print("r1:",r1)
print("r2:",r2)