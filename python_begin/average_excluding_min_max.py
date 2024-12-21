def average_excluding_min_max(numbers):
    if len(numbers) <=2:
        return 'Input list should have at least 3 numbers'
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))   
    return sum(numbers) / len(numbers)

numbers = list(map(float, input('Enter numbers separated by spaces: ').split()))
print("Average excluding min and max:", average_excluding_min_max(numbers))