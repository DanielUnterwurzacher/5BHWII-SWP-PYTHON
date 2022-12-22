import json
import random
import requests

hand = ["schere", "stein","papier","echse","spock"]

dictZähler = { "schere": 0,
               "stein": 0,
               "papier": 0,
               "echse": 0,
               "spock": 0,
               "spielerW": 0,
               "compW": 0,
               "unentschieden":0}

def computerAuswahl(uid):
    response = requests.get("http://127.0.0.1:5000/stats/%s" % uid)
    js = response.json()
    gesamt = js["schere"]+js["papier"]+js["stein"]+js["echse"]+js["spock"]+1
    rand = random.choices(hand, weights=(
        js["papier"] / gesamt+1, js["stein"] / gesamt+1,
        js["echse"] / gesamt+1, js["spock"] / gesamt+1,
        js["schere"] / gesamt+1), k=5)
    return rand[0]

def eingabePrüfung():
    print("Mögliche Auswahl Möglichkeiten:")
    print(hand)
    print("Ihre eingabe:")
    auswahl = input()

    while auswahl not in hand:
        print("Fehler bitte erneut eingeben:")
        auswahl = input()
    dictZähler[auswahl] = dictZähler[auswahl]+1
    return auswahl

def menue(uid):
    weiter = True
    while weiter:
        print("Was wollen sie machen:(s fuer StatistikBisher, w fuer weiterspielen, b fuer beenden, del um einen User zu löschen)")
        eingabe = input()
        if eingabe == "w":
            return True
        elif eingabe == "b":
            return False
        elif eingabe == "s":
            print(dictZähler)
        elif eingabe == "del":
            requests.delete("http://127.0.0.1:5000/stats/%s" % uid)
            return False
        else:
            print("Falsche eingabe, bitte erneut eingeben")

def saveData(id, dictStats):
    j = json.dumps(dictStats)
    requests.patch("http://127.0.0.1:5000/stats/%s" % id, data={'info': j}).json()

def registerNewPlayer():
    j = {'schere': 0, 'stein': 0, 'papier': 0, 'echse': 0, 'spock': 0,
         'spielerW': 0, 'compW': 0, 'unentschieden': 0}
    response = requests.put("http://127.0.0.1:5000/stats/%s" % "500", json={'info': j})
    return response

def spiel(uid):
    weiter = True
    while weiter:
        eingabeSpieler = eingabePrüfung()
        eingabeComputer = computerAuswahl(uid)

        print("Eingabe des Computers:" + eingabeComputer)

        if eingabeComputer == eingabeSpieler:
            print("Es ist unentschieden")
            dictZähler["unentschieden"] = dictZähler["unentschieden"] +1
        elif hand[(hand.index(eingabeSpieler)-1)%5] == eingabeComputer or hand[(hand.index(eingabeSpieler)+2)%5] == eingabeComputer:
            print("Sie haben verloren")
            dictZähler["compW"] = dictZähler["compW"] +1
        else:
            print("Sie haben gewonnen")
            dictZähler["spielerW"] = dictZähler["spielerW"] +1
        print()
        saveData(uid, dictZähler)
        weiter = menue(uid)

def start(id):
    response = requests.get("http://127.0.0.1:5000/stats/%s"%id)
    js = response.json()
    if len(js)==1:
        return False
    dictZähler["schere"] = js["schere"]
    dictZähler["stein"] = js["stein"]
    dictZähler["papier"] = js["papier"]
    dictZähler["echse"] = js["echse"]
    dictZähler["spock"] = js["spock"]
    dictZähler["spielerW"] = js["spielerW"]
    dictZähler["compW"] = js["compW"]
    dictZähler["unentschieden"] = js["unentschieden"]
    return True

def login():
    print('Geben Sie ihre UserId ein oder drücken Sie "R" um sich zu registrieren!')
    eingabe = input()
    if eingabe == "R":
        uid = registerNewPlayer().json()
        print("Die Registrierung war erfolgreich -> Ihre UserId ist %s"%uid)
        start(uid)
    else:
        while eingabe.isdigit() == False:
            eingabe = input("Geben Sie eine Zahl ein!")
        uid = int(eingabe)
        valid = start(uid)
        while valid is False:
            print('Falsche UserId nächster Versuch ("R" für Registrierung):')
            eingabe = input()
            if eingabe == "R":
                uid = registerNewPlayer().json()
                print("Die Registrierung war erfolgreich -> Ihre UserId ist %s" % uid)
                start(uid)
                valid = True
            else:
                uid = int(eingabe)
                valid = start(uid)
    return uid


def main():
    spiel(login())

if __name__ == '__main__':
    main()

