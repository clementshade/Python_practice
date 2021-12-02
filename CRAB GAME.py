T = 5
word = ["hello","bee","cheese","create","yellow","mouse","computer","game"
        ,"virtual","hero"]
hint = [
        "h _ _ l _. greetings",
        "_ _ _. One letter sounds sounds threeee",
        "_ _ e e _ e. smile for the picture",
        "y _ l l _ _. Thats not the colour of snow",
        "c _ _ a _ e. At the beginnig of time",        
        "m _ _ s _. Jerry",
        "c _ _ _ u _ e _",
        "g _ m _. this is CRAB ____" ,
        "v _ r _ u _ _. anime waifu",
        "h _ _ _. Main character in anime"
        ]



    
while T > 0:

    if T == 5:
        num = int(input("pick a number?(1-10) "))
        U = word[num - 1]
        V = hint[num - 1]
        input("welcome")
        input("This is CRAB game.")
        print(" The hint is",(V))
    print ((T),"out of 5 tries")
    y = input("Guess the word? ")
    T -=1
    if T > 1 and y.lower() != U.lower():
        print("incorrect")
    if y.lower() == U.lower():
        print ("correct")
        P = input("do u want to play again(y/n)")
        if  P.lower() == "y":
            T = 5
            continue
        if P.lower() == "n":
            print ("Bye Bye")
            break
       
    if T <= 0:
        print ("out of tries")
        print ("Game Over")
        P = input("do u want to play again(y/n)")
        if  P.lower() == "y":
            T = 5
            continue
        if P.lower() == "n":
            print ("Bye Bye")
            break

    
    
