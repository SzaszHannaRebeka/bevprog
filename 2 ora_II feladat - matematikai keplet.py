from math import sqrt


def main():
    #Implementálj 3 tetszőleges matematikai képletet!
    
    #pitagorasz tétel a^2+b^2=c^2
    print("A Pitagorasz-tétel:")
    
    a=int(input("Add meg az 'a' befogó értékét: "))
    b=int(input("Add meg a 'b' befogó értékét: "))
    c=int(input("Add meg a 'c' átfogó értékét: "))
    
    if a*a+b*b==c*c:
        print("A háromszög derékszögű.")
    else:
        print("A háromszög nem derékszögű.")
    
    print()
    
    #thalesz tétel
    print("A Thalesz-tétle")
    
    a=int(input("Add meg az A csúcsban lévő α szöget: "))
    b=int(input("Add meg a B csúcsban lévő β szöget: "))
    c=int(input("Add meg a C csúcsban lévő γ szöget: "))
    
    o=a+b+c
    
    if o==180:
        if a==90:
            print ("A BC szakasz felezőpontja a derékszögű háromszög köré írható kör középpontja.")
        elif b==90:
            print ("Az AC szakasz felezőpontja a derékszögű háromszög köré írható kör középpontja.")
        elif c==90:
            print("A BA szakasz felezőpontja a derékszögű háromszög köré írható kör középpontja.")
    elif o>180:
        print("A belső szögek összege >180.")
    elif o<180:
        print("A belső szögek összege <180.")
    else:
        print ("A háromszög nem derékszögű, így a Thalesz-tétel nem alkalmazható.")
    
    print ()
    
    #másodfokú egyenlet megoldóképlet
    print ("Másodfokú megoldóképlet: ax^2+bx+c=0")
    
    a=int(input("Add meg az 'a' értékét: "))
    b=int(input("Add meg a 'b' értékét: "))
    c=int(input("Add meg a 'c' értékét: "))
    d=b*b-4*a*c #diszkrimináns számítása
    
    if a==0:
        print("Ez nem egy másodfokű egyenlet.")
    else:
        if d>0: #ha a diszkrimináns nagyobb mint 0 akkor az egyenletnek 2 megoldása van
            x1=(-b-sqrt(d))/2*a
            x2=(-b+sqrt(d))/2*a
            print("Két megoldás van: x1=", x1, " x2=", x2)
        elif d==0: #ha a diszkrimináns 0 akkor az egyenletnek 1 megoldása van
            x=(-b-sqrt(d))/2*a
            print("Egy megoldás van: x=",x)
        else:
            print("Nincs megoldás.")
if __name__ == "__main__":
    main()