from math import *
print("General Form of Quadratic Equation is:") 
print("a.x*2 +b.x +c =0")
print("Here x is the variable") 
print("a,b,c are constants")

def func() :
  a = float(input("Enter value of a : ")) 
  b = float(input("Enter value of b : ")) 
  c = float(input("Enter value of c : "))
  v = input("Enter the variable name : ")

  d = (b**2)-(4*a*c)
  print("Value of discriminant(D/Delta) is = " + str(d))

  if d == 0:
    print("The equation has real and equal roots(Unique solution)") 
  elif d > 0:
    print("The equation has real and unequal roots")
  else:
    print("The equation has Imaginary roots")

  if d==0:
    s = (-b)/(2*a)
    print("The unique value of "+v+" is : "+str(round(s)))
  is_imaginary = False
  if d < 0:
    is_imaginary = True

  if is_imaginary:
    d1 = -d
    r1 = sqrt(d1)
    p1 = -b / (2 * a)
    q1 = r1 / (2 * a)

    print("The two roots are : "+v+" = "+str(p1)+" + "+str(round(q1))+"i or "+v+" = "+str(p1)+" - "+str(round(q1))+"i")
  else :
    r = sqrt(d)
    v1 = -b / 2 * a
    v2 = r / 2 * a
    print("The two roots are : "+v+" = "+str(v1-v2)+" and "+v+" = "+str(v1+v2) )

try :    
  func()
except ValueError : print("Invalid input!")
take = input("Do you want to try again?(Enter yes or no) : ")

if take.lower() == "yes":
    print("Here you go. This is your last chance.")
    func()
elif take.lower() == "no":
    print("It was good to have you:).")
else:
    print("Invalid input!,see you next time:).")
