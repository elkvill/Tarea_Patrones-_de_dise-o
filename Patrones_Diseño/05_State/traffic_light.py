# -*- coding: utf-8 -*-
"""
Patrón: State (Estado)
Propósito: Permitir que un objeto altere su comportamiento cuando su estado interno cambia. El objeto parecerá haber cambiado su clase.
"""

from abc import ABC, abstractmethod


# Estado Base
class EstadoSemaforo(ABC):
    @abstractmethod
    def reportar(self) -> None:
        pass

    @abstractmethod
    def siguiente(self, contexto: "Semaforo") -> None:
        pass


# Estado Concreto: Rojo
class EstadoRojo(EstadoSemaforo):
    def reportar(self) -> None:
        print("🔴 Semáforo en ROJO: Los vehículos deben detenerse.")

    def siguiente(self, contexto: "Semaforo") -> None:
        print("[Transición] Cambiando de Rojo a Verde...")
        contexto.establecer_estado(EstadoVerde())


# Estado Concreto: Verde
class EstadoVerde(EstadoSemaforo):
    def reportar(self) -> None:
        print("🟢 Semáforo en VERDE: Los vehículos pueden avanzar.")

    def siguiente(self, contexto: "Semaforo") -> None:
        print("[Transición] Cambiando de Verde a Amarillo...")
        contexto.establecer_estado(EstadoAmarillo())


# Estado Concreto: Amarillo
class EstadoAmarillo(EstadoSemaforo):
    def reportar(self) -> None:
        print("🟡 Semáforo en AMARILLO: Precaución, el estado va a cambiar.")

    def siguiente(self, contexto: "Semaforo") -> None:
        print("[Transición] Cambiando de Amarillo a Rojo...")
        contexto.establecer_estado(EstadoRojo())


# Contexto: El Semáforo
class Semaforo:
    def __init__(self) -> None:
        # Iniciamos en Rojo
        self._estado: EstadoSemaforo = EstadoRojo()

    def establecer_estado(self, estado: EstadoSemaforo) -> None:
        self._estado = estado

    def mostrar_situacion(self) -> None:
        self._estado.reportar()

    def cambiar(self) -> None:
        """El semáforo no sabe a qué color cambiar, le pregunta a su estado actual."""
        self._estado.siguiente(self)


if __name__ == "__main__":
    print("--- Simulador de Semáforo Inteligente ---")
    semaforo = Semaforo()

    # Ciclo de vida del semáforo
    for _ in range(4):
        semaforo.mostrar_situacion()
        semaforo.cambiar()
        print("-" * 30)
