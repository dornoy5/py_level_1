
def character_counts(s):
    count_dict={}
    for char in s:
        count_dict[char] = count_dict.get(char,0)+1
    return count_dict

s= input("Enter a string: ")
print("character_counts: ",character_counts(s))