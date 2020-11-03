# Broken 
class Computer:
    def __init__(self, owner, operative_system, usage, producer="Generic"):
        """
        father class
        """
        self.owner = owner
        self.operative_system = operative_system
        self.usage = usage 
        self.producer = producer

    def greeting(self):
        return f"""
        Hi {self.owner}, this is your new computer, 
        it is mounted with {self.operative_system}, it is
        a {self.producer} computer.
        Probably you will use it for {self.usage}
        """
    def turn_on(self):
        return "Booting computer"

class LenovoLaptop(Computer):

    def __init__(self, owner, operative_system, usage, producer="Lenovo"):
        super().__init__(self)


if __name__ == "__main__":
    generic_computer = Computer("Daniel", "Linux", "Programming")
    print(generic_computer.greeting)
    print(generic_computer.turn_on)
    new_computer = LenovoLaptop("Felipe", "Windows", usage="Design")
    print(LenovoLaptop.greeting)
    print(LenovoLaptop.turn_on)
