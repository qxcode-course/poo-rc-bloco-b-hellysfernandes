class Pessoa:
    def __init__(self):
        self.__age: int = 0
        self.__name: str = ""

    def getAge(self) -> int:
        return self.__age
    
    def getName(self) -> str:
        return self.__name
    
    def setEnter(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def veAge(self) -> bool:
        if self.__age == 0:
            return False
        else: 
            return True
        
    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"
        
class Moto:

    pessoa = Pessoa()

    def __init__(self):
        self.__power: int = 1
        self.__time: int = 0
        self.__person: Pessoa | None = None

    def getPower(self) -> int:
        return self.__power
    
    def getTime(self) -> int:
        return self.__time
    
    def getPerson(self) -> str:
        return self.__person
    
    def inserir(self, person: Pessoa) -> bool:
        if self.__person != None:
            print("fail: empty motorcycle")
            return False
        self.__person = person
        return True
    
    def __str__(self) -> str:
        return f"power:{self.__power}, time:{self.__time}, person:({self.pessoa})"
    
def main():

    moto = Moto()
    pessoa = Pessoa()

    while True:

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            if pessoa.veAge() == True:
                print(moto)
            else:
                print(f"power:1, time:0, person:(empty)")
        elif args[0] == "enter":
            name: str = args[1]
            age: int = int(args[2])
            pessoa.setEnter(name, age)
main()