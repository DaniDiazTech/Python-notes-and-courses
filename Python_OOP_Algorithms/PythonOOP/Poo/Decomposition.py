class Car:
    # instance attribute
    
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._state = "Resting"
        self._motor = Motor(cylinders=4)

    def accelate(self, acel_type="slow"):
        
        if acel_type == "fast":
            self._motor.inyect_gasoline(10)
        else:
            self._motor.inyect_gasoline(3)

        self._state = "In_movement"


class Motor:

    def __init__(self, cylinders, motor_type="gasoline"):
        self.cylinders = cylinders
        self.motor_type = motor_type
        self._temp = 0
    
    def inyect_gasoline(self, quantity):
        pass
    