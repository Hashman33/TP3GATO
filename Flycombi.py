import sys
import funiones_grafo
import random
import heapq
import fileinput

def listar_operaciones():
	print("camino_mas\ncamino_escalas\ncentralidad_aprox\nexportar_kml\nitinerario\nnueva_aerolinea\npagerank\n")

def cargar_datos(aeropuertos,vuelos,grafo):
	ciudades = {}
	with open(aeropuertos,r) as aeropuertos:
		for linea in aeropuertos:
			linea=linea.rstrip('\n')
			linea=linea.split(',')
			vertice = vertice(linea[1],linea[2],linea[3],linea[0])
			grafo.agregar_vertice(vertice)
			if linea[0] not in ciudades:
				ciudades[linea[0]] = [linea[1]]
			else:
				ciudades[linea[0]].append(linea[1])

	with open(vuelos,r) as vuelos:
		for linea in vuelos:
			linea=linea.rstrip("\n")
			linea=linea.split(",")
			grafo.agregar_arista(grafo.ver_grafo()[linea[0]],grafo.ver_grafo()[linea[1]],linea[3],linea[2],linea[4])
	return ciudades

def camino_mas(grafo,ciudades,ciudad_partida,ciudad_llegada,opcion): # + 1
	if opcion == "barato":
		n = 0
	if opcion == "rapido":
		n = 1
	camino_m = None
	valor_m = 999999999999999999999999999
	for aeropuerto in ciudades[ciudad_partida]:
		camino,valor = camino_minimo_ciudad(grafo,grafo1[aeropuerto],ciudad_llegada,n)
		if valor < valor_m:
			camino_m = camino
			valor_m = valor

	string = ""
	for i in camino_m:
		string += i + " -> "
	print(string)
	return camino_m

def camino_escalas(grafo,ciudades,ciudad_partida,ciudad_llegada): # + 1 necesito funcion de camino minimo entre a y b que devuelva una lista con la rutas con menos vertices
	camino_m
	dist_m
	for aeropuerto in ciudades[ciudad_partida]:
		camino,dist = menos_escalas(grafo,grafo.ver_grafo()[aeropuerto],ciudad_llegada)
		if dist < dist_m:
			camino_m = camino
			dist_m = dist

	for i in camino_m:
		string += i + " -> "
	print(string)
	return camino_m

def centralidad_aprox(grafo,n): # + 1 algoritmo de centralidad de grafos aproximado
	string = ""
	paths = []
	times = {}
	m_aerop = []
	final = []
	for i in range(1000):
		paths.append(random_walk(grafo,1000))
		for j in paths[-1]:
			if j not in times:
				times[j] = 1
			times[j] += 1

	for k in times:
		heappush(m_aerop,(times[k],k))
	for i in range(n):
		string = string + m_aerop[-1][1] + ","
		final.append(m_aerop[-1][1])
		m_aerop.pop()
	print(string)

	return final

#def recorrer_mundo_aprox(grafo,n):
def nueva_aerolinea(grafo,archivo):
	rutas = prim(grafo)
	archivo = open(archivo, "w")
	for i in rutas:
		archivo.write(i[0] + "," + i[1])
	archivo.close()


def itinerario(grafo,archivo,ciudades,dicc_ciudades):
	path_final = []
	cont = 1;
	cond = []
	with open(archivo, r)as archivo:
		ciudades = archivo.readline()
		ciudades = archivo.rstrip("\n")
		ciudades = archivo.split(",")
		for linea in archivo:
			linea=linea.rstrip("\n")
        	linea=linea.split(",")
        	cond.extend(linea)
    ruta_ciudades = city_path(ciudades,cond)
    
    for x in range(len(ruta_ciudades)):
    	path_f = None 
    	value = 99999999999999999999999999999999
    	for aeropuerto in dicc_ciudades[ruta_ciudades[x]]:
    		path,valor = camino_minimo_ciudad(grafo,grafo.ver_grafo()[aeropuerto],ruta_ciudades[x],0)
    		if valor < value:
    			value = valor:
    			path_f = path:
    	path_final.append(path_f)
    string = ""
    path_exportar = []
    for camino in path_final:
    	for aerop in camino:
    		path_exportar.append(aerop)
    		string += aerop + " -> "
		print(string + "\n") 

	return path_exportar # ojo que devuelve lista de lista

def crear_rutas (grafo, camino):
	rutas = []
	for i in camino:
		rutas.append(i, grafo.ver_grafo()[i].latidud, grafo.ver_grafo()[i].longitud)
	return rutas

def exportar_kml (nombre, rutas):
	file = open(nombre, "w")
	write('<?xml version="1.0" encoding="UTF-8"?>\n')
	write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
	write("\t<Document>\n")
	write("\t\t<name>" + nombre + "</name>\n")

	for i in rutas:
		lineas = ["\t\t<Placemark>", "\t\t\t<name>" + rutas[i][0] + "</name>","\t\t\t<Point>", "\t\t\t<coordinates> " + rutas[i][1] + ", " + rutas[i][2] + "</coordinates>", "\t\t\t</Point>", "\t\t</Placemark>\n"]
		file.writelines(lineas)

	write("\t</Document>\n")
	write("</kml>")

	for i in rutas:
		string += rutas[i][0] + " -> "

	print(string)

	file.close()

def city_path(ciudades,condiciones):

	prioridad=[]

	for i in condiciones:

		if((i[0] not in prioridad ) and (i[1] not in prioridad) ):
			prioridad.extend([i[0],i[1]])
	
	for j in condiciones:
		
		if ((j[0] not in i) and (j[1] in i)):
				prioridad.insert(prioridad.index(j[1]),j[0])
		if ((j[1] not in i) and (j[0] in i)):
				prioridad.insert(prioridad.index(j[0])+ 1,j[1])
	n = len(ciudades)- len(prioridad)
	[prioridad.append(n) for n in ciudades if n not in prioridad]
	return prioridad

def calc_page_rank (grafo):
	d = 0.85
	page_rank = {}

	for v in grafo.ver_grafo():
		page_rank[v] = 1/grafo.n_vertices()

	for i in range (1, 1000):
		page_rank_tmp = {}

		for e in grafo.ver_grafo():
			v = grafo.ver_grafo[e]
			page_rank_tmp[v.codigo()]  += ((1-d)/grafo.n_vertices)

			if v.cant_adyacentes() == 0:
				for w in grafo.ver_grafo():
					page_rank_tmp[v.codigo()] += d*(1.0/grafo.n_vertices)
			else:
				for u in v.adyacentes():
					page_rank_tmp[v.codigo()] += d*(page_rank[u]/u.cant_adyacentes)

		page_rank = page_rank_tmp

	return page_rank

def pagerank(grafo, n):
	page_rank = calc_page_rank(grafo)
	list_pr = []
	list_ap = []
	for key, value in page_rank:
    	temp = [value, key]
    	list_pr.append(temp)
    _heapify_max(list_pr)
    string = ""
    for i in range (0, n):
    	aeropuerto = _heappop_max(list_pr)[1]
    	string += aeropuerto + ", "
    	list_ap.append(aeropuerto)
    print(string)
	
def interfaz():
	grafo = grafo()
	ciudades = cargar_datos(sys.arg[1],sys.arg[2],grafo)

	for line in fileinput.input():
		line = line.rstrip("\n")
		line = line.split(" ")

		if line[0] = "listar_operaciones":
			listar_operaciones()
			continue
			ruta = None
		if line[0] =  "camino_mas":
			if len(line) != 4:
				continue
			ruta = camino_mas(grafo,ciudades,line[2],line[3],line[1])
		if line[0] = "camino_escalas":
			if len(line) != 3:
				continue
			ruta = camino_mas(grafo,ciudades,line[1],line[2])
		if line[0] = "centralidad_aprox":
			if len(line) != 2:
				continue
			ruta = centralidad_aprox(grafo,line[1])
		if line[0] = "nueva_aerolinea":
			if len(line)!= 2:
				continue
			ruta = nueva_aerolinea(grafo,line[1])
		if line[0] = "itinerario":
			if len(line) != 2:
				continue
			ruta = itinerario(grafo,line[1])
		if line[0] = "pagerank":
			if len(line) != 1:
				continue
			ruta = pagerank(grafo)
		if line[0] = "exportar_kml"
			if len(line) !=2 and not ruta:
				continue
			rutas = crear_rutas(grafo,ruta)
			exportar_kml(line[1],rutas);


		# algo parecio a lo que se hiso en el tp2
		
def main()
	interfaz()

main()

