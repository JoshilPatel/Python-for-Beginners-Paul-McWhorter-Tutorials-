#In python functions must be at the top

#Whatever is in the function in independant of the program, you just pass in parameters
def tally(numberOfNums,myArray):
    tot=0
    for i in range(0,numberOfNums):
        tot=tot+myArray[i]
    return tot

nums=5
x=[2,4,6,8,10]
mySum=tally(nums,x)
print("Array total= ",mySum)