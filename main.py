def has_consecutive_letter(string_):
    return any(c1 == c2 for c1, c2 in zip(string_,string_[1:]))
str1 = '''bobby goes out with daddy and mommy and talked about his hobbies'''

str2 = str1.split()
print("the following words have consecutive letters : ")
for words in str2:
    if(has_consecutive_letter(words)):
        print(words,end=', ')