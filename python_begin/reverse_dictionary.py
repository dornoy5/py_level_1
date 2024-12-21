def reverse_dictionary(d):
    return {v:k for k, v in d.items()}

dictionary= {'a':1, 'b':2, 'c':3 }
print ('reverse dictionary', reverse_dictionary(dictionary))