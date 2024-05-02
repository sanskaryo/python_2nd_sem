def are_anagrams(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    
    
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
 
    
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False


print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False