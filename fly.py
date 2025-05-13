### PLANERING ###
# Rum 1 cellen
# Dörren är inte låst så det är bara att gå ut.
# Spelaren kan: Genomsöka rummet och öppna dörren (som är olåst)
# Kan hitta en sten som den kan ta upp

# Rum 2 Hallen
# Man möter en vakt.
# Man kan distrahera vakten med sten från första rummet
# Smyga förbi och då tar vakten en. Viss chans att lyckas. Slumpfunktion.

# Rum 3 
# Man kan gå höger eller vänster
# Höger blir tagen av en grupp med vakter och spelet är slut
# Vänster då finns det en vakt i vägen och den får man slåss mot sedan frihet


# KVAR ATT GÖRA
# Programmera en huvudmeny med minst Starta spelet och Avsluta    (exit() - avslutar direkt)
# Skriva en readme.txt fil med spelinstruktioner
# Du behöver göra minst två rum till med två valalternativ i varje rum.



import random

def start_game():
    har_sten = False
    rum_1(har_sten)

def rum_1(har_sten):
    spelaren_väljer = True
    while spelaren_väljer:
        print("\nDu är i en cell. Framför dig har du en dörr.")
        print("Du kan 1. öppna dörren eller 2. genomsöka cellen.")
        cellval = input("Vad väljer du? ").lower()
        
        if cellval == "1":
            print("Du öppnar dörren och går till nästa rum.")
            rum_2(har_sten)
            break
        elif cellval == "2":
            if not har_sten:
                print("Du hittar en sten.")
                svar = input("Vill du ta stenen? (ja eller nej) ").lower()
                if svar == "ja":
                    print("Du har tagit stenen.")
                    har_sten = True
                    rum_2(har_sten)  
                else: 
                    print("Du låter stenen ligga kvar.")
            else:
                print("Det finns inget mer att hitta.")
        else:
            print("Ogiltigt val, försök igen.")

def rum_2(har_sten):
    print("\nDu har kommit till hallen och möter en vakt.")
    if har_sten:
        print("Du kan distrahera vakten med stenen.")
        svar = input("Vill du använda stenen? (ja eller nej) ").lower()
        if svar == "ja":
            print("Vakten distraheras och du smyger förbi!")
            rum_3()
        else:
            print("Vakten ser dig och du får slåss!")
            if random.choice([True, False]):
                print("Du lyckas slåss mot vakten och går vidare!")
                rum_3()
            else:
                print("Du förlorade striden. Spelet är slut.")
                exit()
    else:
        print("Vakten blockerar vägen. Du måste slåss!")
        if random.choice([True, False]):
            print("Du lyckas slåss mot vakten och går vidare!")
            rum_3()
        else:
            print("Du förlorade striden. Spelet är slut.")
            exit()

def rum_3():
    print("\nDu står vid ett vägskäl. Du kan gå vänster eller höger.")
    cellval = input("Vad väljer du? (vänster eller höger) ").lower()
    
    if cellval == "höger":
        print("Du blir tagen av en grupp med vakter. Spelet är slut.")
        exit()
    elif cellval == "vänster":
        print("Det finns en vakt i vägen. Du måste slåss!")
        if random.choice([True, False]):
            print("Du lyckas slåss mot vakten och hittar friheten!")
            print("Grattis, du har vunnit spelet!")
        else:
            print("Du förlorade striden. Spelet är slut.")
            exit()
    else:
        print("Ogiltigt val. Spelet är slut.")
        exit()

def main_menu():
    while True:
        print("\n--- Huvudmeny ---")
        print("1. Starta spelet")
        print("2. Avsluta")
        val = input("Vad väljer du? ")
        
        if val == "1":
            start_game()
        elif val == "2":
            print("Tack för att du spelade! Hejdå!")
            exit()
        else:
            print("Ogiltigt val, försök igen.")


main_menu()
exit()

