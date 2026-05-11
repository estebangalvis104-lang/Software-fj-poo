from cliente import Cliente
from sala import ReservaSala
from reserva import Reserva

try:

    cliente1 = Cliente(
        "Esteban",
        "esteban@gmail.com"
    )

    servicio1 = ReservaSala(
        "Sala VIP",
        50000,
        3
    )

    reserva1 = Reserva(
        cliente1,
        servicio1
    )

    reserva1.confirmar()

    print(reserva1.mostrar_reserva())

    print(
        "Costo total:",
        servicio1.calcular_costo()
    )

except Exception as e:
    print("Ocurrió un error:", e)
