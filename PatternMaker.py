from nltk.tokenize import sent_tokenize, word_tokenize

def ReadText(fileName):
    f = open("test/"+fileName, "r")
    text = f.read()
    f.close()
    return text

text = ReadText("uji2.txt")
print(text)
print("dipecah menjadi")
print(sent_tokenize(text))
