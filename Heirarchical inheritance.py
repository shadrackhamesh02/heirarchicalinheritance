# Heirarchical inheritance

class area :
    print('calculate Area')
class triangle(area):
    def find_area(self,h,b):
        print('Area of triangle : ',0.5*h,b)
class square(area):
    def find_area(self,s):
        print('Area of square : ',s*s)
ob1 = triangle()
ob1.find_area(50,10)
ob2 = square()
ob2.find_area(7)