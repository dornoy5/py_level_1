def is_palindrom(s):
    s = s.replace(' ', '').lower()
    return s==s[::-1]
s=input("Please enter string: ")
print(f"is {s} a palindrom?", is_palindrom(s))