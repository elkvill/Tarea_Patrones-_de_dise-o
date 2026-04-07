# 📚 Patrones de Diseño - Volumen 2

Este segundo volumen profundiza en patrones **Estructurales** y de **Comportamiento**, manteniendo el enfoque educativo y profesional con Python 3.10+.

---

## 🌟 Sección Teórica

### ¿Qué entiendes por patrones de diseño y por qué son el lenguaje universal de los programadores?

Los patrones de diseño son mucho más que simples recetas de código; son el **lenguaje universal** que compartimos los desarrolladores alrededor del mundo. Independientemente de si programas en Python, Java, C++ o Swift, cuando dices "esto es un *Adapter*" o "aquí usaremos un *State*", tus colegas entienden inmediatamente la arquitectura y la intención de tu código sin necesidad de ver una sola línea.

Son el lenguaje universal porque:
1.  **Elevan el nivel de abstracción**: Nos permiten hablar de sistemas complejos en términos simples y conocidos.
2.  **Facilitan la colaboración**: Reducen drásticamente el tiempo de explicación en reuniones técnicas.
3.  **Encapsulan sabiduría**: Son la destilación de décadas de resolución de problemas por parte de los mejores ingenieros de la historia.

Aprender patrones es, en esencia, aprender a comunicarte con otros desarrolladores a través del tiempo y el espacio mediante un diseño elegante y predecible.

---

## 📂 Proyectos del Volumen 2

### 01. Adapter (Adaptador)
*   **Problema del mundo real**: Tenemos un sistema de pagos moderno que solo acepta JSON, pero necesitamos integrarnos con un banco antiguo que solo responde a XML. No podemos cambiar el banco ni queremos ensuciar el código moderno.
*   **Estructura en Python**: La clase `AdaptadorPago` hereda de la interfaz moderna pero envuelve internamente al sistema antiguo, realizando la traducción de datos "al vuelo".

### 02. Facade (Fachada)
*   **Problema del mundo real**: Manejar un Cine en Casa implica lidiar con luces, sonido y proyector por separado, lo cual es tedioso y propenso a errores.
*   **Estructura en Python**: La clase `CineEnCasa` ofrece los métodos `comenzar_pelicula()` y `terminar_pelicula()`, ocultando la complejidad de los subsistemas individuales tras una interfaz sencilla.

### 03. Command (Comando)
*   **Problema del mundo real**: Queremos que un botón de un control remoto no sepa qué está encendiendo, solo que debe ejecutar una acción. Esto permite cambiar qué hace el botón sin modificar el control remoto.
*   **Estructura en Python**: Encapsulamos las acciones de la clase `BombillaInteligente` en objetos `Comando`. El `ControlRemoto` solo recibe y ejecuta estos objetos.

### 04. Proxy (Intermediario)
*   **Problema del mundo real**: Queremos proteger el acceso a un documento confidencial. No cualquiera debe poder llamar al método `leer()`.
*   **Estructura en Python**: La clase `ProxyDocumento` actúa como una barrera. Implementa la misma interfaz que el documento real pero añade una validación de contraseña antes de permitir el acceso.

### 05. State (Estado)
*   **Problema del mundo real**: Un semáforo se comporta de forma distinta según su color actual. Manejar esto con muchos `if` suele ser un caos difícil de mantener.
*   **Estructura en Python**: Cada color del semáforo es una clase separada (`EstadoRojo`, `EstadoVerde`). El `Semaforo` simplemente delega su comportamiento al objeto de estado que tenga asignado en ese momento.

---
*Continuando el viaje hacia la excelencia técnica.*
