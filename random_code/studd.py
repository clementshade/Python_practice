class MyClass:
  x = int()
  y =int()
  pos = x,y
  name = str()
  age = int()
  def property():
    
    print("my name is",MyClass.name)
    print("my age is",MyClass.age)
    print("I can be found at",MyClass.pos)
    

print("Class testing")

Object = MyClass.property()
def move(x,y):
  while True:
    # Horizontal Velocity
    print("HV", x )
    #vertical Velocity
    print("VV", y)

MyClass.name = str(input("What is my name: "))
MyClass.age = int(input("How old am I: "))
MyClass.x = int(input("Where am I(x): "))
MyClass.y = int(input("Where am I(y): "))

Object


