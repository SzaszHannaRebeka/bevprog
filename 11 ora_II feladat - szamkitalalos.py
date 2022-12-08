import random

def main():
    i=random.randint(1, 100) #generál egy random számot

    print("I thought of a number between 1 and 100.")
    
    n=0 #számolja a próbálkozásokat
    
    while True: #végtelen ciklus
        guess=int(input("What's your guess: "))

        n=n+1 #megnöveli a próbálkozások számát minden tipp után
        if guess>i: #ha a random szám kisebb a tippnél...
            print("My number is smaller")
        elif guess<i: #ha a random szám nagyobb a tippnél...
            print("My number is larger")
        elif guess==i: #ha a random szám egyezik a tippel
            print("Good job! That's it!")
            print("Number of guesses: {0}".format(n))
            break #... kiléb a végtelenciklusból mert meglett a random szám

if __name__=="__main__":
    main()