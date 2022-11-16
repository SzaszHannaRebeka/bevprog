def main():
    f = open('pi vers.txt', 'w') #megnyitja felülírásra a pi vers.txt-t
    txt="How I want a drink alcoholic of course After the heavy lectures involving complex functions"
    print(txt, file=f) #beleírja a pi vers.txt-be a verset
    f.close()
    
    with open('pi vers.txt', 'r') as f, open('pi szam.txt', 'w') as f2: #létrehozza felülírásra a pi szam.txt-t
        txt=f.read() #beolvassa a pi vers.txt tartalmát 
        li=txt.split(sep=' ') #listává teszi a vers szavait

        print(len(li[0]), file=f2) #a pi első számjegye a vers első szavának hossza és ezt a számot kiírja a pi szam.txt fájlba
    
    f.close()
    f2.close()
    
if __name__=="__main__":
    main()