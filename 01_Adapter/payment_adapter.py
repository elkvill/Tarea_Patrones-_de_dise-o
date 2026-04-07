# -*- coding: utf-8 -*-
"""
Patrón: Adapter (Adaptador)
Propósito: Permitir que clases con interfaces incompatibles trabajen juntas traduciendo la interfaz de una clase a otra que el cliente espera.
"""

from typing import Dict


# Interfaz Moderna (Lo que el sistema espera)
class ProcesadorPagoModerno:
    def procesar_pago_json(self, datos: Dict[str, str]) -> None:
        """El sistema moderno solo entiende diccionarios (JSON)."""
        print(f"--- Procesando pago moderno ---")
        print(f"ID: {datos['id']}, Monto: ${datos['total']}")


# Clase Antigua (Legacy - Incompatible)
class SistemaPagoAntiguo:
    def realizar_pago_xml(self, xml_string: str) -> None:
        """El sistema antiguo solo entiende strings con formato XML."""
        print(f"--- Sistema Antiguo (Recibiendo XML) ---")
        print(f"XML Recibido: {xml_string}")


# Adaptador
class AdaptadorPago(ProcesadorPagoModerno):
    def __init__(self, sistema_antiguo: SistemaPagoAntiguo) -> None:
        self.sistema_antiguo = sistema_antiguo

    def procesar_pago_json(self, datos: Dict[str, str]) -> None:
        # 1. Convertimos los datos JSON a XML (lo que el sistema antiguo espera)
        xml_convertido = f"<pago><id>{datos['id']}</id><monto>{datos['total']}</monto></pago>"
        
        # 2. Delegamos la ejecución al sistema antiguo pero usando el formato correcto
        print("[Adaptador] Convirtiendo JSON a XML para compatibilidad...")
        self.sistema_antiguo.realizar_pago_xml(xml_convertido)


if __name__ == "__main__":
    # Datos en formato moderno
    pago_usuario = {"id": "12345", "total": "150.00"}

    # Intentamos usar el sistema antiguo directamente (FALLARÍA en un entorno real)
    # sistema_antiguo = SistemaPagoAntiguo()
    # sistema_antiguo.realizar_pago_xml(pago_usuario) # Error: espera XML string, no dict

    # Usamos el Adaptador para que el sistema moderno pueda hablar con el antiguo
    print("--- Probando el Adaptador de Pagos ---")
    legacy_api = SistemaPagoAntiguo()
    adaptador = AdaptadorPago(legacy_api)

    # El cliente usa el método moderno, pero por detrás se usa el sistema antiguo
    adaptador.procesar_pago_json(pago_usuario)
