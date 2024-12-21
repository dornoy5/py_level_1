def find_max_min(numbers):
    return min(numbers), max(numbers)

numbers = list(map(float, input('enter list of numbers separated by spaces:').split()))
min_num,max_num=find_max_min(numbers)
print ('max num:',max_num)
print ('min num:',min_num)
