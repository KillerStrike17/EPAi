def myfunc():
    string='Cppsecrets'
    n=len(string)
    arr=[]
    for i in range(n):
        for j in range(i+1,n+1):
            a=string[i:j]
            arr.append(a)
    print(arr)

def my_func():
    pass

class Rectangle:
    '''
        This is a Rectangle Class. 
        1. If r = Rectangle(10, 20), 
        then >>>r gives 'Rectangle(10, 20)' as it's output
        2. And print(r) gives 'Rectangle: width=10, height=20' as the print output.
        3. Raises Value error if one tries to set width or height as negative
        4. Raises NotImplementedError if one tries to check for r1 < r2, and r2 is not a Rectangle Object
    '''
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width,self.height)
        
    def __init__(self, width, height):
        self.width = width #properties
        self.height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,width):
        if width <= 0:
            raise ValueError("Width Must be positive")
        else:
            self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,height):
        if height <= 0:
            raise ValueError("Height Must be positive")
        else:
            self._height = height

    def area(self): #method
        return self.width*self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            raise NotImplementedError
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width,self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

            