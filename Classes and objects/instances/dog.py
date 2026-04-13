#simple attempt to model a dog.
class Dog():
      def __init__(self, name, age):
            self.name=name
            self.age=age
      def sit(self):
            #Simulate a dog sittint in response to a command.
            print(self.name.title()+" is now sitting.")
      def roll_over(self):
            #simulate rolling over in response to a command. 
            print(self.name.title()+" rolled over!")

my_dog=Dog('willie', 6)


#Accessing attributes 

print("My dog's name is "+ my_dog.name.title()+'.')
print("My dog is "+str(my_dog.age)+' years old.')

#Accessing Methods or calling methods 
my_dog.sit()
my_dog.roll_over()


#calling multiple instances 
your_dog=Dog('lucy', 3)


print('My god name is '+ my_dog.name.title()+' .')
my_dog.sit()

print('YOur dog name is '+ your_dog.name.title() +'.')
print('Your dog is '+ str(your_dog.age)+'years old.')
your_dog.sit()


