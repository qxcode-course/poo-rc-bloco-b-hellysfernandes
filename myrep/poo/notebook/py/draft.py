class Notebook:
    def __init__(self):
        self.__ligado: bool = False

    def getLigado(self) -> bool:
        return self.__ligado
    
    def setStatus(self) -> str:
        if self.__ligado == False:
            return "Desligado"
        return "ligado"
    
    def setLigar(self) -> None:
        self.__ligado = True

    def setDesligar(self) -> None:
        self.__ligado = False

    def setUsar(self, usar) -> str:
        if self.__ligado == True:
            print(f"usado por {usar} minutos")
            return
        print("erro: ligue o notebook primeiro")
    
def main():

    notebook = Notebook()

    while True:

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(f"status: {notebook.setStatus()}")
        elif args[0] == "ligar":
            notebook.setLigar()
        elif args[0] == "desligar":
            notebook.setDesligar()
        elif args[0] == "usar":
            usar: int = int(args[1])
            notebook.setUsar(usar)
main()