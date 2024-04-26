class number:
    
    def __init__(self,lattitude,altitude):
        self.lattitude=lattitude
        self.altitude=altitude
    def __add__(self,others):
        
        return number(self.lattitude+others.lattitude,self.altitude+others.altitude)
        
    #def __div__(self,divisor):
        #return number(self.latitude)
        #return
    #def __eq__(self,others):
       # if self.lattitude==others.lattitude:
            
            #return True
        #else:
            #return False
           
l1=number(lattitude=22.24,altitude=24.34)
l2=number(lattitude=12.21,altitude=32.23)

l3=number(flot(input('enter latitudeand altitude'))
          #l4=number(flot(input('enter altitude'))
x=l1+l2 
print(x)
y=x/2 
print(y)        
       
