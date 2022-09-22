def main():
    #konyhasó mennyisége és maradékelemek mennyisége - 2Na + Cl2 = 2 NaCl
    
    natrium=int(input("Add meg Na mennyiségét: "))
    klor=int(input("Add meg Cl2 mennyiségét: "))
    print()
    nacl=0
    na=0
    cl=0
    
    # 2 Na + Cl2 = 2 NaCl
    # 2x Na + xCl2 = 2x NaCl
    
    if klor*2==natrium:
        nacl=natrium
        print("Létrejött só: ", nacl)
        print("Maradék Na: ", na)
        print("Maradék Cl2: ", cl)
    elif klor*2>natrium:
        nacl=natrium
        cl=(klor*2-natrium)/2
        print("Létrejött só: ", nacl)
        print("Maradék Na: ", na)
        print("Maradék Cl2: ", cl)
    elif klor*2<natrium:
        nacl=natrium
        na=natrium-klor*2
        print("Létrejött só: ", nacl)
        print("Maradék Na: ", na)
        print("Maradék Cl2: ", cl)
    else:
        print("Nem jön létre só.")
    
if __name__ == "__main__":
    main()