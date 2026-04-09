#Users 

class User():
      def __init__(self, first_name, last_name,address, nationality):
            self.first_name=first_name
            self.last_name=last_name
            self.address=address
            self.nationality=nationality
      def describe_user(self):
            print(f"First Name of User is {self.first_name().title()}")
            print(f"Last Name of user is {self.last_name().title()}")
            print(f"Address of user is {self.address().title()}")
            print(f"The nationality of user is {self.nationlaity().title()}")
      def greet_user(self):
            print(f"Hello {self.first_name().title()}, You are welcome to work in Amazon")

