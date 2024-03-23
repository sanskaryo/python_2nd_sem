# polymorphism 

class abc:
    
    
    def add(self,a,b,c):
        return a+ b+c
    def add(self,a,b):
        return a+b
    
obj = abc()
print(obj.add(3,4))


