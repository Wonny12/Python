print("a"+"b")
print("a","b") #print("a"+" b")

#   방법 1
print("나는 %d살입니다." % 20)  #   정수 값
print("나는 %s를 좋아합니다." % "파이썬")   #   string값
print("Apple은 %c로 시작해요." % "A")   #   한 글자만 받는다는 소리 (C: character)
#   %s
print("나는 %s살입니다" % 20)
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

#   방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아합니다".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아합니다".format("파란", "빨간"))