def main():
    #a gúla és kúp térfogatának kiszámítása kör és téglalap területének segítségével
    
    import math #hogy tudjam használni a math.pi-t
    
    r=int(input("Add meg a kör sugarát (cm): ")) #sugár bekérése
    a=int(input("Add meg a téglalap 'a' oldalát (cm): ")) #téglalap 'a' oldalának bekérése
    b=int(input("Add meg a téglalap 'b' oldalát (cm): ")) #téglalap 'b' oldalának bekérése
    print()
    
    tkor=r*r*math.pi #kör területének meghatározása
    
    tteglalap=a*b #téglalap területének meghatározása
    
    m=int(input("Add meg a test magasságát (cm): ")) #magasság bekérése
    
    gula=(tteglalap*m)/3 #gúla térfogatának meghatározása
    
    kup=(tkor*m)/3 #kúp térfogatának meghatározása
    
    print("A gúla térfogata", gula ,"cm3 és a kúp térfogata", kup ,"cm3.") #gúla és kúp térfogatának kiiratása
    
if __name__ == "__main__":
    main()
