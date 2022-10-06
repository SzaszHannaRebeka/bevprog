def konverter(a): #létrehozza a fügvényt
    bi="" #a bináris formát tárolja
    h=1 #a hányados kezdőértéke hogy elinduljon a while függvény
    while (h>0): #ameddig a számolás a végére nem ér
        h=a//2 #ossza el 2-vel a kezdeti számot
        m=a-h*2 #a maradékot megkapjuk ha a számból kivonjuk a hányados kétszeresét
        bi+=str(m) #a maradékot hozzáfűzi a bináris alakot tároló stringhez 
        a=h #a hányadossal folytatja a ciklus a számítást
        
    return bi #a bináris alakkal térjen vissza
def main():
    a=int(input("Add meg a bináris alakban kért számot: ")) #elkéri milyen számnak keresi a bináris alakját

    print(konverter(a)) #meghívja a függvényt és kiírja a bináris alakot 
          
if __name__=="__main__":
    main()