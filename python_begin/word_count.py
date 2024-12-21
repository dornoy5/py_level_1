def word_count(text):
    words=text.split()
    counts={}
    for word in words:
        word= word.lower()
        counts[word]=counts.get(word,0)+1
    return counts

text=input("Please enter words: ")
print('word count: ',(word_count(text)))