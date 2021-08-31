# getallenraden-SeanBooij

# Input vragen voor het getal aan de gamemaster
te_raden_getal = input("Welk getal wil je gebruiken?\n")
# De loop om te vragen aan de nieuweling welk getal het is, met het maximaal aantal beurten. In dit geval 7.
for i in range(0,7):
        ingevoerd_getal = input("Welk getal denk je dat het is?\n")
        if ingevoerd_getal > te_raden_getal:
                print("Getal is te hoog")
        if ingevoerd_getal < te_raden_getal:
                print("Getal is te laag")
        if te_raden_getal == ingevoerd_getal:
            print("je hebt het getal goed geraden good job")
            break
# Maximum aantal beurten
if i == 6:
    print("je hebt geen beurten meer helaas")
