hours=int(input("Enter hours worked"))
wages=float(input("Enter wages per hour"))
if(hours>30):
    salary=30*wages+(hours-30)*2*wages
else:
    salary=wages*hours
print(salary)
