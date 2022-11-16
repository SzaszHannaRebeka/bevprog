def main():    
    with open("string1.py", 'r') as f, open("string1_clean.py", 'w') as f2: #megnyitja a string1.py fájlt és létrehozza a string1_clean.py fájlt
        lines=f.readlines()
        
        for line in lines:
            if (line[0]=="#"): #ha egy sor #-gel kezdődik nem csinál semmit
                pass
            else:
                for l in line:
                    if(l!="#"): #ha a karakter nem '#' kiiírja
                        print(l, end="", file=f2)
                    elif (l=="#"): #ha talál #-et a sorban akkor nem ír ki többet a sorból
                        break
                print()
                    
if __name__=="__main__":
    main()