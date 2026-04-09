#Restaurant exercise  1

class Restaurant():
      def __init__(self, restaurant_name, cusine_type):
            self.restaurant_name=restaurant_name
            self.cusine_type=cusine_type
      def describe_restaurant(self):
            print(f"The name of restaurant is {self.restaurant_name}.")
            print(f"The restaurant is {self.cusine_type} cuisine.")

      def open_restaurant(self):
            print('The restaurant is open. ')


infoo=Restaurant('Namaste Nepal', 'Nepali Authentic')
print(infoo.restaurant_name.title())  
print(infoo.cusine_type.title())


infoo.describe_restaurant()
infoo.open_restaurant()

#exercise 2
infoo2=Restaurant('Buddha', 'Indonepali')
infoo3=Restaurant('Bajara', 'indonepalichinese')
infoo4=Restaurant('Bhetghat','THai')

infoo2.describe_restaurant()
infoo3.describe_restaurant()
infoo4.describe_restaurant()
