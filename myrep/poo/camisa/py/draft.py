class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self, valor: str):
        self.__tamanho = valor

def main():

    camisa = Camisa()
    
    while camisa.getTamanho() == "":

        print("Digite seu tamanho de roupa")
        tamanho = input()
        camisa.setTamanho(tamanho)

    print("Parabens, você comprou uma roupa tamanho", camisa.getTamanho())
main()