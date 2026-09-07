# Actividad Unidad 1 - Torneo por Eliminación Directa

**Asignatura:** Estructura de Datos  
**Institución:** Fundación Universitaria María Cano  

## Descripción del Proyecto
Solución al Problema 1: Determinar el campeón de un torneo por eliminación directa implementando el paradigma de Programación Orientada a Objetos (POO) y la estrategia de **Divide y Vencerás** (Recursividad).

## Estructura de Clases (UML)
![Diagrama UML](diagrama_uml.png)

## Estructura del Código
- `Participante`: Clase que modela cada competidor con atributos encapsulados (`nombre`, `habilidad`).
- `Torneo`: Clase encargada de coordinar los enfrentamientos de forma recursiva calculando el punto medio de la lista.

- ## Justificación de Decisiones Técnicas

* **¿Por qué Divide y Vencerás?**: El torneo por eliminación directa sigue la estructura de un árbol binario. La recursividad divide los competidores a la mitad en cada llamada (`medio`), evitando el uso de arreglos auxiliares complejos que requeriría un bucle iterativo.
* **¿Por qué POO y Encapsulamiento?**: Se separaron las responsabilidades en dos clases (`Participante` y `Torneo`). El uso de atributos privados (`__`) protege la integridad de los datos (como la habilidad) para que no sean alterados externamente durante el torneo.
* **¿Por qué Potencia de 2?**: Garantiza un árbol de decisión perfecto donde todos los participantes tienen pareja en cada ronda sin dejar elementos impares aislados.

## Respuestas a la Presentación (Sustentación Técnica)

* **¿Por qué esas clases y no una sola?**  
  Por el principio de **Responsabilidad Única**. `Participante` maneja la entidad y sus datos, mientras que `Torneo` coordina la lógica de los enfrentamientos. Mezclarlas crearía acoplamiento e iría en contra de la POO.

* **¿Qué regla protege el atributo privado y qué pasaría si fuera público?**  
  Aplica la regla de **Encapsulamiento y Protección de Integridad**. Si los atributos como `habilidad` fueran públicos, cualquier método externo podría alterarlos arbitrariamente a mitad de la competencia.

* **¿Por qué la operación vive en esa clase?**  
  La función `resolver_campeon` vive en `Torneo` porque requiere una visión global de la lista de participantes para realizar la división por mitades. `Participante` solo encapsula el estado individual.

* **¿Cuál es el caso base y por qué garantiza que la recursión termina?**  
  El caso base ocurre cuando `inicio == fin` (queda un solo participante en el subgrupo). Garantiza el fin del ciclo porque el problema se divide iterativamente a la mitad (`medio`), reduciendo el tamaño del arreglo hasta llegar a 1.

* **¿Cómo partes por mitades y qué haces cuando la mitad no es pareja?**  
  Se calcula la mitad exacta mediante `medio = (inicio + fin) // 2`. Para evitar que la mitad no sea pareja y queden participantes desparejados en un árbol binario de eliminación directa, se valida mediante una restricción de entrada que el total sea **potencia de 2** ($2, 4, 8, 16...$).

* **¿Qué decidiste con la entrada inválida y por qué?**  
  Se implementó **manejo defensivo de excepciones (`ValueError`)**. Si se ingresan listas vacías, habilidades negativas, nombres no válidos o una cantidad de participantes que no sea potencia de 2, el programa interrumpe la ejecución antes de generar errores en tiempo de ejecución.

* **¿Qué te falló durante el desarrollo?**  
  El principal reto fue calibrar los índices de partición (`inicio`, `medio`, `fin`) en las llamadas recursivas para evitar bucles infinitos (*RecursionError*) o desbordamiento de índices.

* **¿Qué herramientas usaste?**  
  **VS Code** para codificación, **Draw.io** para el diagrama UML de clases y **GitHub** para control de versiones y repositorio.

* **¿Qué cambiarías si lo hicieras de nuevo?**  
  Implementaría un sistema de *bye* (pase directo) para permitir cantidades impares de participantes sin restringir a potencia de 2, junto a una interfaz gráfica dinámica.
