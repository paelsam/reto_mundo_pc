from computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from teclado import Teclado


raton1 = Raton("USB", "Hp")
raton2 = Raton("Bluetooth", "Asus")
raton3 = Raton("USB", "Gamer")

teclado1 = Teclado("USB", "Hp")
teclado2 = Teclado("Bluetooth", "Asus")
teclado3 = Teclado("USB", "Gamer")

monitor1 = Monitor("Hp", "30 pulgadas")
monitor2 = Monitor("Asus", "25 pulgadas")
monitor3 = Monitor("Gamer", "20 pulgadas")

computadora1 = Computadora("Hp", monitor1, teclado1, raton1)
computadora2 = Computadora("Asus", monitor2, teclado2, raton2)
computadora3 = Computadora("Gamer", monitor3, teclado3, raton3)

computadoras = [computadora1, computadora2]

orden1 = Orden(computadoras)
orden1.agregarComputadora(computadora3)
print(orden1)
