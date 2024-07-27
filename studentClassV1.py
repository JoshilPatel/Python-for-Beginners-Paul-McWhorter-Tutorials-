class Student:
    def __init__(self,fN,sN):
        self.firstName=fN
        self.secondName=sN
    
    def inputGrades(self,numGrades):
        grades=[]
        for i in range(0,numGrades):
            grade=int(input("Please enter grade: "))
            grades.append(grade)
        self.grades=grades
        return self.grades
    
    def highestGrade(self,numGrades):
        highest=0
        for i in range(0,numGrades):
            if self.grades[i]>highest:
                highest=self.grades[i]
        self.highest=highest
        return self.highest
    
    def lowestGrade(self,numGrades):
        lowest=self.grades[0]
        for i in range(0,numGrades):
            if self.grades[i]<lowest:
                lowest=self.grades[i]
        self.lowest=lowest
        return self.lowest
    
    def avgGrade(self,numGrades):
        total=0
        for i in range(0,numGrades):
            total=total+self.grades[i]
        self.avg=total/numGrades
        return self.avg
    
    def printGrades(self,numGrades):
        print("The students grades are: ")
        for i in range(0,numGrades):
            print(self.grades[i])
        
    

student1=Student('Joshil','Patel')
print(student1.firstName)
print(student1.secondName)

student1Grades=student1.inputGrades(3)
print(student1Grades)
print("The highest grade is:",student1.highestGrade(3))
print("The lowest grade is: ",student1.lowestGrade(3))
print("The average grade is: ",student1.avgGrade(3))

student1.printGrades(3)