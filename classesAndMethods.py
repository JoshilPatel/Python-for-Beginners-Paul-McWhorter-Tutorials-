class Rectangle:
    #A function inside of a class in known as a method.

    def __init__(self,c,l,w): #This sets the object up, you are passing myRect1 and myRect2 into this init method.
        self.colour=c
        self.length=l
        self.width=w

    def area(self):
        self.area=self.length*self.width
        return self.area
    
    def per(self):
        self.perimeter=self.length*2+self.width*2
        return self.perimeter
    
    def diagonal(self):
        self.diag=(self.width**2+self.length**2)**(1/2)
        return self.diag
    
    def volume(self,h):
        self.height=h
        self.volume=self.length*self.width*self.height
        return self.volume



myRect1=Rectangle('red',2,1)   #Object 1
print(myRect1.colour)
print('myRect1 length =',myRect1.length)
print('myRect1 diagonal = ',myRect1.diagonal())

area=myRect1.area()
print('myRect1 area = ',area)

vol1=myRect1.volume(5)
print('myRect1 volume is ',vol1)

myRect2=Rectangle('blue',4,2)   #Object 2
print(myRect2.colour)
print('myRect2 length =',myRect2.length)