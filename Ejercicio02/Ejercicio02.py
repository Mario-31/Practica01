from abc import ABC, abstractmethod
from typing import List
from random import randint

"""
En general está muy bien.
No hay muchos errores PEP8
Respecto a la clase playlist hay que reestructurarla un poquito.
Y para ordenar aunque evidentemente funcionan los lambdas, se tenía que
ver cómo manipulaban el código del ordenamiento para poder ordenar bajo esas
condiciones.

5.5
"""

# Clase para manejar fechas en formato "dd/mm/aaaa"
"""
Excelente, sólo recuerden que estamos definiendo clases abstractas también.
"""
class Fecha:
    def __init__(self, fecha: str):
        # Dividir la fecha en día, mes y año
        self.dia, self.mes, self.ano = map(int, fecha.split("/"))

    # Método para comparar fechas
    def __lt__(self, other):
        if self.ano != other.ano:
            return self.ano < other.ano
        if self.mes != other.mes:
            return self.mes < other.mes
        return self.dia < other.dia


"""
Muy bien!
"""
# Clase para representar una canción
class Cancion:
    # Hay más de 79 caracteres por línea
    def __init__(self, nombre_cancion: str, duracion: str, artista: str, release_date: str):
        self.nombre_cancion = nombre_cancion
        self.duracion = duracion
        self.artista = artista
        self.release_date = Fecha(release_date)

    # Método para imprimir la canción
    def __str__(self):
        return f"{self.nombre_cancion} - {self.duracion}"


# Clase abstracta para estrategias de ordenamiento
class Ordenamiento(ABC):
    @abstractmethod
    def ordenar(self, canciones: List[Cancion]) -> List[Cancion]:
        pass

    def merge_sort(self, arr: List[Cancion], compare_func) -> List[Cancion]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = self.merge_sort(left, compare_func)
        right = self.merge_sort(right, compare_func)
        return self.merge(left, right, compare_func)

    def merge(self, left: List[Cancion], right: List[Cancion], compare_func) -> List[Cancion]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if compare_func(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


"""
Bueno lo ideal era buscar la forma de modificar directamente el código
(en este caso merge) para poder ordenar de acuerdo a la condición.
"""
# Estrategia de ordenamiento por nombre de canción
class OrdenarPorNombre(Ordenamiento):
    def ordenar(self, canciones: List[Cancion]) -> List[Cancion]:
        return self.merge_sort(canciones, lambda x, y: x.nombre_cancion < y.nombre_cancion)


# Estrategia de ordenamiento por artista y nombre de canción
class OrdenarPorArtista(Ordenamiento):
    def ordenar(self, canciones: List[Cancion]) -> List[Cancion]:
        return self.merge_sort(canciones, lambda x, y: (x.artista, x.nombre_cancion) < (y.artista, y.nombre_cancion))   


# Estrategia de ordenamiento por fecha de lanzamiento y nombre de canción
class OrdenarPorFecha(Ordenamiento):
    def ordenar(self, canciones: List[Cancion]) -> List[Cancion]:
        return self.merge_sort(canciones, lambda x, y: (x.release_date, x.nombre_cancion) < (y.release_date, y.nombre_cancion))


# Clase para representar una playlist de canciones
"""
La clase está casi bien, no queremos crear diferentes objetos Playlist para
cada ordenamiento, realmente queremos poder ordenar con el mismo playlist.
Entonces deberia poder crearse sin tener que pasar como parámetro qué
ordenamiento queremos.
"""
class Playlist:
    def __init__(self, ordenamiento: Ordenamiento):
        self.canciones = []
        self.ordenamiento = ordenamiento

    # Método para agregar una canción a la playlist
    def agregar_cancion(self, cancion: Cancion):
        self.canciones.append(cancion)

    # Método para ordenar las canciones en la playlist
    def ordenar_canciones(self):
        self.canciones = self.ordenamiento.ordenar(self.canciones)

    # Método para imprimir la playlist
    def __str__(self):
        """
        Quizá queda mejor si le damos formato, al menos el numeral.
        """
        self.ordenar_canciones()
        return "\n".join(str(cancion) for cancion in self.canciones)

# Punto de entrada del programa
if __name__ == "__main__":
    # Crear una playlist y establecer la estrategia de ordenamiento inicial como OrdenarPorNombre
    playlist = Playlist(OrdenarPorNombre())

    # Generar 43 canciones de ejemplo y agregarlas a la playlist
    for i in range(1, 44):
        nombre_cancion = f"Cancion {i}"
        duracion = f"{randint(2, 5)}:{randint(0, 59):02d}"
        artista = f"Artista {randint(1, 10)}"
        fecha = f"{randint(1, 31):02d}/{randint(1, 12):02d}/{randint(2000, 2022)}"
        playlist.agregar_cancion(Cancion(nombre_cancion, duracion, artista, fecha))

    # Imprimir la playlist ordenada por diferentes criterios
    print("Playlist ordenado por nombre:")
    print(playlist)
    playlist.ordenamiento = OrdenarPorArtista()
    print("\nPlaylist ordenado por artista:")
    print(playlist)
    playlist.ordenamiento = OrdenarPorFecha()
    print("\nPlaylist ordenado por fecha:")
    print(playlist)
