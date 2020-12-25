year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  print("This is a Leap Year!")
elif year % 100 == 0:
  print("This is not a Leap Year!")
elif year % 400 == 0:
  print("This is a Leap Year!")
else:
  print("This is not a Leap Year!")