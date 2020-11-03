class Coor:
    def __init__(self, x, y):
      self.x = x
      self.y = y

    def distance(self, other_coor):
        x_dif = (self.x - other_coor.x) ** 2
        y_dif = (self.y - other_coor.y) ** 2

        return (x_dif + y_dif) ** 0.5

if __name__ == "__main__":
    coor_1 = Coor(3, 30)
    coor_2 = Coor(4, 20)

    print(coor_1.distance(coor_2))
    print(isinstance(coor_1, Coor))
    print(isinstance("hello",  Coor))
    print(isinstance(coor_2, Coor))
