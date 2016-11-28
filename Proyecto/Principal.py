
def cargar_mapa (nombre):
	mapa = open(nombre, "r")
	lista_mapa = [ ]

	for i in mapa:
		lista_mapa.append(list(i.strip()))
	mapa.close()
	return lista_mapa

def cargar_instrucciones (inst):
	ins = open(inst, "r")
	lista_instrucciones = []

	for i in ins:
		lista_instrucciones.append(i.strip())
	ins.close()
	return lista_instrucciones