# -*- coding: utf-8 -*-
"""
Patrón: Command (Comando)
Propósito: Encapsular una petición como un objeto, permitiendo así parametrizar a los clientes con diferentes peticiones, encolar peticiones o registrar logs.
"""

from abc import ABC, abstractmethod


# Receptor: La Bombilla Inteligente (El objeto que sabe cómo actuar)
class BombillaInteligente:
    def encender(self) -> None:
        print("🕯️ La bombilla está encendida.")

    def apagar(self) -> None:
        print("🌑 La bombilla está apagada.")


# Interfaz Comando
class Comando(ABC):
    @abstractmethod
    def ejecutar(self) -> None:
        pass


# Comando Concreto para Encender
class ComandoEncender(Comando):
    def __init__(self, bombilla: BombillaInteligente) -> None:
        self.bombilla = bombilla

    def ejecutar(self) -> None:
        self.bombilla.encender()


# Comando Concreto para Apagar
class ComandoApagar(Comando):
    def __init__(self, bombilla: BombillaInteligente) -> None:
        self.bombilla = bombilla

    def ejecutar(self) -> None:
        self.bombilla.apagar()


# Invocador: El Control Remoto (Solo sabe ejecutar comandos)
class ControlRemoto:
    def __init__(self) -> None:
        self._comando = None

    def configurar_comando(self, comando: Comando) -> None:
        self._comando = comando

    def presionar_boton(self) -> None:
        if self._comando:
            self._comando.ejecutar()


if __name__ == "__main__":
    # 1. Creamos el receptor
    mi_bombilla = BombillaInteligente()

    # 2. Creamos los comandos y los asociamos a la bombilla
    luz_on = ComandoEncender(mi_bombilla)
    luz_off = ComandoApagar(mi_bombilla)

    # 3. Creamos el invocador (el mando)
    mando = ControlRemoto()

    print("--- Operando Control Remoto Inteligente ---")
    
    # Configuramos el mando para encender y presionamos
    mando.configurar_comando(luz_on)
    mando.presionar_boton()

    # Ahora lo configuramos para apagar y presionamos
    mando.configurar_comando(luz_off)
    mando.presionar_boton()
