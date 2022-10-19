#a Fibonacci sorozat n. eleme

def main():
    
    #Fibonacci sorozat:
    #   1 1
    #     1 2
    #       2 3
    #         3 5
    #           n n+(n-1)
    
    n=int(input("A Fibonacci sorozat hanyadik elemét kéred? ")) 
    
    fibo=[1] #lista ami a Fibonacci sorozat elemeit tartalmazza, tartalmazza az első biztosan ismert elemet az 1-et
    
    x=0 #számlálja hanyadik elemét vizsgáljuk a Fibonacci sorozatnak
    q=0 #a Fibonacci sorozat következő elemét fogja tartalmazni
    
    while x<n: #ameddig el nem éri a ciklus a keresett n. elemét a Fibonacci sorozatnak
        #y=x+1 #hanyadik eleme lesz a Fibonacci sorozatnak a következő amit kiszámol a ciklus
        z=x-1 #hanyadik eleme volt a Fibonacci sorozatnak az előző amit a következő elem kiszámolásához fog használni
        if (x==0): #ha a Fibonacci sorozat első elemét (1) vizsgáljuk, akkor nincs korábbi elem amivel össze tudnánk adni...
            q=1 #...így a sorozat következő eleme is 1 lesz
            fibo.append(q) #a Fibonacci sorozat elemeit tartalmazó listához hozzáadni a sorozat következő elemét
            #print(fibo[y])
        else: #ha a Fibonacci sorozat nem első elemét vizsgáljuk, akkor van korábbi elem amivel össze tudnánk adni...
            q=fibo[x]+fibo[z] #...így a következő elem az aktuálisan vizsgált elem (x) és az előző (z) összege lesz
            fibo.append(q) #a Fibonacci sorozat elemeit tartalmazó listához hozzáadni a sorozat következő elemét
            #print(fibo[y])
        x=x+1 #továbblépni a Fibonacci sorozat következő elemének vizsgálatára
    
    print("A Fibonacci sorozat", n,". eleme ", fibo[n]) #kiírja a Fibonacci sorozat n. elemét
        
if __name__ == "__main__":
    main()