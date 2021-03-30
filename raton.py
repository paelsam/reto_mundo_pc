from dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, tipo_entrada, marca):
        Raton.contador_ratones += 1
        self.__id_raton = Raton.contador_ratones
        DispositivoEntrada.__init__(self, tipo_entrada, marca)

    def __str__(self):
        return f"\n\nId Raton: {str(self.__id_raton)}\nTipo de Entrada: {DispositivoEntrada.get_tipo_entrada(self)}\nMarca: {DispositivoEntrada.get_marca(self)}"
