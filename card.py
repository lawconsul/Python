import random

class card:
  def __init__(self,type_card):
    cells = list(range(1,99))
    cells = random.sample(cells, k=15)
    cells = [cells[i:i+5] for i in range(0, 15, 5)]
    for i in range(0, 3):
      added = 0
      while added < 4:
        idx = random.randint(0,cells.__len__())
        cells[i] = cells[i][:idx] + [None] + cells[i][idx:]
        added += 1
    self._cells = cells
    self._type_card = type_card

  
  def type_card(self):
    return self._type_card
  
  def print_card(self):
    print("Card of {}:".format(self._type_card))
    for i in self._cells:
      print(i)
  
  def check_number(self, barel):
    for i in range(0, 3):
      if barel in self._cells[i]:
        ind = self._cells[i].index(barel)
        self._cells[i][ind] = "-"
        return True

  def check_win(self):
    for i in range(0, 3):
        for j in range(0, self._cells[i].__len__()):
            if self._cells[i][j] != "-" and self._cells[i][j] != None:
                return False
    return True