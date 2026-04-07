# -*- coding: utf-8 -*-
"""
Patrón: Singleton
Propósito: Garantizar que una clase tenga una única instancia y proporcionar un punto de acceso global a ella.
"""

from typing import Optional


class ConfiguracionBaseDatos:
    _instancia: Optional["ConfiguracionBaseDatos"] = None

    def __new__(cls) -> "ConfiguracionBaseDatos":
        # Si la instancia no existe, la creamos
        if cls._instancia is None:
            print("--- Creando nueva instancia de configuración ---")
            cls._instancia = super(ConfiguracionBaseDatos, cls).__new__(cls)
            # Inicializamos los atributos por defecto
            cls._instancia.host = "localhost"
            cls._instancia.puerto = 5432
            cls._instancia.usuario = "admin"
        return cls._instancia

    def mostrar_configuracion(self) -> None:
        """Muestra los datos actuales de la configuración."""
        print(f"Host: {self.host}, Puerto: {self.puerto}, Usuario: {self.usuario}")


if __name__ == "__main__":
    # Primer acceso a la configuración
    config1 = ConfiguracionBaseDatos()
    config1.mostrar_configuracion()

    # Segundo acceso a la configuración
    config2 = ConfiguracionBaseDatos()
    
    # Modificamos un valor en la segunda referencia
    config2.host = "192.168.1.100"

    # Verificamos si config1 y config2 son la misma instancia
    print(f"\n¿Son la misma instancia? {'Sí' if config1 is config2 else 'No'}")
    
    # Comprobamos que config1 ahora refleja el cambio hecho en config2
    print("Configuración en config1:")
    config1.mostrar_configuracion()
