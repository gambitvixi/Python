# rjesava jednacinu
def rjesenje(konstante):
    return ((konstante[2]-konstante[1])/konstante[0])

# haj da nam nadje a b i c


def konstante(equation):
    za_a = ""
    za_b = ""
    za_c = ""
    jen = equation.index("x")
    dva = equation.index("=")
    for i in equation[:(jen-1)]:
        za_a = za_a + i
    for i in equation[(jen+1):dva]:
        za_b = za_b + i
    for i in equation[(dva+1):]:
        za_c = za_c + i
    a1 = (za_a.strip())
    b1 = (za_b.strip())
    c1 = (za_c.strip())
    a = int(a1)
    if b1.startswith('-'):
        b = - int(b1[1:])
    else:
        b = int(b1[1:])
    c = int(c1)
    return a, b, c


equation = str(
    input("Input your equation in a*x+/-b=c format please: ")).strip().lower()

print(equation)

print(rjesenje(konstante(equation)))
