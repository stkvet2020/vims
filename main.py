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
    """*********************************************************************************"""

    f_name = input("Enter owner's first name : ")
    l_name = input("Enter owner's last name : ")
    street_address = input("Enter owner's street address : ")
    city = input("Enter city where owner lives: ")
    state = input("Enter city where owner lives: ")
    postal_code = input("Enter postal_code of owner's address : ")
    country = input("Enter country where owner lives : ")
    tel_nbr = input("Enter owner's telephone number : ")
    email = input("Enter owner's email : ")

    """Instantiation of an owner object"""
    owner1 = Owner(f_name,l_name,street_address,city,state,postal_code,country,tel_nbr,email)

    """Instantiating a MedicalRecord. Do not forget!!!"""
    medicalrecord_1 = MedicalRecord()

    medicalrecord_1.add_pet(pet1)

    medicalrecord_1.add_owner(owner1)

    """Display Medical Record Individual Parts"""
    medicalrecord_1.display_pet(pet1)
    medicalrecord_1.display_owner(owner1)

    """Display Medical Record Object"""
    medicalrecord_1.display_record(pet1,owner1)



if __name__ == '__main__':
    main()
