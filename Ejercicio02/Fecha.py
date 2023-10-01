from abc import ABC, abstractmethod
from typing import List
from random import randint

# Clase para manejar fechas en formato "dd/mm/aaaa"
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


# Clase para representar una canción
class Cancion:
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


# Estrategia de ordenamiento por nombre de canción
class OrdenarPorNombre(Ordenamiento):
    def ordenar(self, canciones: List[Cancion]) -> List[Cancion]:
        return sorted(canciones, key=lambda x: x.nombre_cancion)


# Estrategia de ordenamiento por artista y nombre de canción
class OrdenarPorArtista(Ordenamiento):
    def ordenar(self, canciones: List[Cancion]) -> List[Cancion]:
        return sorted(canciones, key=lambda x: (x.artista, x.nombre_cancion))


# Estrategia de ordenamiento por fecha de lanzamiento y nombre de canción
class OrdenarPorFecha(Ordenamiento):
    def ordenar(self, canciones: List[Cancion]) -> List[Cancion]:
        return sorted(canciones, key=lambda x: (x.release_date, x.nombre_cancion))


# Clase para representar una playlist de canciones
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
