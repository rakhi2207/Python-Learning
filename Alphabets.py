text1 =  input()
text2 = input()
for text in [text1,text2]:
    if text.__contains__('a') and text.__contains__('e') and text.__contains__('i') and text.__contains__('o') and text.__contains__('u'):
        print("YES")
    else:
        print("NO")

