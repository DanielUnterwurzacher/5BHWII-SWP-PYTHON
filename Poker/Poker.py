import random
import numpy as np

dict = {'Royal Flush':0,'Straight Flush':0,'Straße':0,'Flush':0,'Full House':0,'Paar':0,'Zwei Paare':0,'Drilling':0,'Vierling':0}
dictPercentage = {'Royal Flush':0,'Straight Flush':0,'Straße':0,'Flush':0,'Full House':0,'Paar':0,'Zwei Paare':0,'Drilling':0,'Vierling':0}

def draw():
    liste = []
    for i in range(1,53):
        liste.append(i)

    for j in range(5):
        value = random.randrange(0, 52)
        liste[value], liste[51-j] = liste[51-j], liste[value]

    fiveCards = []
    for x in range(5):
        fiveCards.append(liste[47+x])
    return fiveCards

drawnSymbol = []
drawnColor = []

def showCards(fiveCards):
    for i in range(5):
        drawnSymbol.append(fiveCards[i] % 13)
        drawnColor.append(fiveCards[i] // 13) #int division
    #print(fiveCards)
    #print(drawnSymbol)
    #print(drawnColor)
    #0 = 2, ... 8 = 10, 9 = J, 10 = Q, 11 = K, 12 = A
    #0 = Farbe1, 1 = Farbe2, 2 = Farbe3, 3 = Farbe4


def validate():
    countPairs = 0
    countDrilling = 0
    countQuadruplet = 0

    straight = False

    arr1 = np.array(drawnSymbol)
    arr2 = np.array(drawnColor)

    arr1.sort()
    if arr1[1] == arr1[0]+1:
        if arr1[2] == arr1[1]+1:
            if arr1[3] == arr1[2] + 1:
                if arr1[4] == arr1[3] + 1:
                    straight = True

    result = np.all(arr2 == arr2[0])
    if result and straight:
        if 11 in arr1 and 12 in arr1:
            dict['Royal Flush'] +=1
        else:
            dict['Straight Flush'] += 1
    elif straight:
        dict['Straße'] += 1
    elif result:
        dict['Flush'] += 1

    for i in arr1:
        count = (arr1 == i).sum()
        if count == 2:
            countPairs +=1
        if count == 3:
            countDrilling +=1
        if count == 4:
            countQuadruplet +=1

    if countPairs == 2:
        if countDrilling == 3:
            dict['Full House'] += 1
        else:
            dict['Paar'] += 1
    elif countPairs == 4:
        dict['Zwei Paare'] += 1
    elif countDrilling == 3:
        dict['Drilling'] += 1
    elif countQuadruplet == 4:
        dict['Vierling'] += 1

def percentage(list,drawTimes):
    dictPercentage['Royal Flush'] = str((list['Royal Flush']*100)/drawTimes) + '%'
    dictPercentage['Straight Flush'] = str((list['Straight Flush'] * 100) / drawTimes) + '%'
    dictPercentage['Straße'] = str((list['Straße'] * 100) / drawTimes) + '%'
    dictPercentage['Flush'] = str((list['Flush'] * 100) / drawTimes) + '%'
    dictPercentage['Full House'] = str((list['Full House'] * 100) / drawTimes) + '%'
    dictPercentage['Paar'] = str((list['Paar'] * 100) / drawTimes) + '%'
    dictPercentage['Zwei Paare'] = str((list['Zwei Paare'] * 100) / drawTimes) + '%'
    dictPercentage['Drilling'] = str((list['Drilling'] * 100) / drawTimes) + '%'
    dictPercentage['Vierling'] = str((list['Vierling'] * 100) / drawTimes) + '%'
    print(dictPercentage)

if __name__ == '__main__':
    drawTimes = input("Wie oft wollen Sie ziehen?")
    for i in range(int(drawTimes)):
        showCards(draw())
        validate()
    print(dict)
    percentage(dict,int(drawTimes))

