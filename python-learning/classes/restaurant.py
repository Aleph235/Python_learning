class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and it makes {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, number_served):
        self.number_served += number_served


class IceCreamStand(Restaurant):
    """ A simple attempt to model an ice cream stand"""
    def __init__(self,restaurant_name, cuisine_type):
        """Initialize attributes from the parent class. Then Initialize attribute specific to the ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['choclate', 'pistache', 'fraise', 'vanille', 'noisette']
    def display_flavors(self):
        for flavor in self.flavors:
            print(f'{flavor}')

gelatteria = IceCreamStand('la gelatteria', 'ice cream')
my_restaurant = Restaurant('The bleach', 'japaneese cuisine')
restaurant_2 = Restaurant('Beyrout', 'libanese cuisine')
restaurant_3 = Restaurant('Da pepe', 'Italian cuisine')

print(f"My restaurant is {my_restaurant.restaurant_name} and we make tremendous {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

restaurant_2.set_number_served(23)
restaurant_2.increment_number_served(5)
print(f"{restaurant_2.restaurant_name} has served {restaurant_2.number_served} customers")


gelatteria.display_flavors()
