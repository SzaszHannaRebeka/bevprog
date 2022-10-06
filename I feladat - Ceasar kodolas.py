def main():
    kod="kwwsv=22|rxwx1eh2gTz7z<Zj[fT" #megfejtendő kód
    
    i=0
    dekod=""
    
    while i<len(kod): #ameddig végig nem megy a kód összes betűjén
        x=chr (ord (kod[i]) - 3) #a karakter ASCII kódjából kivonni hármat így megadja a keresett betűt 
        dekod+=x #egymás után fűzni a karaktereket
        i+=1 #vizsgálja a következő karaktert
        
    print (dekod) #írja ki a dekódolt kódot
        
if __name__=="__main__":
    main()