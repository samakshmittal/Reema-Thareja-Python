count_pass=0
count_fail=0
for i in range(1, 11, 1):
    marks=int(input("Enter marks"))
    if(marks>50):
        count_pass+=1
    else:
        count_fail+=1
print("No of students pass =", count_pass)
print("No of students fail =", count_fail)
