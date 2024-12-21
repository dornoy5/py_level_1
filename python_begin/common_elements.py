
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))


lst1=list(map(int,input("enter first numbers list").split()))
lst2=list(map(int,input("enter second numbers list").split()))

print("common elements of the lists are:",common_elements(lst1,lst2))