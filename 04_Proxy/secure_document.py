# -*- coding: utf-8 -*-
"""
Patrón: Proxy (Intermediario)
Propósito: Proporcionar un sustituto o marcador de posición para otro objeto para controlar el acceso a él.
"""

from abc import ABC, abstractmethod


# Interfaz del Sujeto
class Documento(ABC):
    @abstractmethod
    def leer(self) -> None:
        pass


# Sujeto Real: El documento sensible
class DocumentoSensible(Documento):
    def __init__(self, contenido: str) -> None:
        self.contenido = contenido

    def leer(self) -> None:
        print(f"📄 Leyendo contenido sensible: {self.contenido}")


# Proxy: El intermediario de seguridad
class ProxyDocumento(Documento):
    def __init__(self, documento_real: DocumentoSensible) -> None:
        self._documento_real = documento_real
        self._password_correcta = "admin123"

    def leer(self) -> None:
        print("\n--- Intento de acceso al documento ---")
        password = input("Introduce la contraseña para leer el documento: ")
        
        if password == self._password_correcta:
            print("✅ Acceso concedido.")
            self._documento_real.leer()
        else:
            print("❌ Acceso denegado. Contraseña incorrecta.")


if __name__ == "__main__":
    # 1. Creamos el documento real (escondido detrás del proxy)
    secreto_estado = DocumentoSensible("Los planos de la Estrella de la Muerte.")

    # 2. Creamos el proxy para controlar el acceso
    proxy = ProxyDocumento(secreto_estado)

    # 3. El cliente interactúa con el proxy
    # Nota: Como es un ejemplo educativo, usamos input(), pero el patrón se trata del control de flujo.
    print("Simulando sistema de seguridad...")
    proxy.leer()
