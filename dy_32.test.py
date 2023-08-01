print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L:  ")
add_pepperoni = input("Do you want pepperoni? Y or N:  ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
  size = 15
  if add_pepperoni == "Y":
    p_small = 2
    if extra_cheese == "Y":
      extra = 1
      bill = size + p_small + extra
      print(f'Your final bill is: ${bill}')
    if extra_cheese == "N":
      bill = size + p_small
      print(f'Your final bill is: ${bill}')
  if add_pepperoni == "N":
    if extra_cheese == "N":
      bill = size
      print(f'Your final bill is: ${size}')
    if extra_cheese == "Y":
      extra = 1
      bill = size + extra
      print(f'Your final bill is: ${bill}')

 
if size == "M":
  size = 20
  if add_pepperoni == "Y":
    p_medium = 3
    if extra_cheese == "Y":
      extra = 1
      bill = size + p_medium + extra
      print(f'Your final bill is: ${bill}')
    if extra_cheese == "N":
      bill = size + p_medium
      print(f'Your final bill is: ${bill}')
  if add_pepperoni == "N":
    if extra_cheese == "N":
      bill = size
      print(f'Your final bill is: ${size}')
    if extra_cheese == "Y":
      extra = 1
      bill = size + extra
      print(f'Your final bill is: ${bill}')

if size == "L":
  size = 25
  if add_pepperoni == "Y":
    p_large = 3
    if extra_cheese == "Y":
      extra = 1
      bill = size + p_large + extra
      print(f'Your final bill is: ${bill}')
    if extra_cheese == "N":
      bill = size + p_large
      print(f'Your final bill is: ${bill}')
  if add_pepperoni == "N":
    if extra_cheese == "N":
      bill = size
      print(f'Your final bill is: ${bill}')
    if extra_cheese == "Y":
      extra = 1
      bill = size + extra
      print(f'Your final bill is: ${bill}')
