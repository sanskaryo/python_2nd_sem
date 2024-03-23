# def flatten(nested_list):
#    flat_list = []
#    for sublist in nested_list:
#       for item in sublist:
#          if isinstance(item, list):
#             flat_list.extend(flatten(item))
#          else:
#             flat_list.append(item)
#    return flat_list


# flat_list = sum(nested_list, [])



class flatten :
    def __init__(self, lst, r=0,c=0):
        self.lst = lst
        self.c = c
        self.r = r
        
        if r != 0 and c != 0:
            M = []
            tmp = []
            for i in self.lst:
                tmp.append(i)
                if len(tmp)  == c:
                    M.append(tmp)
                    tmp = []
                    
                self.lst = M
                
                
    def flatten(self):
        stri = str(self.lst)
        stri = stri.replace('[', "").replace(']', "")
        print(stri)