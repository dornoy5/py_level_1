temp=int(input("what is the temperature outside? "))
hot=False
lovely=False
cold=False

if temp>28:
    hot= True
elif 20<temp<27:
    lovely= True

    
if hot:
    print("its hot outside drink a lot of water!")
elif lovely:
    print("its a lovely day!")
else:print("its cold outside warm up!")
    
    