from dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, tipo_entrada, marca):
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados
        DispositivoEntrada.__init__(self, tipo_entrada, marca)

    def __str__(self):
        return f"\n\nId Teclado: {str(self.__id_teclado)}\nTipo de Entrada: {DispositivoEntrada.get_tipo_entrada(self)}\nMarca: {DispositivoEntrada.get_marca(self)}"
