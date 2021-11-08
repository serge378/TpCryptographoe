import math

from .models import Resultat

def verifier2(a, b, c, r):
    eql = (a**r + b**r) % 3**3 == c**r

    eq2 = (a+c) % 9 == 0

    eq3 = (b+c) % 9 == 0

    eq4 = (1+b*c) % 3 == 0

    eq5 = (a**2 + b*c) % 9 != 0

    return (eql and (eq2 or eq3) and eq4 and eq5)


def verifier1(a, b, c, r):
    eq1 = (a**r + b**r) % 3**3 == c**r

    eq2 = (a+c) % 3 == 9
    eq3 = (a+c) % 6 == 9
    eq4 = (b+c) % 3 == 9
    eq5 = (b+c) % 6 == 9

    eq6 = (1+b*c) % 3 == 0

    eq7 = (a**2 + b*c) % 9 != 0

    return (eq1 and (eq2 or eq3 or eq4 or eq5) and eq6 and eq7)


def generer_U():

    T = []

    for i in range(1, 27):

        if math.gcd(27, i):

            T.append(i)

    return T


def question_2A (a, b, c, r):
    return (verifier1(a, b, c, r) or verifier2(a, b, c, r))


def algo_principal():
    R= [1,5,7,11,13,17]

    U = generer_U()

    solutions = []

    for a in U:
        for b in U:
            for c in U:
                for r in R:
                    if question_2A(a,b,c,r):
                        # solutions.append({'a': a, 'b':b, 'c':c, 'r':r, "solu":True})
                        Resultat.objects.create(a=a, b=b, c=c, r=r, solution=True)
                        # print(f"Le systemème admet des solutions pour \t\t a= {a} \t\t b= {b} \t\t c= {c} \t\t r= {r}")
                    else:
                        # solutions.append({'a': a, 'b':b, 'c':c, 'r':r, "solu":False})
                        Resultat.objects.create(a=a, b=b, c=c, r=r, solution=False)
    # return solutions