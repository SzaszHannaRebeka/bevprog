class fejlesztogarda:
    def __init__(self, nev, fizetes, ev=0, rang="junior"): #alapértelmezett értéket ad az ev és rang változónak
        self.nev=nev
        self.rang=rang
        self.ev=ev
        self.fizetes=fizetes
    
    def fizetesemeles(self, osszeg=10000): #ha nem kap összeg értéket, akkor 10 000-rel számol
        self.fizetes+=osszeg #összeggel megnöveli a fizetést
        
    def evnov(self):
        self.ev+=1 #egyel növeli a bedolgozott éveket
    
    def rangja(self, ev):
        if ev==0: #ha 0 évett dolgoozott -> intern
            self.rang="intern"
        elif ev==1 | ev==2: #ha 1 vagy 2 évett dolgoozott -> junior
            self.rang="junior"
        elif ev>=3 | ev<=5: #ha 3, 4 vagy 5 évett dolgoozott -> medior
            self.rang="medior"
        elif ev>5: #ha 5 évnél többet dolgoozott -> senior
            self.rang="senior"
    
    def kiir(self):
        print("név: {0}, rang: {1}, bedolgozott év: {2}, fizetés: {3}".format(self.nev, self.rang, self.ev, self.fizetes))
        
def main():
    f1=fejlesztogarda("Bela", 200000) #ha nem adunk meg bedolgozott évet és rangot
    f2=fejlesztogarda("Beluska", 400000, 5, "medior") #ha megadunk bedolgozott évet és rangot
    f1.fizetesemeles()
    f2.fizetesemeles(20000)
    f1.evnov()
    f2.evnov()
    f1.rangja(f1.ev) #a bedolgozott évek számát tekinti az "ev" valtozó értékének
    f2.rangja(f2.ev)
    f1.kiir()
    f2.kiir()
    
if __name__=="__main__":
    main()