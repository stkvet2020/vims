class Pet:
    def __init__(self, name, animal, species, breed, gender, age):
        """self.name = name
        self.animal = animal
        self.species = species
        self.breed = breed
        self.gender = gender
        self.age = age"""
        self.pet_info = {'name': name, 'animal_type': animal, 'species': species,
                    'breed': breed, 'gender': gender, 'age': age}
class Owner:
    def __init__(self, f_name,l_name,street_address,city,state,postal_code,country,tel_nbr,email):
        self.owner_info = {'first name':f_name, 'last name':l_name, 'street_address':street_address,
                           'city':city, 'state':state, 'postal code':postal_code, 'country': country,
                           'telephone':tel_nbr, 'email':email}

class MedicalRecord:
    def __init__(self):
        self.records = {}

    def add_pet(self, pet):
        self.records[pet]=pet.pet_info
        print(f"This is the records[pet] dictionary: {self.records[pet]}")

    def add_owner(self, owner):
        self.records[owner]=owner.owner_info
        print(f"This is the records[owner] dictionary: {self.records[owner]}")

    def display_pet(self):
        for record in self.records:
            print(f"This comes from the display_pet method :  {record.pet_info}")
