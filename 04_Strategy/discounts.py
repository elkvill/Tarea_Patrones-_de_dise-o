# -*- coding: utf-8 -*-
"""
Patrón: Strategy (Estrategia)
Propósito: Definir una familia de algoritmos, encapsular cada uno de ellos y hacerlos intercambiables. Permite que el algoritmo varíe independientemente de los clientes que lo utilizan.
"""

from abc import ABC, abstractmethod


# Interfaz de la Estrategia
class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular(self, monto: float) -> float:
        pass


# Estrategia Concreta: Sin Descuento
class SinDescuento(EstrategiaDescuento):
    def calcular(self, monto: float) -> float:
        return monto


# Estrategia Concreta: Descuento de Verano (10%)
class DescuentoVerano(EstrategiaDescuento):
    def calcular(self, monto: float) -> float:
        print("☀️ Aplicando descuento de verano (10%)...")
        return monto * 0.90


# Estrategia Concreta: Descuento de Navidad (20%)
class DescuentoNavidad(EstrategiaDescuento):
    def calcular(self, monto: float) -> float:
        print("🎄 Aplicando descuento de navidad (20%)...")
        return monto * 0.80


# Contexto: El Carrito de Compras
class CarritoCompras:
    def __init__(self, monto_base: float) -> None:
        self.monto_base = monto_base
        # Por defecto, no hay descuento
        self._estrategia: EstrategiaDescuento = SinDescuento()

    def establecer_estrategia(self, estrategia: EstrategiaDescuento) -> None:
        """Permite cambiar el algoritmo de descuento en tiempo de ejecución."""
        self._estrategia = estrategia

    def obtener_total(self) -> float:
        """Calcula el total usando la estrategia configurada."""
        return self._estrategia.calcular(self.monto_base)


if __name__ == "__main__":
    monto_compra = 1000.0
    carrito = CarritoCompras(monto_compra)

    print(f"Monto base de la compra: ${monto_compra}")

    # Pago normal
    print(f"Total sin descuento: ${carrito.obtener_total()}")

    # Llega el verano
    print("\n--- Cambio de temporada a Verano ---")
    carrito.establecer_estrategia(DescuentoVerano())
    print(f"Total a pagar: ${carrito.obtener_total()}")

    # Llega Navidad
    print("\n--- Cambio de temporada a Navidad ---")
    carrito.establecer_estrategia(DescuentoNavidad())
    print(f"Total a pagar: ${carrito.obtener_total()}")
