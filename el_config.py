input("""
Dobrodosli, ovaj program je napravljen sa namjerom da vam olaksa trazenje elektronskih konfiguracija
atoma. Kada budete spemni da nastavite pritisnite enter.

""")

rad = True
while rad == True:

    broj_e = int(input("Koliko vas atom ima elektrona? >"))

    def provjera(brj_e):
        if 0 < brj_e <= 2:
            return "H"
        elif 2 < brj_e <= 8:
            return "He"
        elif 8 < brj_e <= 18:
            return "Ne"
        elif 18 < brj_e <= 36:
            return "Ar"
        elif 36 < brj_e <= 54:
            return "Kr"
        elif 54 < brj_e <= 86:
            return "Xe"
        elif 86 < brj_e <= 118:
            return "Rn"

    def s_orbitala(kvb_n):
        global broj_e
        if broj_e == 0:
            return ""
        elif broj_e > 2 or broj_e == 2:
            broj_e -= 2
            return(f"({kvb_n}s)2")
        else:
            count = 0
            while broj_e > 0:
                count += 1
                broj_e -= 1
            return(f"({kvb_n}s){count}")

    def p_orbitala(kvb_n):
        global broj_e
        if broj_e == 0:
            return ""
        if broj_e > 6 or broj_e == 6:
            broj_e -= 6
            return(f"({kvb_n}p)6")
        else:
            count = 0
            while broj_e > 0:
                count += 1
                broj_e -= 1
            return(f"({kvb_n}p){count}")

    def d_orbitala(kvb_n):
        global broj_e
        if broj_e == 0:
            return ""
        if broj_e > 10 or broj_e == 10:
            broj_e -= 10
            return(f"({kvb_n}d)10")
        else:
            count = 0
            while broj_e > 0:
                count += 1
                broj_e -= 1
        return(f"({kvb_n}d){count}")

    def f_orbitala(kvb_n):
        global broj_e
        if broj_e == 0:
            return ""
        if broj_e > 14 or broj_e == 14:
            broj_e -= 14
            return(f"({kvb_n}f)14")
        else:
            count = 0
            while broj_e > 0:
                count += 1
                broj_e -= 1
            return(f"({kvb_n}f){count}")

    grupa = provjera(broj_e)

    if grupa == "H":
        n = 1
        print(s_orbitala(n))

    elif grupa == "He":
        broj_e = broj_e - 2
        n = 2
        print(f"[He] {s_orbitala(n)} {p_orbitala(n)}")

    elif grupa == "Ne":
        broj_e = broj_e - 10
        n = 3
        print(f"[Ne] {s_orbitala(n)} {p_orbitala(n)}")

    elif grupa == "Ar":
        broj_e = broj_e - 18
        n = 4
        s_or = s_orbitala(n)
        n -= 1
        d_or = d_orbitala(n)
        n += 1
        p_or = p_orbitala(n)
        print(f"[Ar] {s_or} {d_or} {p_or}")

    elif grupa == "Kr":
        broj_e = broj_e - 36
        n = 5
        s_or = s_orbitala(n)
        n -= 1
        d_or = d_orbitala(n)
        n += 1
        p_or = p_orbitala(n)
        print(f"[Kr] {s_or} {d_or} {p_or}")

    elif grupa == "Xe":
        broj_e = broj_e - 54
        n = 6
        s_or = s_orbitala(n)
        n -= 2
        f_or = f_orbitala(n)
        n += 1
        d_or = d_orbitala(n)
        n += 1
        p_or = p_orbitala(n)
        print(f"[Xe] {s_or} {f_or} {d_or} {p_or}")

    elif grupa == "Rn":
        broj_e = broj_e - 86
        n = 7
        s_or = s_orbitala(n)
        n -= 2
        f_or = f_orbitala(n)
        n += 1
        d_or = d_orbitala(n)
        n += 1
        p_or = p_orbitala(n)
        print(f"[Rn] {s_or} {f_or} {d_or} {p_or}")

    else:
        print("Ne izmisljaj nove atome kada ti i za ove treba program!")
    query = input(
        """

Da napustite program kliknite enter, da nastavite sa radom unesite bilo sta.

""")
    rad = bool(query)
