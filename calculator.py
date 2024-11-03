ch=0
while ch<5:
  print("------------------------------------------")
  print("This is a simple calculator program.")
  print("Enter two numbers and an operator.")
  a=int(input("Enter first number: "))
  b=int(input("Enter second number: "))
  print("Choose an operator:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")
  ch=int(input('> '))
  if ch==1:
    print("Result: ",a+b)
  elif ch==2:
    print("Result: ",a-b)
  elif ch==3:
    print("Result: ",a*b)
  elif ch==4:
    print("Result: ",a/b)
  elif ch==5:
    print("Exiting program.")
    break
  else:
    print("Invalid choice. Please try again.")
  print("------------------------------------------")