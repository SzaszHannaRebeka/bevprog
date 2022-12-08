def main():
    str1=input("Kérem az első sztringet: ")
    str2=input("Kérem a második sztringet: ")

    str1=str1.lower()
    str2=str2.lower()

    anagramma=True #feltételezzük, hogy anagramma

    for i in str1: #az első string elemeit számolja
        
        if(i!=" "):
            n1=0 #számolja hányszor van meg az első sztringben
            n2=0 #számolja hányszor van meg a második sztringben
            for k in str1: #megvizsgálja str1 betűit
                if (k==i): #ha a vizsgált betű egyezik i-vel...
                    n1=n1+1 #...hozzáadja a változóhoz, hogy tárolja hányszor van meg str1-ben
            for l in str2: #megvizsgálja str2 betűit
                if (l==i): #ha a vizsgált betű egyezik i-vel...
                    n2=n2+1 #...hozzáadja a változóhoz, hogy tárolja hányszor van meg str2-ben
        
        if(n1!=n2): #ha a két string-ben nem egyezik a betűk száma...
            anagramma=False #...megváltoztatja az anagramma értékét hamisra
            break #kilép a ciklusból mert felesleges folytatni
    
    if (anagramma==True):
        print("A két sztring anagramma.")
        
    if (anagramma==False):
        print("A két string nem anagramma.")

if __name__=="__main__":
    main()