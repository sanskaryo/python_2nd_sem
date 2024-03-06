#  DIAMOND SHAPE ALGORITHM  ONLY IN PY 3 


# M R O 

class X :
    def disp(self):
        print('display from X')
        
class A(X) :
    def disp(self):
        print('display from A')
        
class B(X) :
    pass

class C(B,A) :
    pass
        
c_ob = C()
c_ob.disp()
print(C.__mro__)


























# def display_available_items(dct):
#     print("Available Items:")
#     print("S.No.   Item        Quantity   Cost/Item")
       
#         availableItems ={1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
#                 2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
#                 3: {'Item': 'Coffee',   'Quantity': 25,     'Cost/Item': 55},
#                 4: {'Item': 'Chips', 'Quantity': 10,      'Cost/Item': 50},
#                 5: {'Item': 'Cream', 'Quantity': 5,        'Cost/Item': 30}}



# display_available_items(availableItems)





 
#     print("      Available Items:")
#     print("S.No.          Item           Quanity        Cost/Item       ")
#     for i in dct:
#         print(f"{i}              {dct[i]['Item']}        {dct[i]['Quantity']}              {dct[i]['Cost/Item']}")  

# availableItems ={1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
#                 2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
#                 3: {'Item': 'Coffee',   'Quantity': 25,     'Cost/Item': 55},
#                 4: {'Item': 'Chips', 'Quantity': 10,      'Cost/Item': 50},
#                 5: {'Item': 'Cream', 'Quantity': 5,        'Cost/Item': 30}}

# display_available_items(availableItems)