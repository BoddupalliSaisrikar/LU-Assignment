def calc():
  n = int(input("""Enter which mathematical operation you want to perform : \n1 for Addition ,\n2 for Multiplication ,\n3 for Division ,\n4 for subtraction ,
5 for power of numbers ,\n6 for remainder between two numbers ,\n7 for integer division ,\n8 for power of e ,\n9 for percentage ,\n10 for root of a number : """))
  if n==1:
    a=int(input("Number of items to be performed : "))
    su = 0
    for i in range(1,a+1):
      print("Enter value-",i,":",end=" ")
      na=int(input())
      su = su + na
    print("Your result is :",su)
  elif n==2:
    a=int(input("Number of items to be performed : "))
    mu = 1
    for i in range(1,a+1):
      print("Enter value-",i,":",end=" ")
      na=int(input())
      mu = mu * na
    print("Your result is :",mu)
  elif n==3:
    a=int(input("Number of items to be performed : "))
    di = 1
    for i in range(1,a+1):
      print("Enter value-",i,":",end=" ")
      na=int(input())
      if i == 1:
        di = na 
      elif i>1:
        di = di / na
    print("Your result is :",di)
  elif n==4:
    a=int(input("Number of items to be performed : "))
    su = 0
    for i in range(1,a+1):
      print("Enter value-",i,":",end=" ")
      na = int(input()) 
      if i == 1:
        su = na 
      elif i>1:
        su = su - na 
    print("Your result is :",su)
  elif n==5:
    a=int(input("Number of items to be performed : "))
    po = 1
    for i in range(1,a+1):
      print("Enter value-",i,":",end=" ")
      na=int(input())
      if i == 1:
        po = na 
      elif i>1:
        po = po ** na
    print("Your result is :",po)
  elif n==6:
    a=int(input("Number of items to be performed : "))
    re = 0
    for i in range(1,a+1):
      print("Enter value-",i,":",end=" ")
      na=int(input())
      if i == 1:
        re = na 
      elif i>1:
        re = re % na
    print("Your result is :",re)
  elif n==7:
    a=int(input("Number of items to be performed : "))
    idi = 1
    for i in range(1,a+1):
      print("Enter value-",i,":",end=" ")
      na=int(input())
      if i == 1:
        idi = na 
      elif i>1:
        idi = idi % na
    print("Your result is :",idi)
  elif n==8:
    a=int(input("Which power of 'e' to be raised : "))
    e = 2.71828
    ep = e ** a 
    print("Your result is :",ep)
  elif n==9:
    a = int(input("Enter the number : "))
    print("what percentage of",a,"needed : ",end=" ")
    b = int(input())
    pr = (a*b)/100
    print("Your result is :",pr)
  elif n==10:
    a = int(input("Enter the value :"))
    print("Which numbered root to be performed for",a,":",end=" ")
    b = int(input())
    rr = a ** (1/b)
    print("Your result is :",rr)
  else:
    print("Enter the correct value in the given range ")
    calc()
calc()
