class Pelicula:
    def __init__(self, titulo, lanzamiento, generos, calificacion, sinopsis, duracion, origen, idioma, director, reparto, calf_edades, user_calificacion):
        self.titulo = titulo
        self.lanzamiento = lanzamiento
        self.generos = generos
        self.calificacion = calificacion
        self.sinopsis = sinopsis
        self.duracion = duracion
        self.origen = origen
        self.idioma = idioma
        self.director = director
        self.reparto = reparto
        self.calf_edades = calf_edades
        self.user_calificacion = user_calificacion

class Grafo:
    def __init__(self):
        self.nodos = []
        self.listas_adyacencia = {}

    def agregar_nodo(self, pelicula):
        self.nodos.append(pelicula)
        self.listas_adyacencia[pelicula] = []

    def agregar_arista(self, pelicula1, pelicula2):
        if pelicula2 not in self.listas_adyacencia[pelicula1]:
            self.listas_adyacencia[pelicula1].append(pelicula2)

        if pelicula1 not in self.listas_adyacencia[pelicula2]:
            self.listas_adyacencia[pelicula2].append(pelicula1)

    def obtener_adyacentes(self, pelicula):
        return self.listas_adyacencia[pelicula]