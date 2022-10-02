from plistlib import InvalidFileException


sentence = "Python is Amazing"
print(sentence.lower()) #   문장을 소문자로 바꿈
print(sentence.upper()) #   문장을 대문자로 바꿈
print(sentence[0].isupper())    #   첫 글자가 대문자인지 확인, True 반환
print(sentence[0].islower())    #   첫 글자가 소문자인지 확인, False 반환
print(len(sentence))
print(sentence.replace("Python", "Java"))

index = sentence.index("n")
print(index)
index = sentence.index("n", index + 1)
print(index)

print(sentence.find("Java"))
#print(sentence.index("Java"))

print(sentence.count("n"))