
class Computer:

    def __init__(self, brand, usage="Programming"):
        self.brand = brand
        self.usage = usage
        self._cpu = "Dual core"
        self._state = None

    def get_info(self):
        print("Your computer has this aspecets:")
        print(f"brand : {brand}")
        print(f"it has a {_cpu} cpu")
        print(f"and you use it for {usage}")

    @property
    def state(self):
        """
        use of decorator
        """
        return self._state

    @state.setter
    def set_state(self, current_state):        
        if current_state == "ON" or current_state == "On" or current_state == "OFF" or current_state == "Off":
            self._state = current_state
        else:
            raise ValueError(f"The state must be ON or OFF")

if __name__ == "__main__":
    Computer_1 = Computer("Generic", "Office")
    print("1.")
    print(Computer_1.state)
    print(Computer_1._state)
    Computer_1._state = "ON"
    print(Computer_1.state)
    print(Computer_1._state)
    
    Computer_2 = Computer("Generic", "Office")
    print("2")
    print(Computer_2.state)
    print(Computer_2._state)
    Computer_2._state = "OFF"
    print(Computer_2.state)
    print(Computer_2._state)


    Computer_3 = Computer("Generic", "Office")
    print("3")
    print(Computer_3.state)
    print(Computer_3._state)
    Computer_3._state = "OFF"
    print(Computer_3.state)
    print(Computer_3._state)
