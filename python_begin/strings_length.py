from typing import List

def string_lengths(strings: List[str]) -> List[int]:
    return [len(s) for s in strings]

# קלט מהמשתמש
strings = input("Enter words separated by spaces: ").split()
print("Lengths of words:", string_lengths(strings))
