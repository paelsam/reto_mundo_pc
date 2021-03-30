from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.__id_computadora = Computadora.contador_computadoras
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    def get_id_computadora(self):
        return self.__id_computadora

    def set_id_computadora(self, compu):
        self.__id_computadora = compu

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_monitor(self):
        return self.__monitor

    def set_monitor(self, monitor):
        self.__monitor = monitor

    def get_teclado(self):
        return self.__teclado

    def set_teclado(self, teclado):
        self.__teclado = teclado

    def get_raton(self):
        return self.__raton

    def set_raton(self, raton):
        self.__raton = raton

    def __str__(self):
        return f"\nComputadora: {str(self.get_id_computadora())}\n\nNombre: {self.get_nombre()}\n{self.get_monitor()}\n{self.get_teclado()}\n{self.get_raton()}"
