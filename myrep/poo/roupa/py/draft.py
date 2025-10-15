class Roupa:
    def __init__(self):
        self.__tamanho: str = ""

    def __str__(self) -> str:
        return f"size: ({self.__tamanho})"
    
    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self, valor: str) -> str:
        match valor:
            case "PP":
                self.__tamanho = valor
            case "P": 
                self.__tamanho = valor
            case "M":
                self.__tamanho = valor
            case "G":
                self.__tamanho = valor
            case "GG":
                self.__tamanho = valor
            case "XG":
                self.__tamanho = valor
            case _:
                print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

def main():

    roupa = Roupa()

    while(True):

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(roupa)
        elif args[0] == "size":
            tamanho: str = args[1]
            roupa.setTamanho(tamanho)
main()