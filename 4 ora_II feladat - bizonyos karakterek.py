def valid(txt, chars): #függvény létrehozása
    
    van="" #a karakterek amik benne vannak a chars-ban
    
    i=0
    for i in txt: #vizsgálja a szöveg karaktereit
        k=0
        for k in chars: #vizsgálja a felhasználó által megadott karaktereket
            if (i==k): #ha a vizsgált karakterek egyeznek...
                van+=i #...fűzze hozzá az egyező karakterek string-jéhez...
                break #...és lépjen ki a második for ciklusból
    
    return van #az egyező karaktereket adja vissza

def main():
    txt=input("Add meg a vizsgált szöveget: ") #bekéri a vizsgálandó szöveget
    chars=input("Add meg a karaktereket: ") #bekéri a jó karaktereket
    
    print ("'", valid(txt, chars), "'") #meghívja valid függvényt és kiírja az egyező karaktereket
    
if __name__=="__main__":
    main()