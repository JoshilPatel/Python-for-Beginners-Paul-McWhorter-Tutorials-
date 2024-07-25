import pickle
fruits=["Apples", "Oranges","Bananas"]
x=7
y=3.14
nuts=["Pecans","Almonds"]
grades=[90,100,56,77,85]

#Creates a file, open it as write binary(wb), f 'points' to the data
with open("myData.pkl","wb") as f:
    #Dumping into f
    pickle.dump(fruits,f)
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(nuts,f)
    pickle.dump(grades,f)

#Reading each line of the fine
with open("myData.pkl","rb") as f2:
    a=pickle.load(f2)
    b=pickle.load(f2)
    c=pickle.load(f2)
    d=pickle.load(f2)
    e=pickle.load(f2)

print(a)
print(b)
print(c)
print(d)
print(e)