import random

def generateArray():
    global numbers
    numbers = []
    for i in range(1,46):
        numbers.append(i)

def drawNumber():
    help1=44
    help2=1
    drawnNumbersArray = []

    for i in range(6):
        indexOfNumber = random.randint(0,help1)
        help1=help1-1
        randomNumber = numbers[indexOfNumber]
        numbers[indexOfNumber] = numbers[len(numbers)-help2]
        numbers[len(numbers)-help2] = randomNumber
        drawnNumbersArray.append(numbers[len(numbers) - help2])
        help2 = help2 + 1
    return drawnNumbersArray

def generateDict():
    dict = {}
    for i in range(1,46):
        dict[i] = 0
    return dict

def statistic():
    dictNumbers = generateDict()

    for i in range(1000):
        numbers = drawNumber()
        for i in numbers:
            dictNumbers[i] = dictNumbers[i] +1

    return dictNumbers

if __name__ == '__main__':
    generateArray()
    min = 1
    max = 45
    number_picks = 6
    print(statistic())

