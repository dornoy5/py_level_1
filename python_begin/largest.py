numbers=[2,6,9,8,5,4,5,6,12,3,5,45,45323,4554]
current_number=0
largest_number=0
for i in numbers:
    if i>current_number:
        current_number=i
        largest_number=i
    elif i>largest_number:
        largest_number=i
        
print(largest_number)