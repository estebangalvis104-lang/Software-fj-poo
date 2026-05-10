class Reserva:

    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def mostrar_reserva(self):

        return (
            f"{self.cliente.get_nombre()} "
            f"- {self.servicio.descripcion()} "
            f"- Estado: {self.estado}"
        )
