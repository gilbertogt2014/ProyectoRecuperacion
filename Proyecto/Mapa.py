class Mapa ():
	def __init__ (self, ancho, alto):
		self.alto = alto
		self.ancho = ancho
		self.monedas = []
		self.robot = None


	def asignar_robot (self, robot):
		self.robot = robot
	
	def poner_moneda (self, moneda):
		self.monedas.append(moneda)

	def dibujar (self):
		resultado = ""
		for y in range(self.alto):
			for x in range(self.ancho):
				if x == self.robot.x and y == self.robot.y:
					resultado += self.robot.dibujar()
				elif self.contar_monedas(x, y) > 0:
					resultado += str(self.contar_monedas(x, y)) 
				else:
					resultado += " "

			resultado += "\n"
		return resultado

	def contar_monedas (self, x, y):
		conteo = 0 
		for moneda in self.monedas:
			if moneda.y == y and moneda.x == x:
				conteo += 1
				
		return conteo 

	def quitar_moneda (self, x, y):

		coincidencia = -1
		for indice in range(len(self.monedas)):
			moneda = self.monedas[indice]
			if moneda.x == x and moneda.y == y:
				coincidencia = indice
				

			if coincidencia >= 0:
				self.monedas.pop (coincidencia)
				coincidencia = indice
				break

			if indice >= 0:
				self.monedas.pop(indice)