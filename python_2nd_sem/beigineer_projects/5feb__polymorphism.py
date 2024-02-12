# polymorphism 

class abc:
    
    def add(self,a,b):
        return a+b
    
    def add(self,a,b,c=0):
        return a+ b
    
obj = abc()
print(obj.add(3,4,6))


