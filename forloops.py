"""fruits=["Apple","Orange","Banana","Mango","Kiwi"]

#Prints apple - Kiwi, prints last one before '5'
#print(fruits[0:5])

for fruit in fruits:
    print(fruit)
    for letter in fruit:
        print(letter)"""

"""myNumbers=[1,2,3,4,5,6,7,8,9,10]
for number in myNumbers:
    print(number)"""

#Counts from 0 to 20 (increments of 2) even numbers

"""for myNumber in range(0,21,2):
    print(myNumber)"""

#Homework

"""numGrades=int(input("Please input number of grades: "))

grades=[]

for grade in range(0,numGrades,1):
    newGrade=int(input("Please enter grade: " ))
    grades.append(newGrade)
    print(grades)

for grade in grades:
    print(grade)

#Or you could have done...
#for i in range(0,numGrades,1):
    #print(grades[i])"""


#Homework: Print out grade average before printing all the grades

numGrades=int(input("Please input number of grades: "))

grades=[]

total=0

for grade in range(0,numGrades,1):
    newGrade=int(input("Please enter grade: " ))
    grades.append(newGrade)
    print(grades)

for grade in grades:
    total=total+grade

average=total/numGrades

print("")
print("The average grade is: ")
print(average)
print("")

#Working out the highest grade
highestGrade=0

for grade in grades:
    if (grade>highestGrade):
        highestGrade=grade

print("The highest grade is: ")
print(highestGrade)
print("")


lowestGrade=grades[0]

for grade in grades:
    if (grade<lowestGrade):
        lowestGrade=grade

print("The lowest grade is: ")
print(lowestGrade)
print("")