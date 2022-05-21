v = 48
roman   = ['L', 'X', 'V', 'I']
rNumber = [50, 10, 5, 1]


def romanTo(numb):
    num = numb
    res = ""
    for idx, val in enumerate(rNumber):
        print("for")
        while num >= val:
            print("while: ", numb, " ", val)
            res += roman[idx]
            num -= val
    return res

print(romanTo(v))

# 56 -> LVI
# 48 -> IIL
# 34 -> XXXIV
