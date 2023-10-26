class Pet:
    

# Initialize pet attributes
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = int(age)

# Set the pet's name
    def set_name(self, name):
        self.__name = name

# Set the type of animal
    def set__animal_type(self, animal_type):
        self.__animal_type = animal_type

# Set the the pet age
    def set_age(self, age):
        self.__age = int(age)
    
# Return the pet's name
    def get_name(self):
        return self.__name

# Return animal type
    def get_animal_type(self):
        return self.__animal_type

# Return pet's age
    def get_age(self):
        return self.__age