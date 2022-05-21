number = "3662277"
words = ["foo", "bar", "baz", "foobar", "emo", "cap"]

digits = ["","", "abc","def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
res = ""
res2 = []
for num in number:
    res += digits[int(num)]

def match(word):
    for char in word:
        if  char not in res:
            return False
    return True

for word in words:
    if match(word):
        res2.append(word)
print(res2)
