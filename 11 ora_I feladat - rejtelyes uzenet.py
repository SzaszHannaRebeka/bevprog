def main():
    txt="""Cbcq Dgyk!

    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

    Ynyb"""

    txt1="    " #négy szóközzel beljebb kezd minden sort így négy szóközt tesz az első sor elé, hogy a formázás stimmeljen
    for i in txt:
        #n=0
        letter = i.isalpha() #vizsgálja betű-e az adott karakter
        if letter==True: #ha betű az adott karakter...
            up = i.isupper() #vizsgálja, hogy betű-e az adott karakter
            if up == True: #ha nagybetű az adott karakter...
                l=i.lower() #...akkor kicsivé változtatja
            elif up == False: #ha nem nagybetű...
                l=i #...békén hagyja
            n=ord(l) #lekéri az ASCII kódot
            n=n+2 #két betűvel van elcsúsztatva a kód ezért kettőt kell adni az ASCII kódhoz
            if (n>ord('z')): #ha az ASCII kód a növelés után nagyobb mint a 'z' betű kódja..
                m=n-ord('z') #akkor n-ből kivonja a 'z' kódját, hogy megkapja hanyadik betű kéne a-tól számolva
                m=ord('a')+(m-1) #a ASCII kódjához hozzáadja, hogy hanyadik betű kéne a-tól számítva (m-1-et ad hozzá, mert ha n-ord('z') 1-et ad akkor az 'a'-t jelenti, nem a+1-et)
                k=chr(m) #megadja a dekódolt betűt
                if up == False: #ha a nem nagybetű volt az eredeti karakter...
                    txt1+=k #...akkor békénhagyja
                elif up == True: #ha nagybetű volt az eredeti...
                    k=k.upper() #...nagybetűvé alakítja
                    txt1+=k 
            elif (n<ord('z')): #
                m=n
                k=chr(m)
                if up == False: #lásd 25-29. sor
                    txt1+=k
                elif up == True:
                    k=k.upper()
                    txt1+=k
            #output=chr(n)
        else:
            txt1+=i
        letter=True
    
    txtli=txt1.splitlines() #listába teszi a dekódolt szöveget hogy soronként lehessen dolgozni vele
    
    txtfin="" #a végső változat
    
    for i in txtli: #megvizsgálja a sorokat
        try: 
            if i[0]==" ": #ha szóközzel kezdődik...
                txtfin+=i[4:len(i)] #...akkor leszedi az első négy szóközt a sor elejéről és beteszi a végső változatot tartalmazó stringbe
                txtfin+="\n"
        except IndexError: #mivel egy üres sornak nincsenek elemei így az i[0] hibát fog adni ("IndexError")... 
            txtfin+="\n" #...mikor ez történik csak hozzáad egy üres sort
        
    print(txtfin) #kiiratja a dekódolt és formázott szöveget
    
if __name__=="__main__":
    main()