def multiple_of(n,limit):
    multiples=[]
    for i in range(1, limit+1, 1):
        multiples.append(n*i)
    return multiples

n=int(input("enter number to multiple"))
limit=int(input("enter limit to multiple"))
print(f"multiple of {n} up to {n*limit} ",multiple_of(n,limit))