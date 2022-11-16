def foo(szo, beszuras): #függvény hogy hozzáadja a szót
    upgrade=beszuras + " " + szo #hozzáfűzi a keresett szóhoz amit elé kell rakni
    return upgrade

def main():
    szo=input("Add meg a szót ami elé be kell szúrni valamit: ") #bekéri a szót ami elé kell beszúrni valamit
    beszuras=input("Add meg a beszúrni valót szót: ") #bekéri mit kell beszúrni 
    txt=input("Add meg a szöveget amin változtatni kell: ") #bekéri a szöveget amiben a szó van
    
    txtupgrade="" #a szöveg javított változatát fogja tárolni

    txtli=list(txt.split()) #listát készít a szöveg szavaiból 
    
    x="" #tárolja a lista aktuálisan vizsgált elemét
    for x in txtli: #megvizsgálja a lista összes elemét
        if x==szo: #ha a vizsgált elem megegyezik a változtatni kívánt szóval 
            txtupgrade=txtupgrade + foo(szo, beszuras) + " " #hozzáfűzi a kiegészített változatát a szónak a javított szöveghez
        else: #ha nem egyezik a szó...
            txtupgrade=txtupgrade + x + " " #...akkor csak hozzzáfűzi az aktuálisat 
            
    print(txtupgrade) #kiíratja a javított változatot 
    
if __name__=="__main__":
    main()