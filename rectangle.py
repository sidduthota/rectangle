class Rectangle:
    def __init__(self,length:int,width:int):
        self.length = length 
        self.width = width 
    def __iter__(self):
        yield f"length :{self.length}"
        yield f"width: {self.width}"

rect=Rectangle(10,5)
for value in rect:
    print(value)    
    