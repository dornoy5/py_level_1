"separate_even_odd.py"

def separate_even_odd(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers

numbers=list(map(int, input("enter list of numbers").split()))
even_numbers, odd_numbers= separate_even_odd(numbers)
print("even numbers: ",even_numbers)    
print("odd numbers: ",odd_numbers)    