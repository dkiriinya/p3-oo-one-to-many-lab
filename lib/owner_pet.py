class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name='tommy', pet_type=None, owner=None):
        self.name = name
        self.owner = owner
        if pet_type and pet_type.lower() not in self.PET_TYPES:
            raise Exception(f"Invalid pet type. Allowed types: {', '.join(self.PET_TYPES)}")
        self.pet_type = pet_type.lower() if pet_type else None
        self.__class__.all.append(self)

class Owner:
    def __init__(self, name='tom'):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet, Pet) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Please provide a valid Pet instance.")
        if pet not in Pet.all:
            raise Exception("Pet is not registered.")
        if pet.owner:
            raise Exception("Pet already has an owner.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    
pet1 = Pet("Whiskers", "cat")
print(Pet.all)