# Repositorio Educativo: Patrones de Diseño en Python

¡Bienvenido! Este repositorio está diseñado para enseñar de manera práctica y sencilla 5 de los patrones de diseño más utilizados en la industria del software, aplicados con **Python 3.10+** y Programación Orientada a Objetos (POO).

---

## Sección Teórica

### ¿Qué entiendes por patrones de diseño en el desarrollo de software?

En el desarrollo de software, los **Patrones de Diseño** son soluciones estandarizadas y probadas para problemas comunes que surgen durante la creación de sistemas robustos. No son piezas de código terminadas que puedes copiar y pegar, sino más bien **plantillas o guías conceptuales** sobre cómo estructurar tus clases y objetos para resolver un desafío específico.

Imagina que estás construyendo una casa: no inventas cómo poner los cimientos o cómo instalar las tuberías cada vez; usas planos que ya se sabe que funcionan. En el software, los patrones nos ayudan a:
1. **Evitar la "reinvención de la rueda"**: Aprovechamos la experiencia de ingenieros que ya enfrentaron y resolvieron estos problemas.
2. **Mejorar la mantenibilidad**: El código se vuelve más organizado y fácil de entender para otros desarrolladores.
3. **Escalabilidad**: Facilitan añadir nuevas funcionalidades sin romper lo que ya existe.

Se dividen principalmente en tres categorías:
- **Creacionales**: Cómo se crean los objetos.
- **Estructurales**: Cómo se ensamblan objetos y clases en estructuras más grandes.
- **De Comportamiento**: Cómo se comunican y reparten responsabilidades los objetos.

---

## Proyectos Implementados

### 01. Singleton (Único)
*   **Problema que resuelve**: A veces necesitamos que una clase tenga **exactamente una instancia** en todo el programa (por ejemplo, una conexión a base de datos o un registro de logs) para evitar conflictos o consumo excesivo de recursos.
*   **Implementación**: En `database_config.py`, usamos el método `__new__` para controlar la creación del objeto. Si ya existe una instancia guardada en una variable de clase, devolvemos esa en lugar de crear una nueva.

### 02. Factory Method (Método Fábrica)
*   **Problema que resuelve**: Cuando un sistema debe crear diferentes tipos de objetos (como notificaciones), pero no queremos que el código principal dependa de las clases concretas (Email, SMS).
*   **Implementación**: En `notifications.py`, definimos una clase abstracta `Notificacion` y una fábrica `FabricaNotificaciones`. El cliente solo le pide a la fábrica un "tipo" de notificación, y esta se encarga de instanciar la clase correcta.

### 03. Observer (Observador)
*   **Problema que resuelve**: Necesitamos que varios objetos (suscriptores) se enteren automáticamente cuando otro objeto (el canal) cambia su estado o publica contenido.
*   **Implementación**: En `newsletter.py`, el `CanalDeNoticias` mantiene una lista de objetos `Suscriptor`. Cuando se publica una noticia, el canal recorre su lista y llama al método `actualizar()` de cada suscriptor.

### 04. Strategy (Estrategia)
*   **Problema que resuelve**: Queremos cambiar el comportamiento de un objeto en tiempo de ejecución. Por ejemplo, aplicar diferentes tipos de descuentos según la temporada sin llenar el código de `if-else` infinitos.
*   **Implementación**: En `discounts.py`, creamos diferentes clases de estrategia (`DescuentoVerano`, `DescuentoNavidad`). El objeto `CarritoCompras` recibe una estrategia y la usa para calcular el total, permitiendo cambiarla en cualquier momento.

### 05. Decorator (Decorador)
*   **Problema que resuelve**: Queremos añadir funcionalidades o "capas" extras a un objeto de forma dinámica sin usar una herencia excesiva y rígida.
*   **Implementación**: En `coffee_shop.py`, tenemos un `CafeSimple`. Creamos decoradores como `ConLeche` y `ConAzucar` que envuelven al objeto original. Cada decorador añade su propio costo y descripción al objeto que tiene dentro.

---

## Cómo ejecutar los ejemplos

Cada carpeta contiene un script independiente. Para probarlos, simplemente abre una terminal y ejecuta:

```bash
# Ejemplo para Singleton
python 01_Singleton/database_config.py

# Ejemplo para Factory Method
python 02_Factory_Method/notifications.py

# Y así con el resto...
```

---
*Desarrollado con para fines educativos.*
