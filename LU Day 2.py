import random
T = int(input("Enter the maximum tickets avaiable "))
participants = [] 

for temp in range(T):
  st = "Ënter the participant name - "+ str(temp + 1) + " - " 
  name = input(st)
  participants.append(name)
print("All our participants - ",participants)
n = random.randint(0,T-1)
print("Winner of the lottery - ",participants[n])
