## Use python inheritance/example.py 

import Animal
import Dog


print(Animal.Animal.dogs)

print(Dog.Dog("Lassie"))

print(Animal.Animal.dogs)

# print(Animal.dogs) - AttributeError: module 'Animal' has no attribute 'dogs'
# print(Dog("Bone")) - TypeError: 'module' object is not callable
