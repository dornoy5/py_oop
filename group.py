class Human:

    def __init__(self,first_name,last_name) -> None:
        self.first_name=first_name
        self.last_name=last_name

    def __str__(self) -> str:
        return f'first_name:{self.first_name} last name: {self.last_name}'
class Test:
    def __init__(self,type,grade) -> None:
        type =""
        grade =0
    

class Student(Human):
    
    def test(self):

        print(self.first_name ,"is doing a test")

    
    def __init__(self,first_name, last_name="waga") -> None:
        super().__init__(first_name, last_name)
        self.test_lst=[]

    def add_test(self,type,grade):
        self.test_lst.append(Test(type,grade))

class Worker(Human):
    def work(self):
        print("work")

    def __init__(self, first_name, last_name) -> None:
        super().__init__("waga", last_name)
        self.salary    =100

    def __str__(self) -> str:
        return super().__str__() + str(self.salary )


class Simple(Worker):

    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.salary =10

class Manager(Worker):

    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.salary =200

if __name__ == "__main__":
    s1 = Student("Itay")
    s2 = Student("Maya")
    w1 =Worker("aaa","bbb")
    
    my_team =[s1,w1,s2]
    for x in my_team:
        if issubclass(type(x),Student) :
            x.test()
        if issubclass(type(x),Worker):
            x.work() 

    # print (issubclass(Worker,Student))
    # print(w1)