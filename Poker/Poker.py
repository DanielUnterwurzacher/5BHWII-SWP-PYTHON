import random

dict = {'Royal Flush':0,'Straight Flush':0,'Straße':0,'Flush':0,'Full House':0,'Paar':0,'Zwei Paare':0,'Drilling':0,'Vierling':0}
dictPercentage = {'Royal Flush':0,'Straight Flush':0,'Straße':0,'Flush':0,'Full House':0,'Paar':0,'Zwei Paare':0,'Drilling':0,'Vierling':0}
dictPercentageWiki = {'Royal Flush':'0.000154%','Straight Flush':'0.00139%','Straße':'0.3925%','Flush':'0.1965%','Full House':'0.1441%','Paar':'42.2569%','Zwei Paare':'4.7539%','Drilling':'2.1128%','Vierling':'0.0240%'}

drawnSymbol = []
drawnColor = []

def draw():
    liste = []
    for i in range(0,52):
        liste.append(i)

    for j in range(5):
        value = random.randrange(0, 52)
        while value in liste[51-j:51]:
            value = random.randrange(0, 52)

        liste[value], liste[51-j] = liste[51-j], liste[value]

    fiveCards = []
    for x in range(5):
        fiveCards.append(liste[47+x])
    return fiveCards

def showCards(fiveCards):
    for i in range(5):
        drawnSymbol.append(fiveCards[i] % 13)
        drawnColor.append(fiveCards[i] // 13) #int division
    #0 = 2, ... 8 = 10, 9 = J, 10 = Q, 11 = K, 12 = A
    #0 = Farbe1, 1 = Farbe2, 2 = Farbe3, 3 = Farbe4

def validate():
    countPair = 0
    countTriplet = 0
    countQuadruplet = 0
    straight = True

    drawnSymbol.sort()
    for i in range(1, 5):
        if drawnSymbol[i] != drawnSymbol[i - 1] + 1:
            straight = False

    result = True
    for a in drawnColor:
        if drawnColor[0] != a:
            result = False

    if result and straight:
        if 11 in drawnSymbol and 12 in drawnSymbol:
            return 'Royal Flush'
        else:
            return 'Straight Flush'
    elif straight:
        return 'Straße'

    for i in drawnSymbol:
        count = drawnSymbol.count(i)
        if count == 2:
            countPair += 1
        elif count == 3:
            countTriplet += 1
        elif count == 4:
            countQuadruplet += 1

    if countPair == 2:
        if countTriplet == 3:
            return 'Full House'
        elif result:
            return 'Flush'
        else:
            return 'Paar'
    elif result:
        return 'Flush'
    elif countPair == 4:
        return 'Zwei Paare'
    elif countTriplet == 3:
        return 'Drilling'
    elif countQuadruplet == 4:
        return 'Vierling'

    return ''

def countCombinations(combination):
    if combination == 'Paar':
        dict['Paar'] += 1
    elif combination == 'Zwei Paare':
        dict['Zwei Paare'] += 1
    elif combination == 'Drilling':
        dict['Drilling'] += 1
    elif combination == 'Vierling':
        dict['Vierling'] += 1
    elif combination == 'Straße':
        dict['Straße'] += 1
    elif combination == 'Flush':
        dict['Flush'] += 1
    elif combination == 'Full House':
        dict['Full House'] += 1
    elif combination == 'Straight Flush':
        dict['Straight Flush'] += 1
    elif combination == 'Royal Flush':
        dict['Royal Flush'] += 1

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
        drawnSymbol=[]
        drawnColor=[]
        showCards(draw())
        countCombinations(validate())
    print(dict)
    print('Berechnet:')
    percentage(dict,int(drawTimes))
    print('Recherchiert:')
    print(dictPercentageWiki)

