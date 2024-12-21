

def words_by_length(sentence):
    words=sentence.split()
    length_dict={}
    for word in words:
        length= len(word)
        length_dict.setdefault(length, []).append(word)
    return length_dict

sentence= input("enter sentence: ")
print("words_by_length:",words_by_length(sentence))