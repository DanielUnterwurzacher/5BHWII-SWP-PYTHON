import random
from random import randrange

def createArr(number_poss):
    i = []
    for n in range(1, number_poss + 1):
        i.append(n)
    return i

def ziehung(number_draw, number_poss):
    zahlen = createArr(int(number_poss))
    for i in range(0,number_draw):
        g = randrange(number_poss)
        zahlen[g], zahlen[(number_poss-1)-i] = zahlen[(number_poss-1)-i], zahlen[g]
    return zahlen[-number_draw:]

liste = []


poss_in = input("Wie viele Möglichkeiten wollen Sie?:")
draw_in = input("Wie viele Zahlen wollen Sie ziehen?:")
anz_wdh = input("Wie of wollen Sie ziehen?:")
print(anz_wdh + " Ziehungen \t\t" + poss_in + " Möglichkeiten \t\t" + draw_in + " Anzahl Züge")

if(int(poss_in) > int(draw_in)):
    for i in range(int(anz_wdh)):
        liste = liste + ziehung(int(draw_in), int(poss_in))
    for i in range(int(poss_in)):
        print(i+1, "=" ,liste.count(i))