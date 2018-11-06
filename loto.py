#!/usr/bin/python3
import random
from card import card

class loto():
  def __init__(self):
    self.barels = []

  def play(self):
    cards = [card('user'), card('ai')]
    for i in cards:
      i.print_card()

    barels = list(range(1,99))
    while (barels.__len__() > 0):
      idx = random.randint(0,barels.__len__()-1)
      barel = barels[idx]
      barels.remove(barel)
      count_barel = barels.__len__()
    
      ans = str(input("Check burel {} lost: {}, YN: ".format(barel, count_barel)))
      if ans == "Y":
        if cards[0].check_number(barel) == False:
          print("Game over")
          #return

      elif ans == "N":
        if cards[0].check_number(barel) == True:
          print("Game over")
          #return

      cards[1].check_number(barel)
      
      for i in cards:
        if i.check_win():
          print("Win of {}".format(i.type_card()))
          return

      for i in cards:
        i.print_card()
  