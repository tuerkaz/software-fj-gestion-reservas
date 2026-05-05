from abc import ABC, abstractmethod
from src.excepciones import DatosInvalidosError, CalculoCostoError


class Servicio(ABC):
    def __init__(self, nombre, precio_base, disponible=True):
        self._nombre = None
        self._precio_base = None
        self._disponible = disponible

        self.nombre = nombre
        self.precio_base = precio_base

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not str(valor).strip():
            raise DatosInvalidosError("El nombre del servicio no puede estar vacío.")
        self._nombre = str(valor).strip()

    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor):
        try:
            valor = float(valor)
            if valor <= 0:
                raise DatosInvalidosError("El precio base del servicio debe ser mayor que cero.")
            self._precio_base = valor
        except ValueError as error:
            raise CalculoCostoError("El precio base debe ser numérico.") from error

    @property
    def disponible(self):
        return self._disponible

    def cambiar_disponibilidad(self, estado):
        if not isinstance(estado, bool):
            raise DatosInvalidosError("La disponibilidad debe ser True o False.")
        self._disponible = estado

    def validar_duracion(self, duracion):
        try:
            duracion = float(duracion)
            if duracion <= 0:
                raise DatosInvalidosError("La duración del servicio debe ser mayor que cero.")
            return duracion
        except ValueError as error:
            raise DatosInvalidosError("La duración debe ser numérica.") from error

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass


class ReservaSala(Servicio):
    def __init__(self, nombre, precio_base, capacidad, disponible=True):
        super().__init__(nombre, precio_base, disponible)

        if capacidad <= 0:
            raise DatosInvalidosError("La capacidad de la sala debe ser mayor que cero.")

        self.capacidad = capacidad

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        duracion = self.validar_duracion(duracion)

        subtotal = self.precio_base * duracion
        subtotal -= subtotal * descuento
        total = subtotal + subtotal * impuesto

        if total <= 0:
            raise CalculoCostoError("El costo calculado no puede ser menor o igual a cero.")

        return total

    def describir_servicio(self):
        return f"Reserva de sala: {self.nombre}, capacidad: {self.capacidad} personas."


class AlquilerEquipo(Servicio):
    def __init__(self, nombre, precio_base, tipo_equipo, disponible=True):
        super().__init__(nombre, precio_base, disponible)

        if not tipo_equipo or not str(tipo_equipo).strip():
            raise DatosInvalidosError("El tipo de equipo no puede estar vacío.")

        self.tipo_equipo = str(tipo_equipo).strip()

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        duracion = self.validar_duracion(duracion)

        subtotal = self.precio_base * duracion
        subtotal += subtotal * 0.10
        subtotal -= subtotal * descuento
        total = subtotal + subtotal * impuesto

        if total <= 0:
            raise CalculoCostoError("El costo calculado no puede ser menor o igual a cero.")

        return total

    def describir_servicio(self):
        return f"Alquiler de equipo: {self.nombre}, tipo: {self.tipo_equipo}."


class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre, precio_base, area, profesional, disponible=True):
        super().__init__(nombre, precio_base, disponible)

        if not area or not str(area).strip():
            raise DatosInvalidosError("El área de asesoría no puede estar vacía.")

        if not profesional or not str(profesional).strip():
            raise DatosInvalidosError("El profesional no puede estar vacío.")

        self.area = str(area).strip()
        self.profesional = str(profesional).strip()

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        duracion = self.validar_duracion(duracion)

        subtotal = self.precio_base * duracion
        subtotal += subtotal * 0.20
        subtotal -= subtotal * descuento
        total = subtotal + subtotal * impuesto

        if total <= 0:
            raise CalculoCostoError("El costo calculado no puede ser menor o igual a cero.")

        return total

    def describir_servicio(self):
        return (
            f"Asesoría especializada: {self.nombre}, "
            f"área: {self.area}, profesional: {self.profesional}."
        )
