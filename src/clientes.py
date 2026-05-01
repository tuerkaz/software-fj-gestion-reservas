from src.excepciones import DatosInvalidosError
 
 
class Cliente:
    """
    Clase que representa un cliente de la empresa Software FJ.
    Aplica encapsulamiento mediante atributos privados y validaciones.
    """
 
    def __init__(self, nombre, documento, correo, telefono):
        self.__nombre = None
        self.__documento = None
        self.__correo = None
        self.__telefono = None
 
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono
 
    @property
    def nombre(self):
        return self.__nombre
 
    @nombre.setter
    def nombre(self, valor):
        if not valor or not str(valor).strip():
            raise DatosInvalidosError("El nombre del cliente no puede estar vacío.")
        if len(str(valor).strip()) < 3:
            raise DatosInvalidosError("El nombre del cliente debe tener al menos 3 caracteres.")
        self.__nombre = str(valor).strip()
 
    @property
    def documento(self):
        return self.__documento
 
    @documento.setter
    def documento(self, valor):
        if not valor or not str(valor).strip():
            raise DatosInvalidosError("El documento del cliente no puede estar vacío.")
        if not str(valor).isdigit():
            raise DatosInvalidosError("El documento del cliente debe contener solo números.")
        if len(str(valor)) < 6:
            raise DatosInvalidosError("El documento del cliente debe tener mínimo 6 dígitos.")
        self.__documento = str(valor)
 
    @property
    def correo(self):
        return self.__correo
 
    @correo.setter
    def correo(self, valor):
        if not valor or not str(valor).strip():
            raise DatosInvalidosError("El correo del cliente no puede estar vacío.")
        if "@" not in valor or "." not in valor:
            raise DatosInvalidosError("El correo del cliente no tiene un formato válido.")
        self.__correo = str(valor).strip().lower()
 
    @property
    def telefono(self):
        return self.__telefono
 
    @telefono.setter
    def telefono(self, valor):
        if not valor or not str(valor).strip():
            raise DatosInvalidosError("El teléfono del cliente no puede estar vacío.")
        if not str(valor).isdigit():
            raise DatosInvalidosError("El teléfono debe contener solo números.")
        if len(str(valor)) < 7:
            raise DatosInvalidosError("El teléfono debe tener mínimo 7 dígitos.")
        self.__telefono = str(valor)
 
    def actualizar_contacto(self, correo=None, telefono=None):
        """
        Método con parámetros opcionales para simular sobrecarga.
        Permite actualizar correo, teléfono o ambos.
        """
        if correo is not None:
            self.correo = correo
 
        if telefono is not None:
            self.telefono = telefono
 
    def mostrar_informacion(self):
        """
        Retorna la información básica del cliente.
        """
        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )
 
    def __str__(self):
        return self.mostrar_informacion()
    