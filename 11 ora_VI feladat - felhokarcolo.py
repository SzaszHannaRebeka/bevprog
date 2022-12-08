def main():
    m=str(2**1024)
    n=len(m)
    f=""
    
    for i in range(n): #vesszővel elválasztott elemeket készít a 2^1024-en számjegyeiből
        f+=m[i] + ","
        
    fk=f.split(sep=",") #listát hoz létre a vesszővel elválasztott számjegyekből
    
    mk=0 #szomszédos felhőkarcolók magasságkülönbsége
    mko=0 #magasságkülönbségek összege
    
    i=0
    
    for i in range(n-1): #végigmegy a felhőkarcolókon az utolsó előttiig, hogy ne vizsgálja az utolsó és utolsó utáni magasságkülönbségét
        mk=int(fk[i])-int(fk[i+1]) #vizsgálja az i-edik és i+1-edik elemet
        if mk<0: #ha negatív érték a magasságkülönbség...
            mk=mk*-1 #...akkor -1-szeresét vesszük
            mko=mko+mk #hozzáadja a magasságkülönbség összegéhez
        elif mko>0: #ha pozitív a magasságkülönbség akkor...
            mko=mko+mk #...csak hozzáadja a magasságkülönbségek összegéhez
           
    print("A felhőkarcolók magasságkülönbségének összege: {0}".format(mko))
    
if __name__=="__main__":
    main()