﻿"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jaroslav Shanel
email: jarekshanel@gmail.com
discord: JaroslavS
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil, Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

oddelovac = "----------------------------------------"
registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }# textovy_analyzator

def zadane_udaje():
    print("$ python projekt1.py")
    print(f"username:{prihlasovaci_jmeno}")
    print(f"password:{heslo}")


prihlasovaci_jmeno = input("Zadej přihlašovací jméno :")
heslo = input("Zadej heslo :")

if prihlasovaci_jmeno not in registrovani_uzivatele:
    zadane_udaje()
    print("Uživatel není registrovaný, ukončuji program...")
    quit()
elif heslo != registrovani_uzivatele[prihlasovaci_jmeno]:
    zadane_udaje()
    print("Bohužel", prihlasovaci_jmeno, "bylo zadané špatné heslo, ukončuji program...")
    quit()
else:
    zadane_udaje()
    print(oddelovac)
    print("Vítej do téte aplikace,", prihlasovaci_jmeno)
    print("Máme pro tebe tři texty k analýze")
    print(oddelovac)

    volba = input("Zvol si text jež chceš analyzovat :")
    print(oddelovac)
    if not volba.isnumeric():
        print("Zadaný parametr nesplňuje požadavky volby. Ukončuji program...")
        quit()
    elif int(volba) <=0 or int(volba) >3:
        print("Zadaný parametr není číslo v daném rozmezí. Ukončuji program...")
        quit()
vybrany_text=TEXTS[int(volba)-1]
vybrany_text = vybrany_text.replace(",", " ").replace(".", " ")
upraveny_vybrany_text = []
titulovana_slova = 0
velka_pismena = 0
mala_pismena = 0
pocet_cisel = 0
suma = 0
for slovo in vybrany_text.split():
    upraveny_vybrany_text.append(slovo.strip(",\n:"))
    if slovo.istitle():
        titulovana_slova +=1
    elif slovo.islower()and slovo.isalpha():
        mala_pismena+=1
    elif slovo.isupper()and slovo.isalpha():
        velka_pismena+=1
    if not slovo.isalpha() and slovo.isnumeric():
        pocet_cisel+=1
        suma += int(slovo)
odsazovac = "|"
print("V textu je celkem", len(upraveny_vybrany_text), "slov")
print(f"V textu je {titulovana_slova} pismen.")
print(f"V textu je {velka_pismena} psaných kapitálkou.")
print(f"V textu je {mala_pismena} pismen.")
print(f"V textu je {pocet_cisel} čísel.")
print(f"Suma čísel uvedených v textu je {suma}.")
print(oddelovac)

delka_slov = dict()
for slovo in upraveny_vybrany_text:
    if len(slovo) not in delka_slov:
        delka_slov[len(slovo)] =1
    else:
        delka_slov[len(slovo)] +=1
print(("LEN"+"|").center(2,"0"), "\t", "OCCURENCES".center(4),"|", "NR.")
nejdelsi = max(sorted(delka_slov.values()))
    
for k, v in sorted(delka_slov.items()):
    print(str(str(k).rjust(3)+str(odsazovac)+v*"*"+" "*abs(v-nejdelsi))+str(4*" ")+"|"+str(v))
