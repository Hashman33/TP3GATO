import random

class vertice:

	def __init__(self,codigo,latitud,longitud,ciudad):
		self.adyacentes = {}
		self.codigo = codigo
		self.latitud = latitud
		self.longitud = longitud
		self.ciudad = ciudad
		self.adyacentes_c = 0
	def agregar_adyacente(self,destino,peso,tiempo,cant_vuelos):
		self.adyacentes[destino.codigo] = (peso,tiempo,cant_vuelos)
		self.adyacentes_c += 1
	def adyacentes(self):
		return self.adyacentes
	
	def codigo(self):
		return self.codigo

	def latitud(self):
		return self.latitud

	def longitud(self):
		return self.longitud
	
	def ciudad(self):
		return self.ciudad
	def cantidad_adyacentes(self):
		return self.adyacentes_c


class grafo:

	def __init__(self):
		self.grafo = {}
		self.n_vertices = 0
		self.aristas = 0

	def agregar_vertice(self,vertice):
		self.grafo[vertice.codigo] = vertice
		self.vertices += 1 

	def cantitdad_vertices(self):
		return self.n_vertices

	def cantidad_aristas(self):
		return self.aristas

	def ver_grafo(self):
		return self.grafo

	def agregar_arista(self,partida,destino,costo,tiempo,cant_vuelos):
		partida.agregar_adyacente(destino,costo,tiempo,cant_vuelos)
		self.aristas  += 1

	def cant_vertices(self):
		return self.vertices

	def obtener_vertice(self):
		return self.grafo[random.choice(list(self.grafo.keys()))]

