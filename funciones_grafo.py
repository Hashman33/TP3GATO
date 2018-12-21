import TDA_grafo
import heapq

def recorrido_dfs (grafo, a, b, visitados):
	grafo = grafo.ver_grafo()
	visitados.append[a]
		for v in grafo[a].adyacentes:
			if v.codigo == b : 
			    return camino
			if v.codigo not in visitados:
				recorrido_dfs (grafo, v, b, visitados)

def prim (grafo,a):
	dicc_g = grafo.ver_grafo()
	visitados[]
	path[]
	queue[]
	visitados.append(a)
	for i in a.adyacentes():
			if i not in visitados:
				heappush(queue,(a.adyacentes()[i][0],a,i))
	while queue:
		v = heappop(queue)
		if v[2] in visitados:
			continue
		visitados.append(v[2])
		path.append((v[1],v[2]))
		nodo_act = dicc_g[v[2]]
		for i in nodo_act.adyacentes():
			if i in visitados:		
				continue
			heappush(queue,(nodo_act.adyacentes()[i][0],nodo_act,i))
	return path



def camino_minimo(grafo,a,b,n): # n variara dependiendo si quiero tomar como peso, precio'0' tiempo '1'.
	
	camino[]
	visitados[]
	caminos_cortos = {a:(None,0)}
	vert_act = a
	grafo1 = grafo.ver_grafo()

	while vert_act != b:
		visitados.append(nodo_act)
		adyacentes = grafo1[vert_act].adyacentes()
		peso_a_vert_act = caminos_cortos[vert_act][1]

		for vert_prox in adyacentes:
			peso = grafo1[vert_act].adyacentes()[vert_prox][n] + peso_a_vert_act

			if vert_prox not in caminos_cortos:
				caminos_cortos[vert_prox] = (vert_act,peso)
			else:
				minimo_peso_act = caminos_cortos[vert_prox][1]

				if minimo_peso_act > peso:
					caminos_cortos[vert_prox] = [vert_act, peso]

		prox_ady = {vert:caminos_cortos[vert] for vert in caminos_cortos if vert not in visitados}

		if not prox_ady:

			return False

		vert_act = min(prox_ady, key=lambda k: prox_ady[k][1])
	
	while vert_act is not None:
		camino.append(vert_act)
		
		vert_prox = caminos_cortos(vert_act)[0]
		vert_act = vert_prox

	camino = camino[::-1]

	return camino

def camino_minimo_ciudad(grafo,a,ciudad,n): # n variara dependiendo si quiero tomar como peso, precio'0' tiempo '1'.
	
	camino[]
	visitados[]
	caminos_cortos = {a:(None,0)}
	vert_act = a
	grafo1 = grafo.ver_grafo()

	while vert_act.ciudad != ciudad:
		visitados.append(vert_act)
		adyacentes = grafo1[vert_act].adyacentes()
		peso_a_vert_act = caminos_cortos[vert_act][1]

		for vert_prox in adyacentes:
			peso = grafo1[vert_act].adyacentes()[vert_prox][n] + peso_a_vert_act

			if vert_prox not in caminos_cortos:
				caminos_cortos[vert_prox] = (vert_act,peso)
			else:
				minimo_peso_act = caminos_cortos[vert_prox][1]

				if minimo_peso_act > peso:
					caminos_cortos[vert_prox] = [vert_act, peso]

		prox_ady = {vert:caminos_cortos[vert] for vert in caminos_cortos if vert not in visitados}

		if not prox_ady:

			return False

		vert_act = min(prox_ady, key=lambda k: prox_ady[k][1])

	valor = caminos_cortos(vert_act)[1]

	while vert_act is not None:
		camino.append(vert_act)
		
		vert_prox = caminos_cortos(vert_act)[0]
		vert_act = vert_prox

	camino = camino[::-1]

	return camino,valor

def random_walk(grafo,n):
	visitados[]
	path[]
	dicc = grafo.ver_grafo()
	v = grafo.obtener_vertice()
	cont = 0
	prox[]
	while( cont < n):
		visitados.append(v.codigo)
		path.append(v.codigo)
		for i in v.adyacentes():
		 	if i not in visitados:
		 		prox.append[dicc[i]]
		v = random.choice(prox)
		if not v:
			return path
		cont += 1
		del prox[:]
	return path


def min_vertices_bfs (grafo, u, v):
	visitados = {}
	distancias = {}
	grafo1 = grafo.ver_grafo()
	q[]
	distancias[u] = 0
	visitados[u] = true
	q.append(u) 

	while q:
		x = q.pop(0)

		for y in grafo1[x].adyacentes():
			if y in visitados:
				continue
			distancias[y] = distancias[x]+1
			q.append(y)
			visitados[y] = true
			if grafo1[y].ciudad() == v:
				break

	return distancias[v]


def minimos_nodos(grafo,n,cont,nodo_act,destino,path):
    if nodo_act.ciudad() == destino:
        path.append(nodo_act.codigo())
        return True
    if cont > n:
        return False
    for i in nodo_act.adyacentes():
        if minimos_nodos(grafo,n,cont+1,grafo.ver_grafo()[i],destino,path):
            path.append(nodo_act.codigo())
            return True
    return False


def menos_escalas(grafo, u, v):
	distancia = min_vertices_bfs(grafo, u, v)
	cont = 0
	path = []
	minimos_nodos(grafo, distancia, cont, u, v, path)
	return path,distancia
