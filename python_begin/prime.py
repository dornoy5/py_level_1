def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input('enter a number to test'))
print(f"{number} is prime" if is_prime(number) else f"{number} is not prime.")