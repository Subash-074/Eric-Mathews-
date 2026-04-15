#Ice Cream Stand 
#Parent class 
class Restaurant():
      def __init__(self, restaurant_name, cusine_type):
            self.restaurant_name=restaurant_name
            self.cusine_type=cusine_type
      def describe_restaurant(self):
            print(f"The name of restaurant is {self.restaurant_name}.")
            print(f"The restaurant is {self.cusine_type} store.")

      def open_restaurant(self):
            print('The restaurant is open. ')

#Child class 
class IceCreamStand(Restaurant):
      def __init__(self, restaurant_name, cusine_type):
            super().__init__(restaurant_name, cusine_type) 
            self.flavors=['vanilla', 'chocolate', 'strawberry', 'mango']
      def display_flavors(self):
            print('Available ice cream flavors.')
            for flavor in self.flavors:
                  print(f'The flavor is {flavor}.')

#creating instances 
my_icecream_stand=IceCreamStand('Cool Ice', 'Icecream')
my_icecream_stand.describe_restaurant()
my_icecream_stand.display_flavors()
