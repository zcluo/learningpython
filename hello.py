message = "Hello Python world!"
print(message)

message = "Hello Python Crash Cource world!"
print(message)

name = "luo zhicong"
print(name.title())
print(name.upper())
print(name.upper().lower())

fav_lang = " python "
print(fav_lang.rstrip())
print(fav_lang.lstrip())
print(fav_lang.strip())

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0].title())

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0,'ducati')

print(motorcycles)

del motorcycles[0]

print(motorcycles)

motorcycles.insert(0,'ducati')

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('ducati')
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
cars.reverse()
print(cars)
print(len(cars))

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
for value in range(1,10):
	print(value)
numbers = list(range(1,10))
print(numbers)
squares = []
for value in range(1,10):
	square = value ** 2
	squares.append(square)
print(squares)
digits = list(range(0,11))
print(min(digits))
print(max(digits))
print(sum(digits))
squares = [value ** 3 for value in range(1,11)]
print(squares)
for value in range(1,21):
	print(value)
largelist = list(range(1,1000001))
print(min(largelist))
print(max(largelist))
print(sum(largelist))
jishu = list(range(1,20,2))
print(jishu)
db3 = []
for value in range(3,31):
	if value%3 == 0:
		db3.append(value)
print(db3)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
age = 18
print(age == 18)
print(age >= 19)
print(age < 19)
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")
	
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

alien_0 = {'color':'green','points':5}
print(alien_0['color'])
del alien_0['points']
print(alien_0)
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
	}
print("Sarah's favorite language is " + 
	favorite_languages['sarah'].title() +
	".")
user_0 = {
	'username':'efermi',
	'first':'enrico',
	'last':'fermi',
	}
for key,value in user_0.items():
	print("\nKey: " + key);
	print("Value: " + value);
	
for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".");

for language in favorite_languages.values():
	print(language.title())

for language in set(favorite_languages.values()):
	print(language.title())
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = []
for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print('...')
print("Total number of aliens: " + str(len(aliens)))
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
name = input("Please enter your name: ")
print("Hello, " + name + "!")
age = input("How old are you? ")
print(age)
print(int(age)>=21)

current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

def greet_user(username):
	"""Greeting you"""
	print("Hello, " + username.title() + "!")
greet_user("losy")

import dog
my_dog = dog.Dog('willie',12)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
from car import Car,ElectricCar

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(25)
my_new_car.read_odometer()
my_new_car.update_odometer(2)
my_new_car.read_odometer()
my_new_car.increment_odometer(3)
my_new_car.read_odometer()	
my_tesla = ElectricCar('tesla','model_s',2018)
print(my_tesla.get_descriptive_name())	
my_tesla.describe_battery()

from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")

from random import randint
x = randint(1,20)
print(x)

with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())
	
with open('pi_digits.txt') as file_object:
	for line in file_object:
		print(line.rstrip())

with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

with open('pi_million_digits.txt') as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()
print(pi_string[:52]+"...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits!")
	
filename = 'programming.txt'
with open(filename,'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")
try:
	print(5/0)
except ZeroDivisionError:
	print("You cann't divide by zero!")
	
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.");
while True:
	first_number = input("\n First number: ")
	if first_number == 'q':
		break
	second_number = input(" Second number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)

filename = 'alice.txt'
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
else:
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + "words.")

import json
numbers = [1,3,4,5,6]
filename = 'numbers.json'
with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj)
with open(filename) as f_obj:
	numbers = json.load(f_obj)
print(numbers)

username = input("What is your name?")
filename = 'username.json'
with open(filename,'w') as f_obj:
	json.dump(username,f_obj)
print("We'll remember you when you come back, " + username + "!")
with open(filename) as f_obj:
	username = json.load(f_obj)
	print("Welcome back, " + username + "!")

