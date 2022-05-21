import math as m

def mySin(theta):
    theta = m.fmod(theta + m.pi, 2*m.pi) - m.pi
    res = 0
    termsign = 1
    power = 1

    for i in range(10):
        res += (m.pow(theta, power) / m.factorial(power)) * termsign
        termsign *= -1
        power += 2
    return res

print(mySin(7))
print(m.sin(7))
