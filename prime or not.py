def PrONPr():
  a = int(input("Enter a number : "))
  n = 0
  for i in range(1,a+1):
    if a%i==0:
      n = n + 1
    re = n
  if re>2:
    print(a,"is not a prime number.")
  elif re==2:
    print(a,"is a prime number.")
PrONPr()
