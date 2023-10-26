class Car:
    def __init__(self, year_model, make):
        # Initialize car attributes
        self.__year_model = year_model
        self.__make = make
        # Initialize car to 0
        self.__speed = 0

    # Increase car's speed by 5
    def accelerate(self):
        self.__speed += 5

    # Decrease car's speed by 5
    def brake(self):
        self.__speed -= 5

    # Return the current speed
    def get_speed(self):
        return self.__speed