grades=[20,40,50,90,30,95,60]
temp=0

for i in range(0,6):
    for i in range(0,6):
        if grades[i]<grades[i+1]:
            temp=grades[i]
            grades[i]=grades[i+1]
            grades[i+1]=temp
    print(grades)