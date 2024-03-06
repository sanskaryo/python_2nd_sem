def add(a,b):
    return a+b

def deco(fun):
    def wraper(a,b):
        print("this is addtional")
        return fun(a,b)     
    
    re = add(3,5)
    print(re)
    
#map
def apna_fun(x):
    print(x)
    
    
    
map(10)