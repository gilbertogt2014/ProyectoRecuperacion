class Robot(object):
	def __init__ (self, x, y):
		self.x = x
		self.y = y
		self.monedas = 0
		self.direccion = 0
		self.mapa = None 

	def colocar_en_mapa (self, mapa):
		self.mapa = mapa

	def  rotar (self):
		if self.direccion == 0:
			self.direccion = 1
		elif self.direccion == 1:
			self.direccion = 2
		elif self.direccion == 2:
			self.direccion = 3
		else:
			self.direccion = 0
			
	def dibujar (self):
		if self.direccion == 0:
			return 'A'
		elif self.direccion == 1:
			return '>'
		elif self.direccion == 2:
			return 'v'
		else:
			return '<'

	def recoger (self):
		if self.mapa.contar_monedas(self.x, self.y) > 0:
			self.monedas += 1
			self.mapa.quitar_moneda(self.x, self.y)

	def mover (self):
		if self.direccion == 0:
			self.y -= 1
			if self.y < 0:
				self.y = 0
		elif self.direccion == 1:
			self.x += 1 
			if self.x > self.mapa.ancho :
				self.x = self.mapa.ancho
		elif self.direccion == 2:
			self.y += 1 
			if self.y > self.mapa.alto :
				self.y = self.mapa.alto
		else :
			self.x -= 1
			if self.x < 0:
				self.x = 0


