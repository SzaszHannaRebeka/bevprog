#tükörszám-e a bekért szám

def main():
    
    x=input("Addj meg egy számot: ") #szám bekérése
        
    y=x [::-1] #a bekért szám visszafele felírva
    
    if y==x: #ha a szám és tükre egyenlő
        print("A megadott szám tükörszám.")
    else:
        print("A megadott szám nem tükörszám.")
    
if __name__ == "__main__":
    main()