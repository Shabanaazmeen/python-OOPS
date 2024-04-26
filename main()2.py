#main program()
from Abstractpets import PetAnimal, Birds, Wildanimals

def main():
    petanimal = PetAnimal(color="white", num_types=2, sound="medium")
    birds = Birds(color="parrot green", num_types=3, sound="melodious")
    wildanimals = Wildanimals(color="brown", num_types=1, sound="scary")

    petanimal.display_details()
    print("\n")
    birds.display_details()
    print("\n")
    wildanimals.display_details()

if _name_ == "_main_":
    main()

