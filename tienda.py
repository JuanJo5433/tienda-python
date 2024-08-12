class Tienda:
	def __init__(self, nit_tienda, nombre_tienda, direccion, telefono, correo):
		self.__nit_tienda = nit_tienda
		self.nombre_tienda = nombre_tienda
		self.direccion = direccion
		self.telefono = telefono
		self.correo = correo

	def get_nit_tienda(self):
		return self.__nit_tienda

	def visualizar_tienda(self):
		print("El NIT de la tienda es: ", self.__nit_tienda)
		print("El nombre de la tienda es: ", self.nombre_tienda)
		print("La direccion de la tienda es: ", self.direccion)
		print("El telefono de la tienda es: ", self.telefono)
		print("El correo de la tienda es: ", self.correo)
