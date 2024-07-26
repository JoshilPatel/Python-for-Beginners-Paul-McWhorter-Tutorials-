import pickle
names=[]
grades=[]
numStudents=int(input("How many students do you have?: "))

for j in range(0,numStudents):
    name=input("Please enter student name: ")
    names.append(name)
    grade=float(input("Please input grade: "))
    grades.append(grade)

with open("studentData.pkl","wb") as dataF:
    pickle.dump(numStudents,dataF)
    pickle.dump(names,dataF)
    pickle.dump(grades,dataF)

with open("studentData.pkl","rb") as readF:
    a=pickle.load(readF)
    b=pickle.load(readF)
    c=pickle.load(readF)

print(a,b,c)