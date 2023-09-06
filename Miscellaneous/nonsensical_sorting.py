import itertools, random as rd, time


test = [10, 20, 15, 25, 5]

def is_sorted(data):
    for i in range(len(data)-1):
        if data[i] > data[i+1]: return False
    return True






"""
--- Bogo Sort

# Alias : Stupid sort
# Idea : Generates permutations of its input until it finds one that is sorted
""" 

def bogo_sort(data):
    for permuation in list(itertools.permutations(data)):
        if is_sorted(permuation):
            return permuation

# print(bogo_sort(test.copy()))                          # Result : [5, 10, 20, 15, 25, 5]



"""
--- Miracle Sort

# Idea : Hope for a miracle to sort the list by itself
""" 

def miracle_sort(data):
    while not is_sorted(data):
        time.sleep(10)
    
    return data

# print(miracle_sort(test.copy()))                          # Hope for a miracle to happen




"""
--- Stalin Sort

# Alias : Dictator Sort, Trump sort
# Idea : Each element that is not in the correct order is simply eliminated from the list, left to right
""" 

def stalin_sort(data):
    sorted = data[:1]
    
    for val in data:
        if val > sorted[-1]: 
            sorted.append(val)
    
    return sorted

# print(stalin_sort(test.copy()))                          # Returns : [10, 20, 25]