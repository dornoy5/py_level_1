
def is_even_and_divisible_by_three(number):
    return number % 2==0 and number % 3==0

number= int(input("enter a number"))
print(f"is {number} even and divisible by 3? ",(is_even_and_divisible_by_three(number)))