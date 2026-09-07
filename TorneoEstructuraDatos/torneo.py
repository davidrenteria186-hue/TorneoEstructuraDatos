class Participante:
    def __init__(self, nombre: str, habilidad: int):
        # Encapsulamiento: atributos privados
        if not nombre or habilidad < 0:
            raise ValueError("Datos de participante inválidos.")
        self.__nombre = nombre
        self.__habilidad = habilidad

    def get_nombre(self) -> str:
        return self.__nombre

    def get_habilidad(self) -> int:
        return self.__habilidad


class Torneo:
    def __init__(self, participantes: list[Participante]):
        # Validación de entrada vacía
        if not participantes:
            raise ValueError("El torneo debe tener al menos un participante.")
        self.__participantes = participantes

    def __jugar_duelo(self, p1: Participante, p2: Participante) -> Participante:
        """Compara la habilidad de dos participantes y retorna el ganador."""
        if p1.get_habilidad() >= p2.get_habilidad():
            return p1
        return p2

    def resolver_campeon(self, inicio: int = 0, fin: int = None) -> Participante:
        """Encuentra al campeón utilizando la técnica Divide y Vencerás (Recursivo)."""
        if fin is None:
            fin = len(self.__participantes) - 1

        # Caso base de validación
        if inicio > fin:
            raise IndexError("Rango de búsqueda inválido.")

        # CASO BASE: Solo queda 1 participante en este tramo de la llave
        if inicio == fin:
            return self.__participantes[inicio]

        # DIVIDE: Punto medio del arreglo
        medio = (inicio + fin) // 2

        # VENCE: Resolver recursivamente la mitad izquierda y derecha
        campeon_izquierda = self.resolver_campeon(inicio, medio)
        campeon_derecha = self.resolver_campeon(medio + 1, fin)

        # COMBINA: Enfréntalos en un duelo final de esa ronda
        return self.__jugar_duelo(campeon_izquierda, campeon_derecha)


# --- PRUEBA DEL CÓDIGO ---
if __name__ == "__main__":
    # Lista de competidores para probar
    competidores = [
        Participante("Ana", 80),
        Participante("Carlos", 95),
        Participante("Beatriz", 70),
        Participante("David", 90)
    ]

    # Crear torneo y resolver
    torneo_actual = Torneo(competidores)
    ganador = torneo_actual.resolver_campeon()

    print("--------------------------------------------------")
    print(f"¡El campeón del torneo es: {ganador.get_nombre()}!")
    print(f"Nivel de habilidad: {ganador.get_habilidad()}")
    print("--------------------------------------------------")