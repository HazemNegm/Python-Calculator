def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiplay(x,y):
    return x * y
def divide(x,y):
    return x / y

print("Enter an operation")
print("+")
print("-")
print("*")
print("/")
choice = input("Enter an operation")
a = int(input("Enter First Numper"))
b = int(input("Enter Seconde Numper"))
if choice == '+':
    print(a,"+",b,"=",add(a,b))
elif choice == '-':
    print(a,"-",b,subtract(x,y))
elif choice == '*':
    print(a,"*",b,multiplay(x,y))
elif choice == '/':
    print(a,"/",b,divide(x,y))
else:
    print("Invaild operation")