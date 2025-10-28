class Carregador:
    def __init__(self, potencia: int = 0):
        self.__potencia: int = potencia

    def getPotencia(self) -> int:
        return self.__potencia
    
    def setCarregadorInit(self, carregadorInit: int) -> None:
        self.__potencia = carregadorInit
    
    def __str__(self) -> str:
        return f"(potencia {self.__potencia})"

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
    
    def setIncrement(self, increment: int) -> None:
        self.__carga += increment

    def __str__(self) -> str:
        return f"({self.__carga}/{self.__capacidade})"

class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def getLigado(self) -> bool:
        return self.__ligado
    
    def setStatus(self) -> str:
        if self.__ligado == False:
            return "Desligado"
        return "ligado"
    
    def ligar(self) -> str:
        if self.__bateria == None and self.__carregador == None:
            print("fail: não foi possível ligar")
            return
        else:
            self.__ligado = True

    def desligar(self) -> None:
        self.__ligado = False

    def usar(self, usar: int) -> None:
        if self.__ligado == True:
            if self.__bateria != None or self.__carregador != None:
                if self.__carregador != None:
                    increment: int = usar * self.__carregador.getPotencia()
                    self.__bateria.setIncrement(increment)
                    print("Notebook utilizado com sucesso")
                    return
                elif usar >= self.__bateria.getCarga():
                    self.__ligado = False
                    print(f"usado por {self.__bateria.getCarga()} minutos, notebook desligado")
                    self.__bateria.setDecrement(self.__bateria.getCarga())
                    return
                else:
                    self.__bateria.setDecrement(usar)
                    print(f"usado por {usar} minutos")
                    return
            return "erro: capacidade maxima exedida"
        print("fail: desligado")
        return

    def setBateria(self) -> str:
        if self.__bateria == None:
            return "Nenhuma"
        return f"{self.__bateria}"
    
    def setBateriaIncluida(self, bateria: Bateria) -> None:
        self.__bateria = bateria
    
    def rmBateria(self) -> None:
        self.__bateria = None
        return "bateria removida"
    
    def setCarregador(self) -> str:
        if self.__carregador == None:
            return "Desconectado"
        return f"{self.__carregador}"
    
    def setCarregadorIncluir(self, carregador: Carregador) -> None:
        self.__carregador = carregador

def main():

    notebook = Notebook()
    bateria = Bateria()
    carregador = Carregador()

    while True:

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            if bateria.getCapacidade() == 0:
                print("Notebook: desligado")
            elif carregador.getPotencia() == 0:
                print(f"status: {notebook.setStatus()}, batrtia: {notebook.setBateria()}")
            elif carregador.getPotencia() > 0:
                print(f"status: {notebook.setStatus()}, batrtia: {notebook.setCarregador()}")
            else:
                print(f"status: {notebook.setStatus()}, batrtia: {notebook.setBateria()}, Carregador: {notebook.setCarregador()}")
                
        elif args[0] == "turn_on":
            notebook.ligar()
        elif args[0] == "desligar":
            notebook.desligar()
        elif args[0] == "use":
            usar: int = int(args[1])
            notebook.usar(usar)
        elif args[0] == "bateria":
            batInit: int = int(args[1])
            bateria.setBateriInit(batInit)
        elif args[0] == "mostrar":
            print(bateria)
        elif args[0] == "incluir":
            notebook.setBateriaIncluida(bateria)
        elif args[0] == "remover":
            notebook.rmBateria()
        elif args[0] == "set_charger":
            carregadorInit: int = int(args[1])
            carregador.setCarregadorInit(carregadorInit)
        elif args[0] == "cabo":
            print(carregador)
        elif args[0] == "conctar":
            notebook.setCarregadorIncluir(carregador)
main()