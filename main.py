from src.clientes import Cliente
from src.servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from src.reservas import Reserva
from src.excepciones import ErrorSistema
from src.logger_config import configurar_logger


logger = configurar_logger()


def ejecutar_operacion(numero, descripcion, funcion):
    """
    Ejecuta una operación del sistema y controla cualquier excepción personalizada.
    """
    print(f"\nOperación {numero}: {descripcion}")

    try:
        resultado = funcion()

    except ErrorSistema as error:
        logger.error(f"Operación {numero} fallida: {descripcion} - {error}")
        print(f"Error controlado: {error}")

    except Exception as error:
        logger.exception(f"Error inesperado en operación {numero}: {descripcion}")
        print(f"Error inesperado controlado: {error}")

    else:
        logger.info(f"Operación {numero} exitosa: {descripcion}")
        if resultado is not None:
            print(resultado)

    finally:
        logger.info(f"Finalizó la operación {numero}: {descripcion}")


def main():
    print("Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ")
    print("-" * 75)

    datos = {}

    ejecutar_operacion(
        1,
        "Registrar cliente válido",
        lambda: datos.update({
            "cliente_1": Cliente(
                "Carlos Pérez",
                "1020304050",
                "carlos@gmail.com",
                "3101234567"
            )
        }) or datos["cliente_1"]
    )

    ejecutar_operacion(
        2,
        "Registrar cliente con nombre vacío",
        lambda: Cliente(
            "",
            "1020304051",
            "cliente@gmail.com",
            "3109876543"
        )
    )

    ejecutar_operacion(
        3,
        "Registrar cliente con correo inválido",
        lambda: Cliente(
            "Ana Gómez",
            "1020304052",
            "correo_invalido",
            "3112223344"
        )
    )

    ejecutar_operacion(
        4,
        "Crear servicio de reserva de sala válido",
        lambda: datos.update({
            "sala": ReservaSala(
                "Sala de reuniones ejecutiva",
                50000,
                15,
                True
            )
        }) or datos["sala"].describir_servicio()
    )

    ejecutar_operacion(
        5,
        "Crear servicio con precio negativo",
        lambda: ReservaSala(
            "Sala inválida",
            -10000,
            10,
            True
        )
    )

    ejecutar_operacion(
        6,
        "Crear servicio de alquiler de equipo válido",
        lambda: datos.update({
            "equipo": AlquilerEquipo(
                "Video Beam Epson",
                30000,
                "Proyector",
                True
            )
        }) or datos["equipo"].describir_servicio()
    )

    ejecutar_operacion(
        7,
        "Crear asesoría especializada válida",
        lambda: datos.update({
            "asesoria": AsesoriaEspecializada(
                "Asesoría en desarrollo de software",
                80000,
                "Programación",
                "Ingeniero especialista",
                True
            )
        }) or datos["asesoria"].describir_servicio()
    )

    ejecutar_operacion(
        8,
        "Crear reserva válida",
        lambda: datos.update({
            "reserva_1": Reserva(
                datos["cliente_1"],
                datos["sala"],
                3
            )
        }) or datos["reserva_1"].resumen()
    )

    ejecutar_operacion(
        9,
        "Crear reserva con duración inválida",
        lambda: Reserva(
            datos["cliente_1"],
            datos["equipo"],
            -2
        )
    )

    ejecutar_operacion(
        10,
        "Confirmar reserva válida",
        lambda: datos["reserva_1"].confirmar() or datos["reserva_1"].resumen()
    )

    ejecutar_operacion(
        11,
        "Procesar reserva confirmada con descuento e impuesto",
        lambda: f"Costo total: ${datos['reserva_1'].procesar(descuento=0.10, impuesto=0.19):,.2f}"
    )

    ejecutar_operacion(
        12,
        "Intentar cancelar una reserva ya procesada",
        lambda: datos["reserva_1"].cancelar()
    )

    print("\n" + "-" * 75)
    print("Pruebas finalizadas. Revisar el archivo logs/sistema.log")


if __name__ == "__main__":
    main()