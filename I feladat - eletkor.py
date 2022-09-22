def main():
    #Kérd be egy felhasználó életkorát, és döntsd el hogy...
    age = int(input("Add meg az életkorod: "))
    print()
    
    #1. ...fogyaszthat-e legálisan alkoholt Amerikában? (21 év)
    if age>=21:
        print("Legálisan fogyaszthatsz alkoholt Amerikában.")
    elif age==20:
        print("Nemsoká legálisan fogyaszthatsz majd alkoholt Amerikában.")
    else:
        print("Legaláisan nem fogyaszthatsz alkoholt Amerikában.")
    
    #2. ...vásárolhat-e dohányterméket Magyarországon? (18 év)
    if age>=18:
        print("Vásárolhatsz dohányterméket Magyarországon.")
    elif age==17:
        print("Nemsoká vásárolhatsz dohányterméket Magyarországon.")
    else:
        print("Nem vásárolhatsz dohányterméket Magyarországon.")
    
    #3. ...szerezhet-e jogosítványt? (16 év)
    if age>=16:
        print("Szerezhetsz jogosítványt.")
    elif age==15:
        print("Nemsoká szerezhetsz jogosítványt.")
    else:
        print("Nem szerezhetsz jogosítványt.")
    
    #4. ...megnézheti-e egyedül a Shrek 2-t? (12 év)
    if age>=12:
        print("Megnézheted egyedül a Shrek 2-t.")
    elif age==11:
        print("Nemsoká megnézheted egyedül a Shrek 2-t.")
    else:
        print("Nem nézheted meg egyedül a Shrek 2-t.")
    
if __name__ == "__main__":
    main()