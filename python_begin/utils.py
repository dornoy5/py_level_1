# numbers=[1,2,3,6,5,8,5,8,4,6,3,2,4,5,4,56,4]
def find_max(numbers):
    max_number=0
    for number in numbers:
        if number > max_number:
            max_number=number
    print(max_number)

# find_max(numbers)