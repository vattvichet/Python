import math

#/
#print("Enter a and b for (ax + b = 0)")
#a = int(input(" a :"))
#b = int(input(" b :"))
#if(a == 0):
#    print("Np root")
#else:
 #   x = (-b)/a
#print("x = ", end= ' ')
#print(x)
#print(math.sqrt(x))

print("Enter a and b for (ax^2 + bx + c = 0)")
a = int(input(" a :"))
b = int(input(" b :"))
c = int(input(" c :"))
delta = (b**2) - (4*a*c)
print("x = ", end= ' ')
if(delta < 0):
    print("No root")
if(delta == 0):
    print((-b)/(2*b))
if(delta > 0):
    print(((-b + math.sqrt(delta))/ 2*a))
    print(((-b - math.sqrt(delta))/ 2*a))
    


