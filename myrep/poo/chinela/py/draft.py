class Chinela:
    def __init__(self):
        self.__size: int = 0
    
    def getSize(self) -> int:
        return self.__size
    
    def setSize(self, valor: int):
        if valor >= 20 and valor <= 50:
            self.__size = valor
            return
        return print("valor nao esta no padaro de chinelas")
        
def main():

    chinela = Chinela()

    while chinela.getSize() == 0:
        
        print("digite seu tamanho de chinela")
        #size = int(input())
        chinela.setSize(30)

    print("parabens, voce comprou uma chinela tamanho", chinela.getSize())
main()