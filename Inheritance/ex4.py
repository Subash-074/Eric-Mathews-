#Electric car final version 
"""
You don't always have to start from scratch when writing a class. If the class you're writing is a specialized version of another class you wrote, you can use inheritance. 

When one class inherits form another, it automatically takes on all the attributes and methods of the first class. 

The original class is called parent class, and the new class is the child class. 

The child class inherits every attribute and method from its parent class but it is also free to define new attributes and methods of its own 

"""

#Parent class 

class Car():
      def __init__(self, make, model, year ):
            self.make=make
            self.model=model
            self.year=year
            self.odometer_reading=0

      def full_name_of_car(self):
            long_name=str(self.year)+' '+self.make+' '+self.model
            return long_name.title()
      
      def read_odometer(self):
            print('This car has'+str(self.odometer_reading)+'miles on it. ')
      def update_odometer(self, mileage):
            if mileage>=self.odometer_reading:
                  self.odometer_reading=mileage
            else:
                  print("You can't roll back an odometer ")
      def increment_odometer(self, miles):
            self.odometer_reading+=miles




#Instances/Objects  as attribute 


#Here we want to go into depths of battery of electric car and provide each and every individual detail

class Battery():
      #A simple attempt to model a battery for electric car 
      def __init__(self, battery_size=70):
            self.battery_size=battery_size
      def describe_battery(self):
            print("This car has a " +str(self.battery_size)+"-kWh battery. ")
      def get_range(self):
             #let's print a statement that prints the rage this battery provides. 
            if self.battery_size==70:
                  range=240
            elif self.battery_size==85:
                  range=270
            message='This car can go approximately '+str(range)
            message+=' miles on a full charge.'
            print(message)
      def upgrade_battery(self):
            if self.battery_size!=85:
                  self.battery_size=85




#child class 

class ElectricCar(Car):
      #represents aspects of a car, specic to electric vehicle 
      def __init__(self, make, model, year):
            #initialize all the attributes of parent class
            super().__init__(make, model, year)
            #here we already called all the attributes of parent class now we can also add specific attribute as need 
            #adding attributes on child calss can be done by 
            # self.attribute=attribute

            #using instances or objects as attributes inside child class-- after calass is called it becomes object.

            self.battery=Battery() 

      def describe_battery(self):
            self.battery.describe_battery()
            self.battery.get_range()
            self.battery.upgrade_battery()
            self.battery.get_range()






my_tesla=ElectricCar('Tesla', 'Model S', 2016)
print(my_tesla.full_name_of_car())
my_tesla.describe_battery()

