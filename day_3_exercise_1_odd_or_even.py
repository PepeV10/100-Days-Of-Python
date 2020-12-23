number = int(input("Which number do you want to check? "))
num_div_by_2 = number % 2
if num_div_by_2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")