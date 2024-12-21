def find_element(lst, element):
    if element in lst:
        return lst.index(element)
    else:
        return 'Element not found in list'

lst=list(map(int, input("Enter numbers separated by spaces: ").split()))
element= int(input("which elemnt to search"))
print("result:", find_element(lst,element))