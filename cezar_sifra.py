# ova defka mi mjenja slova
def smjena(i, alf_kod):
    for x, y in alf_kod.items():
        if i == x:
            return y
    return i


print("""
Cezarova sifra radi tako sto \"pomjeri\" slova i brojeve za odredjen broj koraka i na taj
nacin ucini tekst necitljivim za nekoga kome nije poznato koliko je \"pomjeranje\".

""")
# stvorim liste koje predstavljaju alfabet i cifre

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# trazim kljuc, tj koliko ce biti pomjeranje

kljuc = int(input(
    "Koji kljuc zelite da koristite, tj. za koliko mjesta da pomjerite slova i brojeve? "))

# sada treba prepraviti alfabet na novi
kod = ""
for i in alfabet[kljuc:]:
    kod = kod + i
for i in alfabet[:kljuc]:
    kod = kod + i
kod = list(kod)
print(len(kod))
# sada napravim dict sa alf i kodom
alf_kod = {}
for i in range(0, 36):
    alf_kod[alfabet[i]] = kod[i]

za_sifrovati = str(
    input("Molimo da unesete ono sto zelite da kodirate: \n")).strip().lower()
sifrovano = ""


for i in za_sifrovati:
    sifrovano += smjena(i, alf_kod)

print(sifrovano)
