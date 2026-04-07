# -*- coding: utf-8 -*-
"""
Patrón: Observer (Observador)
Propósito: Definir una dependencia de uno a muchos entre objetos, de forma que cuando un objeto cambie de estado, se notifique y actualicen automáticamente todos los objetos dependientes.
"""

from abc import ABC, abstractmethod
from typing import List


# Interfaz del Observador
class Suscriptor(ABC):
    @abstractmethod
    def actualizar(self, noticia: str) -> None:
        pass


# Observador Concreto: Usuario
class Usuario(Suscriptor):
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def actualizar(self, noticia: str) -> None:
        print(f"📖 {self.nombre} ha recibido una noticia: {noticia}")


# Sujeto (Canal de Noticias)
class CanalDeNoticias:
    def __init__(self) -> None:
        self._suscriptores: List[Suscriptor] = []
        self._ultima_noticia: str = ""

    def suscribir(self, suscriptor: Suscriptor) -> None:
        """Añade un nuevo suscriptor a la lista."""
        self._suscriptores.append(suscriptor)
        print(f"--- Nuevo suscriptor añadido ---")

    def desuscribir(self, suscriptor: Suscriptor) -> None:
        """Elimina un suscriptor de la lista."""
        self._suscriptores.remove(suscriptor)
        print(f"--- Un suscriptor se ha dado de baja ---")

    def notificar(self) -> None:
        """Notifica a todos los suscriptores sobre la nueva noticia."""
        for suscriptor in self._suscriptores:
            suscriptor.actualizar(self._ultima_noticia)

    def publicar_noticia(self, noticia: str) -> None:
        """Publica una noticia y activa la notificación."""
        print(f"\n📢 Publicando noticia: {noticia}")
        self._ultima_noticia = noticia
        self.notificar()


if __name__ == "__main__":
    # Creamos el canal
    tech_news = CanalDeNoticias()

    # Creamos suscriptores
    user1 = Usuario("Ana Python")
    user2 = Usuario("Carlos Dev")
    user3 = Usuario("Maria JS")

    # Realizamos suscripciones
    tech_news.suscribir(user1)
    tech_news.suscribir(user2)

    # Publicamos una noticia
    tech_news.publicar_noticia("¡Python 3.12 ya está disponible!")

    # Alguien más se suscribe
    tech_news.suscribir(user3)

    # Publicamos otra noticia
    tech_news.publicar_noticia("IA generativa revoluciona el desarrollo de software.")

    # Alguien se desuscribe
    tech_news.desuscribir(user1)

    # Última noticia
    tech_news.publicar_noticia("Lanzamiento del nuevo framework 'Antigravity'.")
