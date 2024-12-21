numbers=[1,1,5,5,2,1,2,5,4,8,9,8,5,8,5,3,5]
remove_numbers=[]
for number in numbers[:]:
    if number not in remove_numbers:
        remove_numbers.append(number)

print(numbers)
    