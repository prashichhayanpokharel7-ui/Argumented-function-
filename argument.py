#argumented function 
# from numpy import multiply


def greet1(name):
    print(f"Hello,{name}")
greet1("Pokharel")    

def details(first_name,last_name):
    print(f"{first_name} {last_name}")
def details1(first_name,last_name):
    return f"{first_name} {last_name}"
print(details("Prasik", "Pokharel"))
print(details1("Prasu","Pokharel" ))    

# add,subtract,divide,multiply 
def calculation():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))     
    add = a+b
    sub= a-b
    mul= a*b 
    div= a/b

    print(f"Addition: {add}")
    print(f"Subtraction: {sub}")
    print(f"Multiply: {mul}")
    print(f"Divide: {div}")
calculation()
def calculation():
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))