class Dog():  # Class named dog

    # class object attribute
    # samfor any instance of a class
    species = 'mammal'

    def __init__ (self, breed, name):
        # attributes
        # we take in the arguments
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

    # opertions/actions ---> Methods
    def bark(self, number): #number is an ex
        print(f'Woof! My name is {self.name}')


my_dog = Dog('lab', 'Frankie' )

type ( my_dog )

my_dog.species

my_dog.name

my_dog.bark()


'''while True:
    name = str(input('Name: '))
    age = int(input('Age: '))
    grade = float(input('Grade: '))
    option = ' '
    while option not in 'YN':
        option = str(input('New student? [Y/N]')).strip().upper()
    if option == 'N':
        break
print(my_dog
      )'''
