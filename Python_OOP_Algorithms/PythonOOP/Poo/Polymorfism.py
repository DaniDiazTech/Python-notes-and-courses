class Person:
    def __init__(self, name):
      self.name = name
    
    def movement(self):
        print(f"Hi, I'm {self.name} and I move by walking")

class Cyclist(Person):
    def __init__(self, name):
        super().__init__(name)

    def movement(self):
        print(f"Hi I'm {self.name} and I move by riding my bycicle")

def main():
    camilo = Person("Camilo")
    camilo.movement()
    nairo = Person("Nairo")
    nairo.movement()

if __name__ == "__main__":
    main()
