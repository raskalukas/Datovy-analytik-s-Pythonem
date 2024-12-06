'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lukáš Raška
email: raskalukas@seznam.cz
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
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

uzivatele = {"bob":"123",
                 "ann":"pass123",
                 "mike":"password123",
                 "liz":"pass123"
            }

#pomocne promenne
cara = 40 * "-"

#Beh programu
username = input("username:")
password = input("password:")

if username in uzivatele.keys() and password == uzivatele[username]:
     #spocitani mnozstvi textu k analyze
     pocet_textu = len(TEXTS)
     cisla_textu = range(1,pocet_textu+1)

     #privitani uzivatele
     print(cara)
     print(f"Welcome to the app, {username} \nWe have {pocet_textu} texts to be analyzed.")
     print(cara)

     #volba textu k analyze
     poradi_textu = input(f"Enter a number btw. 1 and {pocet_textu} to select: ")

     #ukonceni pokud uzivatel nazada cislo
     if poradi_textu.isnumeric() == False:
          print("Not a number, terminating programm..")

     #hlavni telo analyzy
     elif int(poradi_textu) in cisla_textu:
          print(cara)

          #rozdeleni textu na jednotliva slova a ocisteni o specialni znaky
          vybrany_text = TEXTS[int(poradi_textu)-1]
          slova = [slovo.strip(r",.:;'") for slovo in vybrany_text.split()]
          
          #pocet slov v textu
          print("There are", len(slova), "words in the selected text.")

          #pocet slov s prvnim velkym pismenem
          title_case_slova = [slovo for slovo in slova if slovo.istitle()]
          print("There are", len(title_case_slova), "titlecase words.")

          #pocet slov psanych velkymi pismeny
          #upper_case_slova = [slovo for slovo in slova if slovo.isupper()]   # -> bere retezec 30N jako psany velkymi pismeny... 
          upper_case_slova =  [slovo for slovo in slova if (slovo.isupper() and slovo.isalpha())]
          print("There are", len(upper_case_slova), "uppercase words.")

          #lower case
          lower_case_slova = [slovo for slovo in slova if slovo.islower()]
          print("There are", len(lower_case_slova), "lowercase words.")

          #numeric
          numeric_slova = [slovo for slovo in slova if slovo.isnumeric()]
          print("There are", len(numeric_slova), "numeric strings.")

          #suma vsech cisel
          soucet = 0
          for cislo in numeric_slova:
               soucet += int(cislo)
          print("The sum of all numbers is", soucet)
          
          ##tvorba grafu poctu delek jednotlivych slov##########
          #vypocet poctu slov pro ruzne delky
          my_dict = {}
          for slovo in slova:
              delka = len(slovo)
              
              #pridavani do slovniku s cetnosti delek jednotlivych slov
              if delka not in my_dict.keys():
               my_dict[delka] = 1
              else:
                  my_dict[delka] += 1
          
          #zjisteni maximalniho poctu slov u jedne delky (potrebuji pro graf)
          max_pocet_slov = max(my_dict.values())
          delka_pred_hlavickou = len("  OCCURENCES")
          sloupec_v_hlavicce = max_pocet_slov - delka_pred_hlavickou
          
          #print hlavicky
          print(cara)
          print(f"LEN|  OCCURENCES{'' :<{sloupec_v_hlavicce}}|NR.", sep="")
          print(cara)

          #print vysledneho grafu
          for keys,values in sorted(my_dict.items()):
               print(f"{keys: >3}", "|", f"{values * "*": <{max_pocet_slov}}", "|", values, sep="")

     #ukonceni pokud uzivatel zada neexistujici cislo textu
     else:
          print("no text with such number, terminating the program..")

#ukonceni programu pri spatnem uzivateli a/nebo heslu
else:
     print("unregistered user, terminating the program..")
