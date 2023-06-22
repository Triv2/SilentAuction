from replit import clear
#HINT: You can call clear() to clear the output in the console.

bidders={}

def main():
  print("Welcome to the secret auction program.")
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidders.update({name:bid})
  extra = input("Are there any other bidders? Type 'yes' or 'no'.: ").lower()
  if extra == "yes":
    clear()
    main()
  if extra == "no":
    clear()
    highest_bid=0
    auctioner=""
    for key, value in bidders.items():
      if value >=highest_bid:
        highest_bid=value
        auctioner=key
    print(f"The highest bid is ${bidders[auctioner]}, from {auctioner}!")
    


main()