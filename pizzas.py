def describe_pet(pet_name,animal_type='dog'):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster','harry')
describe_pet(animal_type='hamster',pet_name='pot')

def get_formatted_name(first_name,last_name):
	full_name = first_name+' '+last_name;
	return full_name.title()
	
musician = get_formatted_name('jimi','hendrix')
print(musician)
