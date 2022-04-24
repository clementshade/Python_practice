T = 5
U = "monopoly"
V = "m___p___. The money game"

    
while T > 0:

    if T == 5:
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

    
    
