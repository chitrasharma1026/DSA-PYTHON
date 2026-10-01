a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a**2 == b**2 + c**2: 
  print("First number is hypotenuse: ")

if b**2 == a**2 + c**2:
  print("Second number is hypotenuse: ")
  
if c**2 == b**2 + a**2:
  print("Third number is hypotenuse: ")
  
else: 
  print("This is not pythagoras")
  