word = str(input("Please input the word to be translated:  ")).lower()
samoglasnici = ["a", "e", "u", "i", "o"]
pig_latin = ""
sufiks = ""
mickete = False
for slovo in word:
    for glas in samoglasnici:
        if slovo == glas:
            broj = word.index(glas)
            mickete = True
            break
    if mickete == True:
        break


print(broj)
