
n = int(input("input n = "))
i = 1
s =0
while(i <=n):
    s= s+i
    i = i+ 1
    print("sum ",s)


a = int(input("input a = "))
b = int(input("input b = "))
while(a!= b):
    if(a>b):
        a=a-b
    else:
        b= b-a
print("PGCD = ",a)

num = int(input("input num = "))
i =2
while((num % i) != 0):
    i = i+1
if(num ==i):
    print(num, "is primary")
else:
    print(num, "is non-primary")