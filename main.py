from medicalrecord_2 import *


def main():
    """Instantiating a Pet
   name, animal, species, breed, gender, age)"""

    name = input("Enter pet's name : ")
    animal = input("Enter type of animal (dog , cat ...): ")
    species = input("Scientific name or common name: ")
    breed = input("Enter breed: ")
    gender = input("Enter gender: ")
    age = input("Enter age: ")

    """Actual instantiation of  the pet object"""
    pet1 = Pet(name,animal,species,breed,gender,age)

    print(f"THis is the pet info in dictionary format:{pet1.pet_info}" )

    """Instantiating a MedicalRecord. Do not forget!!!"""
    medicalrecord_1 = MedicalRecord()

    medicalrecord_1.add_pet(pet1)

    """Display Medical Record"""
    medicalrecord_1.display_pet()



if __name__ == '__main__':
    main()
