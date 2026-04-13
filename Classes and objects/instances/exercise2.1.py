#Numbers Served 
class Number:
      def __init__(self, number_served=0):
            self.number_served=number_served
      def set_number_served(self):
            print(f"The number of customers served till now is {self.number_served}")
      def increment_number_served(self,number):
            self.number_served+=number
            print(f'The number of customer served now is {self.number_served}')

progress=Number()
progress.set_number_served()
progress.increment_number_served(30)