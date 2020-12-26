print("Welcome to Pepe's Pizzeria!")
size = input("What size pizza do you want? Small - S, Medium - M, Large - L: ")
add_pepperoni = input("Do you want Pepperoni? Yes - Y, or No - N: ")
extra_cheese = input("Do you want extra cheese? Yes - Y, or No - N: ")

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is ${bill}")