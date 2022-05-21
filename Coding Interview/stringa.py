string = "aaabbbcccd"

def comp(string):
    res = ""
    momC = string[0]
    count = 0
    for i in string:
        if i == momC:
            count += 1
        else:
            res += momC + str(count)
            momC = i
            count = 1
    res += momC + str(count)
    return res

print(comp(string))
