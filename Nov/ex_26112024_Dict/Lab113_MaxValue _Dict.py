#max value in the dictionary
#{"a:10,b:20,c:30}

def max_value(dictionary):
    return max(dictionary.values())
   # return min(dictionary.values())
print(max_value({"a":10,"b":20,"c":30}))