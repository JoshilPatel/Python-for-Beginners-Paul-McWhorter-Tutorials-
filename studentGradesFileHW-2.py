import pickle

with open("studentData.pkl","rb") as dataF:
    numStudents=pickle.load(dataF)
    names=pickle.load(dataF)
    grades=pickle.load(dataF)

while True:
    name=input("Which student do you want to check?: ")
    for i in range(0,numStudents):
        if names[i]==name:
            print(name,"'s grade is ",grades[i])
