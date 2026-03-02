#DiceRoll.py
#Name:Scott Bassinger
#Date:03/01/2026
#Assignment:Lab6-DiceRoll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  #simulate 10,000 dice rolls
  for i in range(10000):
    #Create two dice values ranging from 1 - 6 each
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    #find the sum total of the two dice
    total = die1 + die2
    #increase the count at the relevant index
    rolls[total] += 1
  
  #print statictics for dice rolls
  print("Sum    Count   Percentage")
  for i in range(2,13):
    pct = rolls[i] / 10000 * 100
    print(f"{i}   {rolls[i]}    {pct:.2f}%")


if __name__ == '__main__':
  main()
