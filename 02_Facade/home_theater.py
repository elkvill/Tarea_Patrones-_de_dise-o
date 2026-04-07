# -*- coding: utf-8 -*-
"""
Patrón: Facade (Fachada)
Propósito: Proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema. Define una interfaz de nivel superior que hace que el subsistema sea más fácil de usar.
"""

# Subsistema 1: Luces
class LucesAmbiente:
    def atenuar(self, nivel: int) -> None:
        print(f"💡 Luces: Atenuando al {nivel}%")

    def encender(self) -> None:
        print("💡 Luces: Encendidas al máximo")


# Subsistema 2: Proyector
class Proyector:
    def encender(self) -> None:
        print("📽️ Proyector: Encendido")

    def modo_cine(self) -> None:
        print("📽️ Proyector: Configurado en modo 4K HDR")


# Subsistema 3: Sistema de Sonido
class SistemaSonido:
    def encender(self) -> None:
        print("🔊 Sonido: Altavoces activos")

    def establecer_volumen(self, nivel: int) -> None:
        print(f"🔊 Sonido: Volumen establecido en {nivel}")


# Fachada: El "Cine en Casa"
class CineEnCasa:
    def __init__(self, luces: LucesAmbiente, proyector: Proyector, sonido: SistemaSonido) -> None:
        self.luces = luces
        self.proyector = proyector
        self.sonido = sonido

    def comenzar_pelicula(self) -> None:
        """La fachada simplifica todos los pasos complejos en un solo método."""
        print("\n--- Preparando el cine en casa... ---")
        self.luces.atenuar(10)
        self.proyector.encender()
        self.proyector.modo_cine()
        self.sonido.encender()
        self.sonido.establecer_volumen(20)
        print("--- ¡Todo listo! Disfruta la película. ---")

    def terminar_pelicula(self) -> None:
        print("\n--- Apagando el cine en casa... ---")
        self.sonido.establecer_volumen(0)
        self.proyector.encender() # En realidad sería apagar, pero mantenemos simpleza
        self.luces.encender()
        print("--- Sistema apagado. ---")


if __name__ == "__main__":
    # Creamos todos los subsistemas complejos
    mis_luces = LucesAmbiente()
    mi_proyector = Proyector()
    mi_sonido = SistemaSonido()

    # Los envolvemos en la fachada
    cine = CineEnCasa(mis_luces, mi_proyector, mi_sonido)

    # El cliente ya no necesita saber cómo encender cada cosa
    # Solo usa la fachada simplificada
    cine.comenzar_pelicula()
    
    # Cuando termina, igual de fácil
    cine.terminar_pelicula()
