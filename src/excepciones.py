class ErrorSistema(Exception):
    """
    Clase base para las excepciones personalizadas del sistema.
    """
    pass


class DatosInvalidosError(ErrorSistema):
    """
    Error para datos inválidos ingresados en el sistema.
    """
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """
    Error para servicios que no se encuentran disponibles.
    """
    pass


class ReservaInvalidaError(ErrorSistema):
    """
    Error para reservas con datos incorrectos.
    """
    pass


class CalculoCostoError(ErrorSistema):
    """
    Error para problemas en el cálculo de costos.
    """
    pass


class OperacionNoPermitidaError(ErrorSistema):
    """
    Error para operaciones no permitidas.
    """
    pass