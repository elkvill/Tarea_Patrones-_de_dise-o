# 📚 Repositorio Educativo: Patrones de Diseño

Este repositorio contiene una colección de patrones de diseño implementados en **Python 3.10+**, con un enfoque educativo, profesional y práctico.

---

## 🌟 Sección Teórica

### ¿Qué entiendes por patrones de diseño y por qué son el lenguaje universal de los programadores?

Los patrones de diseño son mucho más que simples recetas de código; son el **lenguaje universal** que compartimos los desarrolladores alrededor del mundo. Independientemente del lenguaje utilizado, cuando dices "esto es un *Adapter*" o "aquí usaremos un *State*", tus colegas entienden inmediatamente la arquitectura y la intención del código.

Son el lenguaje universal porque:
1.  **Elevan el nivel de abstracción**: Nos permiten hablar de sistemas complejos en términos simples.
2.  **Facilitan la colaboración**: Reducen el tiempo de explicación técnica.
3.  **Encapsulan sabiduría**: Son la destilación de soluciones probadas por expertos.

Aprender patrones es aprender a comunicarte con otros desarrolladores mediante un diseño elegante y predecible.

---

## 📂 Patrones Implementados

### 01. [Adapter (Adaptador)](./01_Adapter/payment_adapter.py)
*   **Problema**: Integrar un sistema moderno (JSON) con uno antiguo (XML) sin modificar el código legacy.
*   **Solución**: Una clase que traduce la interfaz antigua a la esperada por el cliente moderno.

### 02. [Facade (Fachada)](./02_Facade/home_theater.py)
*   **Problema**: Manejar múltiples subsistemas complejos (luces, sonido, proyector) de forma individual.
*   **Solución**: Una interfaz única y sencilla (`CineEnCasa`) que orquestra todos los subsistemas.

### 03. [Command (Comando)](./03_Command/smart_bulb.py)
*   **Problema**: Acoplamiento fuerte entre quien solicita una acción y quien la ejecuta.
*   **Solución**: Encapsular la petición en un objeto comando independiente.

### 04. [Proxy (Intermediario)](./04_Proxy/secure_document.py)
*   **Problema**: Necesidad de controlar el acceso o añadir seguridad a un objeto sensible.
*   **Solución**: Un intermediario que valida credenciales antes de delegar al objeto real.

### 05. [State (Estado)](./05_State/traffic_light.py)
*   **Problema**: Objetos cuyo comportamiento cambia drásticamente según su estado interno (ej. un semáforo).
*   **Solución**: Delegar el comportamiento a clases de estado específicas que gestionan las transiciones.

---

## 🚀 Cómo ejecutar los ejemplos

Para probar cualquier patrón, utiliza Python desde tu terminal:

```bash
# Ejemplo:
python 01_Adapter/payment_adapter.py
```

---
*Diseño y arquitectura de software para fines educativos.*
