# arbitrary parameters

def hello(*st):
    for i in st:
        print("Hello", i, "!")

hello("vichet","vichet1","vichet2")
hello("Sok")

# initialize parameter
def facto(n=0):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
print("5! :", facto(5))