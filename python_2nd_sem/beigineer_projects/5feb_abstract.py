
from abc import ABC, abstractmethod

class test(ABC) :
    
    @abstractmethod
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    
class sample(test):
    def add(self,a,b):
        return f"addition of a and b is  {a+b}"

obj = sample()
print(obj.add(4,6))
    
    
    

    