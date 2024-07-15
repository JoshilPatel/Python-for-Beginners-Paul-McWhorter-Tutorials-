"""myColour=input("Please input your colour: ")

if (myColour=="Red" or myColour=="red" or myColour=="RED"):
    print("Your colour is red")

if (myColour !="Red" and myColour !="red" and myColour !="RED"):
    print("Your colour is not red")"""


#Homework 1


"""number=float(input("Please input your number: "))

if (number>=5 and number<=10):
    print("Your number is between 5 and 10")

else:
    print("Your number is NOT beteen 5 and 10!")"""


#Homework 2

number=float(input("Please enter your number: "))

if (number==0):
    print("Your number is 0!")

if (number%2==0):
    if (number>0):
        print("Your number is even and postiive")
    if (number<0):
        print("Your number is even and negative")

if (number%2!=0):
    if (number>0):
        print("Your number is odd and positive")
    if (number<0):
        print("Your number is odd and negative")