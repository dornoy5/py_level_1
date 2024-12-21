phone_num=input("Please enter phone number")

numbers={
    '1':"one",
    '2':"two",
    '3':"three",
    '4':"four",
    '5':"five",
    '6':"six",
    '7':"seven",
    '8':"eight",
    '9':"nine",
    '0':"zero"}

def convert_to_words(phone_num):
    words=[]
    for digit in phone_num:
        if digit in numbers:
            words.append(numbers[digit])
        else: words.append("unknown")
    return " ".join(words)
print(convert_to_words(phone_num))