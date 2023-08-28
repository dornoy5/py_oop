from enum import Enum
import pickle

def save_zoo(zoo, filename):
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)

def load_zoo(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    
class Actions(Enum):
    ADD_ANIMAL =0
    PRINT_ALL =1
    PRINT_PREDATORS =2
    PRINT_VEGY =3
    EXIT =4

class Animal_type(Enum):
    LION =0
    SHARK =1
    FISH =2

class Animal:
    def eat(self):
        print("eat")

    def move(self):
        pass

    def __str__(self) -> str:
        return   __class__.__name__

class Fish(Animal):
    def __init__(self,age=2) -> None:
        self.age=age
    
    def move(self):
        print("Swim")

    def __str__(self) -> str:
        return  " ilove to swim"
class Shark(Animal):
    def __init__(self,age=2) -> None:
        self.age=age
    
    def move(self):
        print("Swim")

    def kill(self):
        print("nemo yami")

    def __str__(self) -> str:
        return  " ilove to swim"
class Lion(Animal):
    counter=0

    def move(self):
        print("Walk")

    def __init__(self,age,gender,name) -> None:
        Lion.counter =Lion.counter+1
        self.age=age
        self.gender="female"
        self.name ="yossi"
    
    def __str__(self) -> str:
        return  self.gender + self.name
zoo=[]
def menu():
    while(True):
        for i in Actions:
            print(i.value , i.name)
        user_selection =Actions( int( input("what 2 do?")))
        if user_selection == Actions.EXIT: return
        if user_selection == Actions.ADD_ANIMAL: add_animal()
        if user_selection == Actions.PRINT_ALL: 
            for animal in zoo:
                print(animal)
        if user_selection == Actions.PRINT_PREDATORS: 
            for anim in zoo:
                if isinstance(anim,Lion) or isinstance(anim,Shark):
                    anim.move()
                
        print(user_selection.name)

def add_animal():
    for i in Animal_type:
            print(i.value , i.name)
    user_selection =Animal_type( int( input("what animal 2 add?")))
    if user_selection == Animal_type.FISH :zoo.append(Fish(5))
    if user_selection == Animal_type.LION :zoo.append(Lion(3,"male","mufasa"))
    if user_selection == Animal_type.SHARK :zoo.append(Shark(3))
    

if __name__ == "__main__":
    zoo = load_zoo("zoo_data.pkl")
    menu()
    save_zoo(zoo, "zoo_data.pkl")
    
