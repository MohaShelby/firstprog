import random

prix = random.randint(1,10)
choix = int(input("Saisissez votre choix : "))

while (choix != prix) :
    if choix > prix :
        print("Moins")
        choix = int(input("Saisissez votre choix : "))
    elif choix < prix :
        print("Plus")
        choix = int(input("Saisissez votre choix : ")) 
else :
    print("Le prix est juste !")

    
