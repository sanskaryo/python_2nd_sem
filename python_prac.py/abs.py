from abc import ABC , abstractmethod

class Sample(ABC):
    @abstractmethod
    def add(self,a,b):
        return a+b
    
