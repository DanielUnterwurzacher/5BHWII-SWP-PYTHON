import random


class ArrayList(): 
    def __init__(self):
        self.arr = []
        self.size = 10

    def add(self, elem):
        self.arr.append(elem)
        if len(self.arr) < self.size:
            return True
        else: 
            self.size *= 2

    def delete(self, elem):  
        while self.arr.__contains__(elem):
            self.arr.remove(elem)
        if len(self.arr) <= self.size/2:  
            self.size /= 2

    def __len__(self):
        l = 0
        for i in self.arr:
            if i is not None:
                l += 1
        return l
    
    def getLast(self):
        return self.arr[-1]
    
    def getAllElements(self):
        allElements = '['
        for i in self.arr:
            allElements+=str(i)+','
        allElements = allElements[:-1]
        return allElements+"]"
    
    def getItem(self, obj):
        return self.arr.__contains__(obj)
    
    def getItemByIndex(self,index):
        return self.arr[index]
    
    def getIndex(self,obj):
        return self.arr.index(obj)
    
    def getStart(self):
        return self.arr[0]
    
    def isEmpty(self):
        if self.arr is []:
            return True

    def addByIndex(self,index,obj): 
        self.arr.insert(index,obj)
        if len(self.arr) >= self.size:
            self.size *= 2

def main():
    a = ArrayList()

    for i in range(100):
        a.add(random.randint(0,10))

    i = a.getAllElements()
    print("Liste: ")
    print(i)

    print()
    auswahl = input("Welchen Wert möchtest du löschen? ")
    a.delete(int(auswahl))

    print()
    i = a.getAllElements()
    print("Liste: ")
    print(i)
    
    print()
    print("Länge der Liste: ")
    print(len(a))
    
    print()
    print("getItem: ")
    find = input("Welchen Wert möchtest du finden? ")
    if a.getItem(find) is True:
        print("Ist Bestandteil der Liste")
    else:
        print("Ist nicht Bestandteil der Liste")
    
    print()
    print("getItemByIndex: ")
    find1 = input("Index von zu holendem Item: ")
    print(a.getItemByIndex(int(find1)))

    print()
    print("getIndex: ")
    find2 = input("Item: ")
    print(a.getIndex(int(find2)))

    print()
    print("getStart and getLast: ")
    print(a.getStart())
    print(a.getLast())

    print()
    print("isEmpty: ")
    if a.isEmpty() is True:
        print("leere Liste")
    else:
        print("befüllte Liste")

    print()
    print("addByIndex: ")
    find3 = input("An welchen Index möchtest du das Item einfügen? ")
    find4 = input("Welches Item möchtest du einfügen? ")
    a.addByIndex(int(find3),int(find4))
    y = a.getAllElements()
    print("Liste: ")
    print(y)

if __name__ == '__main__':
    main()