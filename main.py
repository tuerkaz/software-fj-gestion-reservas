from src.excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    OperacionNoPermitidaError
)


class Reserva:
    """
    Clase que integra un cliente, un servicio, duración y estado de la reserva.
    Permite confirmar, cancelar y procesar reservas con manejo de excepciones.
    """

    ESTADO_PENDIENTE = "Pendiente"
    ESTADO_CONFIRMADA = "Confirmada"
    ESTADO_CANCELADA = "Cancelada"
    ESTADO_PROCESADA = "Procesada"

    def __init__(self, cliente, servicio, duracion):
        if cliente is None:
            raise ReservaInvalidaError("La reserva debe tener un cliente asociado.")

        if servicio is None:
            raise ReservaInvalidaError("La reserva debe tener un servicio asociado.")

        if not servicio.disponible:
            raise ServicioNoDisponibleError("No se puede reservar un servicio no disponible.")

        try:
            duracion = float(duracion)
            if duracion <= 0:
                raise DatosInvalidosError("La duración de la reserva debe ser mayor que cero.")
        except ValueError as error:
            raise DatosInvalidosError("La duración de la reserva debe ser numérica.") from error

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = self.ESTADO_PENDIENTE
        self.costo_total = 0

    def confirmar(self):
        if self.estado == self.ESTADO_CANCELADA:
            raise OperacionNoPermitidaError("No se puede confirmar una reserva cancelada.")

        if self.estado == self.ESTADO_PROCESADA:
            raise OperacionNoPermitidaError("No se puede confirmar una reserva ya procesada.")

        self.estado = self.ESTADO_CONFIRMADA

    def cancelar(self):
        if self.estado == self.ESTADO_PROCESADA:
            raise OperacionNoPermitidaError("No se puede cancelar una reserva ya procesada.")

        if self.estado == self.ESTADO_CANCELADA:
            raise OperacionNoPermitidaError("La reserva ya se encuentra cancelada.")

        self.estado = self.ESTADO_CANCELADA

    def procesar(self, descuento=0, impuesto=0):
        if self.estado != self.ESTADO_CONFIRMADA:
            raise OperacionNoPermitidaError("Solo se pueden procesar reservas confirmadas.")

        self.costo_total = self.servicio.calcular_costo(
            self.duracion,
            descuento=descuento,
            impuesto=impuesto
        )

        self.estado = self.ESTADO_PROCESADA
        return self.costo_total

    def resumen(self):
        return (
            f"Reserva | Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self.duracion} horas | "
            f"Estado: {self.estado} | "
            f"Costo total: {self.costo_total}"
        )

    def __str__(self):
        return self.resumen()