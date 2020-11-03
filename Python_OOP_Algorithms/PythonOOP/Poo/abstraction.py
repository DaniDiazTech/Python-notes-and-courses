class WashingMachine:
    def __init__(self):
        pass

    def wash(self):
        self._fill_water_tank()
        self._add_soap()
        self._wash_clothes()
        self._centrifuge()

    def _fill_water_tank(self, temperature):
        _t = temperature
        print(f"Filling up with water at {_t} °C" if 100 > _t > 0 else "Wow!, you are going to burn your clothes")

    def _add_soap(self, brand=None):
        print(f"Adding soap" if brand ==
              None else f"Adding soap of brand {brand}")

    def _wash_clothes(self):
        print("Washing clothes")

    def _centrifuge(self):
        print("spinning the clothes")

if __name__ == "__main__":
    test = WashingMachine()
    test._fill_water_tank(50)
    test._add_soap("Dove")
    test._wash_clothes()
    test._centrifuge()


