"""print("Time to count")
j=1
while (j<=10):
    print(j)
    j=j+1
print("That is all folks!")"""

numGrades=int(input("Please enter the number of grades you have: "))
j=1
grades=[]

while (j<=numGrades):
    grade=int(input("Please enter grade: "))
    grades.append(grade)
    print(grades)
    j=j+1

i=0
while(i<numGrades):
    print(grades[i])
    i=i+1