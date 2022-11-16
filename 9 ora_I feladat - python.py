def main():
    with open("vers.txt", "r") as f: #megnyitja a vers.txt-t olvasásra
        print(f.read()) #kiírja a vers.txt tartalmát
if __name__=="__main__":
    main()