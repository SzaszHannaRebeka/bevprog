class Verem: #deklarálja az osztályt
    
    def __init__(self):
        self.szamok=[] #létrehozza a szamok listát a számjegyek tárolására
    
    def ures(self):
        if len(self.szamok)==0: #ha a lista hossza 0...
            return True #...igazat ad
        elif len(self.szamok)!=0: #ha a lista hossza nem 0...
            return False #...hamisat ad
    
    def betesz(self, szam):
        self.szamok.append(szam) #hozzáadja a megadott számot
    
    def meret(self):
        return len(self.szamok) #megmondja a lista hosszát
    
    def kivesz(self):
        try: #megpróbálja végrehajtani a kódot
            n=self.szamok[-1] #megadja a legutoljára berakott elemet
            i=1
            li=[] #létrehoz egy új listát
            for i in range(len(self.szamok)): #belerakja az új listába a régit
                li.append(self.szamok[i])
            self.szamok=[] #kiüríti a régi listát
            i=1
            for i in range(len(li)-1): #a régi listába belerakja az új összes kivéve utolsó elemét
                self.szamok.append(li[i])
        except IndexError: #ha a lista üres akkor...
            n="None" #...n értéke None, jelezve, hogy a lista üres
        return n

def main():
    v = Verem()
    print(v.szamok) 
    print(v.ures())
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v.szamok) 
    print(v.meret())
    print(v.ures()) 
    x = v.kivesz()
    print(x) 
    print(v.szamok) 
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)         

if __name__=="__main__":
    main()