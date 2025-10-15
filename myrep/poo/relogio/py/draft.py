class Watch:
    def __init__(self):
        self.__horas: int = 0
        self.__minutos: int = 0
        self.__segundos: int = 0

    def __str__(self) -> str:
        return f"{self.__horas:02d}:{self.__minutos:02d}:{self.__segundos:02d}"
        
    def getHoras(self) -> int:
        return self.__horas
    
    def getMinutos(self) -> int:
        return self.__minutos
    
    def getSegundos(self) -> int:
        return self.__segundos 
    
    def setTers(self, horas: int, minutos: int, segundos: int) -> int:
        if horas >= 0 and horas <= 23:
            self.__horas = horas
        else:
            print("fail: hora invalida")
    
        if minutos >= 0 and minutos <= 59:
            self.__minutos = minutos
        else:
            print("fail: minuto invalido")

        if segundos >= 0 and segundos <= 59:         
            self.__segundos = segundos
        else:
            print("fail: segundo invalido")

    def setTersInit(self, horas: int, minutos: int, segundos: int) -> int:
        if horas >= 0 and horas <= 23:
            self.__horas = horas
        else:
            self.__horas = 0
            print("fail: hora invalida")
    
        if minutos >= 0 and minutos <= 59:
            self.__minutos = minutos
        else:
            self.__minutos = 0
            print("fail: minuto invalido")

        if segundos >= 0 and segundos <= 59:         
            self.__segundos = segundos
        else:
            self.__segundos = 0
            print("fail: segundo invalido")
    
    def nextSecond(self, next: int) -> int:
        if self.__segundos < 59:
            self.__segundos += 1
        elif self.__minutos < 59:
            self.__segundos = 0
            self.__minutos += 1
        elif self.__horas < 23:
            self.__segundos = 0
            self.__minutos = 0
            self.__horas += 1 
        else:
            self.__segundos = 0
            self.__minutos = 0
            self.__horas = 0
        
def main():

    relogio = Watch()

    while(True):

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "set":
            horas: int = int(args[1])
            minutos: int = int(args[2])
            segundos: int = int(args[3])
            relogio.setTers(horas, minutos, segundos)
        elif args[0] == "next":
            relogio.nextSecond(next)
        elif args[0] == "init":
            horas: int = int(args[1])
            minutos: int = int(args[2])
            segundos: int = int(args[3])
            relogio.setTersInit(horas,minutos,segundos)


main()