class points():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        #print(x,y)
    def __add__ (self,other):
        return(self.x+other.x,self.y+other.y)
    def __sub__ (self,other):
        return(self.x-other.x,self.y-other.y)
    def __eq__(self,other):
        return(self.x==other.x and self.y==other.y)
    def __str__(self):
        return(f"{self.x},{self.y}")
point=points(5,10)
point2=points(10,45)
p3=point==point2
print(p3)
print(point)
