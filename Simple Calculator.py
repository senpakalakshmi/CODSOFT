x=int(input("Enter the First Number :"))
y=int(input("Enter the Second Number :"))
print("The operations are:\t 1.Addition\n"
      "2.Subtraction\n"
      "3.Multiplication\n"
      "4.Division\n"
      "5.Modulus\n")
operation=input("Add/Sub/Mul/Div/Mod :")
if(operation=="Add"):
    print(x+y)
elif(operation=="Sub"):
    print(x-y)
elif(operation=="Mul"):
    print(x*y)
elif(operation=="Div"):
    print(x/y)
elif(operation=="Mod"):
    print(x%y)
else:
      print("Invalid Operation")
