import random


class ListElement:
    def __init__(self,obj):
        self.obj = obj
        self.nextElem = None

    def setNextElement(self,next):
        self.nextElem = next

    def getNextElement(self):
        return self.nextElem
    
    def getObject(self):
        return self.obj

class OwnList:
    first = ListElement(None)

    def getLast(self):
        i = self.first
        while i.getNextElement() is not None:
            i = i.getNextElement()
        return i

    def add(self, obj):
        newElement = ListElement(obj)
        if self.first.obj is None:
            self.first = newElement
            return
        lastElement = self.getLast()
        lastElement.setNextElement(newElement)

    def len(self):
        length = 0
        help = self.first
        if self.first is None:
            return 0
        while help is not None:
            length += 1
            help = help.getNextElement()
        return length

    def getAllElements(self):
        help = self.first
        allElements = '['
        while help is not None:
            allElements+=str(help.obj)+','
            help = help.getNextElement()
        allElements = allElements[:-1]
        return allElements+"]"
    
    def delete(self,object):
        el = self.first
        next = el.getNextElement()
        while next is not None and el.obj != object:
            if next.obj == object:
                if next.getNextElement() is not None :
                    el.setNextElement(next.getNextElement())
                else:
                    el.setNextElement(None)
            el = el.getNextElement()
            next = el.getNextElement()        

def main():
    l = OwnList()

    #auswahl = input("Wie groß soll deine Liste sein? ")
    for i in range(100):
        l.add(random.randint(0,100))
    
    #auswahl = input("Welchen Wert möchtest du löschen? ")
    l.delete(44)
    
    print("Länge der Liste: ")
    print(l.len())
    i = l.getAllElements()
    print("Liste: ")
    print(i)

if __name__ == '__main__':
    main()