# -*- coding: utf-8 -*-
"""
Patrón: Decorator (Decorador)
Propósito: Añadir responsabilidades adicionales a un objeto de manera dinámica. Los decoradores proporcionan una alternativa flexible a la herencia para extender la funcionalidad.
"""

from abc import ABC, abstractmethod


# Componente Abstracto
class Bebida(ABC):
    @abstractmethod
    def obtener_descripcion(self) -> str:
        pass

    @abstractmethod
    def calcular_costo(self) -> float:
        pass


# Componente Concreto: Café Simple
class CafeSimple(Bebida):
    def obtener_descripcion(self) -> str:
        return "Café Solo"

    def calcular_costo(self) -> float:
        return 2.50


# Decorador Base
class AgregadoDecorador(Bebida):
    def __init__(self, bebida: Bebida) -> None:
        self._bebida = bebida

    def obtener_descripcion(self) -> str:
        return self._bebida.obtener_descripcion()

    def calcular_costo(self) -> float:
        return self._bebida.calcular_costo()


# Decorador Concreto: Leche
class ConLeche(AgregadoDecorador):
    def obtener_descripcion(self) -> str:
        return f"{self._bebida.obtener_descripcion()}, con Leche"

    def calcular_costo(self) -> float:
        return self._bebida.calcular_costo() + 0.50


# Decorador Concreto: Azúcar
class ConAzucar(AgregadoDecorador):
    def obtener_descripcion(self) -> str:
        return f"{self._bebida.obtener_descripcion()}, con Azúcar"

    def calcular_costo(self) -> float:
        return self._bebida.calcular_costo() + 0.25


if __name__ == "__main__":
    print("--- Cafetería 'Diseño de Software' ---")

    # Pedido 1: Café solo
    mi_cafe = CafeSimple()
    print(f"Pedido 1: {mi_cafe.obtener_descripcion()} | Costo: ${mi_cafe.calcular_costo():.2f}")

    # Pedido 2: Café con leche
    cafe_con_leche = ConLeche(mi_cafe)
    print(f"Pedido 2: {cafe_con_leche.obtener_descripcion()} | Costo: ${cafe_con_leche.calcular_costo():.2f}")

    # Pedido 3: Café con leche y azúcar
    cafe_completo = ConAzucar(cafe_con_leche)
    print(f"Pedido 3: {cafe_completo.obtener_descripcion()} | Costo: ${cafe_completo.calcular_costo():.2f}")

    # Pedido 4: Café con doble azúcar (demuestra la flexibilidad)
    cafe_muy_dulce = ConAzucar(cafe_completo)
    print(f"Pedido 4: {cafe_muy_dulce.obtener_descripcion()} | Costo: ${cafe_muy_dulce.calcular_costo():.2f}")
