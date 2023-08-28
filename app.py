

class Pion:
    position =""
    color=""
    status =""

    def __init__(self,position,status,colorrr="black"):
        self.position=position
        self.color=colorrr
        self.status =status

    def move(self)-> str:
        return f'position: {self.position} ,Color:  {self.color}  status:  {self.status}'

    def kill(self):
        pass

    def __str__(self) -> str:
        return f'position: {self.position} ,Color:  {self.color}  status:  {self.status}'

if __name__ == "__main__":
    p1 = Pion("a2",1)
    p2 = Pion("b2",0,"white")
    p3 = Pion("a4",1)
    p4 = Pion("a5",1,"black")

    print(p1)
    print(p2)