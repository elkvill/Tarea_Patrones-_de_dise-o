# -*- coding: utf-8 -*-
"""
Patrón: Factory Method (Método Fábrica)
Propósito: Definir una interfaz para crear un objeto, pero dejar que las subclases decidan qué clase instanciar.
"""

from abc import ABC, abstractmethod


# Producto Abstracto
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass


# Producto Concreto: Email
class NotificacionEmail(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"📧 Enviando Email: {mensaje}")


# Producto Concreto: SMS
class NotificacionSMS(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"📱 Enviando SMS: {mensaje}")


# Producto Concreto: Push
class NotificacionPush(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"🔔 Enviando Notificación Push: {mensaje}")


# Creador / Fábrica
class FabricaNotificaciones:
    @staticmethod
    def crear_notificacion(tipo: str) -> Notificacion:
        """Método fábrica que decide qué objeto crear según el tipo."""
        tipos = {
            "email": NotificacionEmail,
            "sms": NotificacionSMS,
            "push": NotificacionPush
        }
        
        clase_notificacion = tipos.get(tipo.lower())
        
        if clase_notificacion:
            return clase_notificacion()
        else:
            raise ValueError(f"Tipo de notificación '{tipo}' no reconocido.")


if __name__ == "__main__":
    # Queremos enviar diferentes tipos de avisos
    tipos_a_enviar = ["email", "sms", "push"]

    print("--- Sistema de Notificaciones ---")
    for tipo in tipos_a_enviar:
        # La fábrica se encarga de instanciar la clase correcta
        notificacion = FabricaNotificaciones.crear_notificacion(tipo)
        notificacion.enviar("¡Hola! Tienes una nueva actualización de tu curso.")
