import math #hogy tudjam használni a math.sqrt-t

def main():
    A=[0, 0] #az A pont koordinátáit tároló lista
    
    A[0]=int(input("Add meg 'A' pont x koordinátáját: ")) #az A pont első koordinátájának bekérése
    A[1]=int(input("Add meg 'A' pont y koordinátáját: ")) #az A pont második koordinátájának bekérése
    print()
    
    B=[0, 0] #a B pont koordinátáit tároló lista
    
    B[0]=int(input("Add meg 'B' pont x koordinátáját: ")) #a B pont első koordinátájának bekérése
    B[1]=int(input("Add meg 'B' pont y koordinátáját: ")) #a B pont második koordinátájának bekérése
    print()
    
    ABd=math.sqrt(((B[0]-A[0])*(B[0]-A[0]))+((B[1]-A[1])*(B[1]-A[1]))) #két pont távolságának kiszámítása "AB=d=√(b1−a1)ˇ2+(b2−a2)^2" képlettel
    
    print("Az 'A' (",A[0],",", A[1], ") és 'B' (", B[0], ",", B[1], ") pont távolsága:", ABd)

if __name__ == "__main__":
    main()