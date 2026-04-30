from src.excepciones import DatosInvalidosError, ServicioNoDisponibleError
from src.logger_config import configurar_logger


logger = configurar_logger()


def registrar_cliente(nombre, documento, correo):
    """
    Función temporal para probar validaciones de cliente.
    Más adelante será reemplazada por la clase Cliente.
    """

    try:
        if not nombre:
            raise DatosInvalidosError("El nombre del cliente no puede estar vacío.")

        if not documento:
            raise DatosInvalidosError("El documento del cliente no puede estar vacío.")

        if "@" not in correo:
            raise DatosInvalidosError("El correo ingresado no tiene un formato válido.")

    except DatosInvalidosError as error:
        logger.error(f"Error al registrar cliente: {error}")
        print(f"Error controlado: {error}")

    else:
        logger.info(f"Cliente registrado correctamente: {nombre}")
        print(f"Cliente registrado correctamente: {nombre}")

    finally:
        logger.info("Finalizó el intento de registro de cliente.")


def validar_servicio(nombre_servicio, disponible):
    """
    Función temporal para probar la disponibilidad de un servicio.
    Más adelante será reemplazada por las clases de servicios.
    """

    try:
        if not disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {nombre_servicio} no se encuentra disponible."
            )

    except ServicioNoDisponibleError as error:
        logger.error(f"Error de servicio: {error}")
        print(f"Error controlado: {error}")

    else:
        logger.info(f"Servicio disponible: {nombre_servicio}")
        print(f"Servicio disponible: {nombre_servicio}")

    finally:
        logger.info("Finalizó la validación del servicio.")


def main():
    print("Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ")
    print("-" * 75)

    registrar_cliente("Carlos Pérez", "1020304050", "carlos@gmail.com")
    registrar_cliente("", "1020304051", "cliente@gmail.com")
    registrar_cliente("Ana Gómez", "", "ana@gmail.com")
    registrar_cliente("Luis Torres", "1020304052", "correo_invalido")

    validar_servicio("Reserva de sala", True)
    validar_servicio("Asesoría especializada", False)

    print("-" * 75)
    print("Pruebas iniciales finalizadas. Revisar el archivo logs/sistema.log")


if __name__ == "__main__":
    main()