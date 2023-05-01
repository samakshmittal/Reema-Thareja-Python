a=int(input("Enter no"))
def factorial(a):
    if(a==1):
        return 1
    f=a*factorial(a-1)
    return f
print(factorial(a))
