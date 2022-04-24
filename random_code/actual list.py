

name = str(input("what's Your name?"))
age = int(input("how old are you"))
gender = str(input("Boy or Girl?"))
player_data = [name , age, gender]
print(name)
print(age)
print(gender)
        
print (player_data)
if age <= 17 :
    print ("U too young bye")
elif age >= 17:
    print ("U too old bye")
else:
    print("error")

input()
pass
    

