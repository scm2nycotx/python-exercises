#1. Basics
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_greeted = []
    
    def greet(self, other_person):
        print("Hello {}, I am {}!".format(other_person.name, self.name))
        self.greeting_count += 1
        self.unique_greeted.append(other_person.name)
        
#2. Back to #1 add a method 2 for Person
    def print_contact_info(self):
        print("{}'s email and phone number are:\n {}\n {}\n".format(self.name, self.email, self.phone))

    def add_friend(self, friend):
        self.friends.append(friend.name)
        
    def number_friends(self):
        print(len(self.friends))
    
    def __str__(self):
        return "Person: Name - {}, Email - {}, Phone - {}".format(self.name, self.email, self.phone)
        
    def number_unique_people_greeted(self):
        uniques = set(self.unique_greeted)
        uniques_greeted = list(uniques)
        print(len(uniques_greeted))
        
        
        

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
sam = Person("Sam", "sams@gmail.com", "303-881-1234")


#1.3
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(sam)
#1.4
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(sam)
jordan.greet(sam)
#1.5
print("{}'s email and phone number are:\n {}\n {}\n".format(sonny.name, sonny.email, sonny.phone))
#1.6
print("{}'s email and phone number are:\n {}\n {}\n".format(jordan.name, jordan.email, jordan.phone))
#1.7 another way to answer 1.5/1.6
sonny.print_contact_info()
jordan.print_contact_info()
#1.8 add a friend
sonny.add_friend(jordan)
jordan.add_friend(sonny)
sonny.add_friend(sam)
jordan.add_friend(sam)
print(sonny.friends)
print(jordan.friends)
#1.9 count number of friends
sonny.number_friends()
jordan.number_friends()
sam.number_friends()
#1.10 count number of greetings
print(sonny.greeting_count)
print(jordan.greeting_count)
print(sam.greeting_count)
#1.11 convert object to string
print(sonny)
print(jordan)
print(sam)
#1.11 number of unique people greeted
sonny.number_unique_people_greeted()
jordan.number_unique_people_greeted()
sam.number_unique_people_greeted()


#2. Make your own class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print("{} {} {}".format(self.year, self.make, self.model))
        
car1 = Vehicle("Volvo", "XC60", "2016")
car2 = Vehicle("Volkswagen", "Jetta", "2011")
car3 = Vehicle("Toyota", "Camry", "2005")
car1.print_info()
car2.print_info()
car3.print_info()


