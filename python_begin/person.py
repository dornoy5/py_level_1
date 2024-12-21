class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def talk(self):
        print("Hello " + self.first_name + " " + self.last_name)
    def name(self):
        # name=input("what is your name?")
        print("my name is " +self.first_name )
        

# person1=Person("dor","noy")
# person1.name()
# person1.talk()
      
      
# person2=Person("adi","noy")
# person2.talk()


person3 = Person(input("enter your first name: "),"noy")
person3.name()
      