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
