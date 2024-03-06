# M R O 

class A :
    def disp(self):
        print('display from a')
        
class B :
    def disp(self):
        print('display from B')
        
class C :
    def disp(self):
        print('display from C')
        
c_ob = C()
c_ob.disp()
print(C.__mro__)