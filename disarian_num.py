broj = str(input("Broj koji treba provjeriti je? \n"))
suma = 0
exp = 1
for i in broj:
    suma += (int(i) ** exp)
    exp += 1
if suma == int(broj):
    print("Broj je DISARIAN! BRAVO!")
else:
    print("Broj nije DISARIAN!")
