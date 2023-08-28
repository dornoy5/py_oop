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
        return  __class__.__name__

if __name__ == "__main__":
    f1 = Fish()
    
    l1 = Lion(12,"male","mmm")
    l2 = Lion(12,"male","mmm")
    l3 = Lion(12,"male","mmm")
    l1.move()
    f1.move()
    f1.eat()
