def main():
    oldalak=input("Kérem a nyomtatandó oldalakat: ")

    oldal=oldalak.split(sep=",")

    for i in oldal:
        intervallum=False #abból indul ki, hogy egy oldalt kap, nem oldalintervallumot
        for k in i: #végigmegy az oldalszám(ok) karakterein
            if (k=="-"): #ha talál a karakterek között "-"-t...
                intervallum=True #...intervallumnak tekinti
        if intervallum==True: #ha intervallum...
            oldalszam=i.split(sep="-") #...listába rakja az első és utolsó oldalt
            n=int(oldalszam[0]) #az első oldalt n értékének veszi
            print("{0},".format(n), end="")
            while True: #végtelen ciklus
                n=n+1 #megadja az intervallum következő elemét
                print("{0},".format(n), end="")
                if n==int(oldalszam[1]): #ha az oldalszám eléri az intervallum utolsó értékét...
                    break  #...megszakítja a végtelenciklust
        elif (intervallum==False): #nem intervallum
            print("{0},".format(i), end="")

if __name__=="__main__":
    main()