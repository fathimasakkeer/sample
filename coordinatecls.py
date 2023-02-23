class coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,obj):
        return(self.x+obj.x,self.y+obj.y)
x1=int(input("enter 1 x coordinate: "))
x2=int(input("enter 2 x coordinate: "))
y1=int(input("enter 1 y coordinate: "))
y2=int(input("enter 2 y coordinate: "))
obj1=coordinate(x1,y1)
obj2=coordinate(x2,y2)
print(obj1+obj2)
