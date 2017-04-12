#Sort of faulty
answer = 42

guess = False
while guess == False:
  try:
    x = input("Guess a number: ")
    if int(x) > answer:
      print("Guess lower")
    elif int(x) < answer:
      print("Guess higher")
    elif int(x) == answer:
      print("You win!")
      guess = True
  except ValueError:
      print("That is not a number")
