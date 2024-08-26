class Animal():
    def __init__(self):
        self.species='General'
    
    def produce_sound(self):
        print('Generic Animal sound!!')
    
    def present(self):
        print('I can produce the following sound:')
        self.produce_sound()

class Dog(Animal):
    def __init__(self):
        #super().species='Canis Familiaris' #This will give error. 
        self.species='Canis Familiaris'
    
    def produce_sound(self):
        print('Woof! Woof!')

my_pet_1=Animal()
print(my_pet_1.species)
my_pet_1.present()

my_pet_2=Dog()
print(my_pet_2.species)
my_pet_2.present()