# trazi indeks od suglasnika
def sug_find(rijec):
    samoglasnici = ["a", "e", "u", "i", "o"]
    for slovo in rijec:
        for glas in samoglasnici:
            if slovo == glas:
                return(rijec.index(glas))

# cekira cime pocinje rijec


def provjera(rijec):
    samoglasnici = ["a", "e", "u", "i", "o", "y"]
    for samoglasnik in samoglasnici:
        if rijec.startswith(samoglasnik):
            return True

# preslaze rijec


def slagalica(rijec):
    indeks = sug_find(rijec)
    sufiks = ""
    ostatak = ""
    for i in rijec[:indeks]:
        sufiks += i
    for i in rijec[indeks:]:
        ostatak += i
    return ostatak + sufiks + "ay"


do = False
while do == False:
    word = str(input("Please input the word to be translated:  ")).lower()

    if provjera(word):
        print(word + "yay")
    else:
        print(slagalica(word))
    do = bool(input("go again? "))
