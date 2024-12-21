def calculate_average(numbers):
    return sum(numbers)/ len(numbers)

numbers = list(map(float,input('enter numbers seperated by spaces: ').split()))

print('avarege:', calculate_average(numbers))