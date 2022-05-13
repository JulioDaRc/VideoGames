class State:
  def __init__(self):
    self.player = 0
    self.grid = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]

  def get_grid_item(self, x, y):
    dic = {
      (-200,66):[0, 0],
      (-67,66):[0, 1],
      (66,66):[0, 2],
      (-200,-67):[1, 0],
      (-67,-67):[1, 1],
      (66,-67):[1, 2],
      (-200,-200):[2, 0],
      (-67,-200):[2, 1],
      (66,-200):[2, 2]
    }
    return dic[(x, y)]