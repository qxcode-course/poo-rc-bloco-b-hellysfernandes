class Bateria:
    def __init__(self, capacidade: int = 0):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

    def getCapacidade(self) -> int:
        return self.__capacidade
    
    def getCarga(self) -> int:
        return self.__carga
    
    def setBateriInit(self, batInit: int) -> None:
        self.__capacidade = batInit
        self.__carga = batInit

    def setDecrement(self, decrement: int) -> None:
        self.__carga -= decrement
    
    def __str__(self) -> str:
        return f"({self.__carga}/{self.__capacidade})"

class Notebook:

    bateria = Bateria()

    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None

    def getLigado(self) -> bool:
        return self.__ligado
    
    def setStatus(self) -> str:
        if self.__ligado == False:
            return "Desligado"
        return "ligado"
    
    def setLigar(self) -> None:
        if self.__bateria == None:
            print("não foi possível ligar")
            return 
        self.__ligado = True

    def setDesligar(self) -> None:
        self.__ligado = False

    def setUsar(self, usar) -> str:
        if self.__ligado == True:
            if usar <= self.bateria.__carga:
                self.bateria.setDecrement(usar)
                print(f"usado por {usar} minutos")
                return
            return "erro no if doido"
        print("erro: ligue o notebook primeiro")

    def setBateri(self) -> str:
        if self.__bateria == None:
            return "Nenhuma"
        return f"{self.__bateria}"
    
    def setBateriaIncluida(self) -> None:
        self.__bateria =  self.bateria

def main():

    notebook = Notebook()

    while True:

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(f"status: {notebook.setStatus()}, batrtia: {notebook.setBateri()}")
        elif args[0] == "ligar":
            notebook.setLigar()
        elif args[0] == "desligar":
            notebook.setDesligar()
        elif args[0] == "usar":
            usar: int = int(args[1])
            notebook.setUsar(usar)
        elif args[0] == "bateria":
            batInit: int = int(args[1])
            notebook.bateria.setBateriInit(batInit)
        elif args[0] == "mostrar":
            print(notebook.bateria)
        elif args[0] == "incluir":
            notebook.setBateriaIncluida()

main()