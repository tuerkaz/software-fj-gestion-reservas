import logging
import os


def configurar_logger():
    """
    Configura el sistema de logs del proyecto.
    """

    carpeta_logs = "logs"

    if not os.path.exists(carpeta_logs):
        os.makedirs(carpeta_logs)

    logging.basicConfig(
        filename=os.path.join(carpeta_logs, "sistema.log"),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

    return logging.getLogger("SoftwareFJ")