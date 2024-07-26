numStudents=int(input("Please enter the number of students: "))
grades=[]

for i in range(0,numStudents):
    grade=int(input("Enter grade: "))
    grades.append(grade)

def averageGrade(grades,numGrades):
    total=0
    for i in range(0,numGrades):
        total=total+grades[i]
    avg=total/numGrades
    return avg

def highestGrade(grades,numGrades):
    highest=0
    for i in range(0,numGrades):
        if grades[i]>highest:
            highest=grades[i]
    return highest

def lowestGrade(grades,numGrades):
    lowest=grades[0]
    for i in range(0,numGrades):
        if grades[i]<lowest:
            lowest=grades[i]
    return lowest

print("The average grade is: ",averageGrade(grades,numStudents))
print("The highest grade is: ",highestGrade(grades,numStudents))
print("The lowest grade is: ",lowestGrade(grades,numStudents))
