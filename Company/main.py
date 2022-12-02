class Person():
    def __init__(self,name,geschlecht):
        self.name = name
        self.geschlecht = geschlecht

class Mitarbeiter(Person):
    def __init__(self,name,geschlecht,firma):
        super().__init__(name,geschlecht)
        self.firma = firma

class Gruppenleiter(Mitarbeiter):
    def __init__(self,name,geschlecht,firma):
        super().__init__(name,geschlecht,firma)

class Firma():
    def __init__(self,name):
        self.name = name
        self.abteilungen = []

    def anzPersonen(self):
        anzMitarbeiter = 0
        anzGruppenleiter = 0
        for i in self.abteilungen:
            anzMitarbeiter += len(i.mitarbeiter)
            anzGruppenleiter += len(i.gruppenleiter)
        return {'Mitarbeiter':anzMitarbeiter,'Gruppenleiter':anzGruppenleiter}

    def anzAbteilungen(self):
        return len(self.abteilungen)

    def groessteAbteilung(self):
        arr=[]
        wertVorher = 0
        for i in self.abteilungen:
            if len(i.mitarbeiter) > wertVorher:
                arr.clear()
                arr.append(i.name)
                wertVorher = len(i.mitarbeiter)
            elif len(i.mitarbeiter) == wertVorher:
                arr.append(i.name)
        return arr

    def prozentGeschlecht(self):
        maenner = 0
        frauen = 0
        for i in self.abteilungen:
            for x in i.mitarbeiter:
                if x.geschlecht == 'M':
                    maenner+=1
                elif x.geschlecht == 'W':
                    frauen+=1
            for y in i.gruppenleiter:
                if y.geschlecht == 'M':
                    maenner+=1
                elif y.geschlecht == 'W':
                    frauen+=1
        return {'Männer': str(round((maenner*100)/(maenner+frauen),1))+'%','Frauen':str(round((frauen*100)/(maenner+frauen),1))+'%'}

class Abteilung():
    def __init__(self,name):
        self.name = name
        self.gruppenleiter = []
        self.mitarbeiter = []

if __name__ == '__main__':
    firma = Firma('danielAG')
    gl = Gruppenleiter('Daniel','M',firma)
    gl2 = Gruppenleiter('Susi', 'W', firma)
    gl3 = Gruppenleiter('Franz', 'M', firma)
    ma = Mitarbeiter('Niklas', 'M',firma)
    ma2 = Mitarbeiter('Fabian', 'M', firma)
    ma3 = Mitarbeiter('Jakob', 'M', firma)
    ma4 = Mitarbeiter('Lena', 'W', firma)
    ab = Abteilung('Informatik')
    ab2 = Abteilung('Buchhaltung')
    firma.abteilungen.append(ab)
    firma.abteilungen.append(ab2)
    ab.gruppenleiter.append(gl)
    ab.gruppenleiter.append(gl2)
    ab2.gruppenleiter.append(gl3)
    ab.mitarbeiter.append(ma)
    ab.mitarbeiter.append(ma2)
    ab2.mitarbeiter.append(ma3)
    ab2.mitarbeiter.append(ma4)

    print('Anzahl Abteilungen:')
    print(firma.anzAbteilungen())
    print('Anzahl Personen:')
    print(firma.anzPersonen())
    print('Mitarbeiterstärkste Abteilung(en):')
    print(firma.groessteAbteilung())
    print('Verhältnis Frauen und Männer:')
    print(firma.prozentGeschlecht())