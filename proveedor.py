class Proveedor:
	def __init__(self, nit_empresa, nombre_empresa, id_representante, nombre_representante, telefono, correo):
		self.__nit_empresa = nit_empresa
		self.nombre_empresa = nombre_empresa
		self.__id_representante = id_representante
		self.nombre_representante = nombre_representante
		self.telefono = telefono
		self.correo = correo

	def get_nit_proveedor(self):
		return self.__nit_empresa

	def visualizar(self):
		print("El NIT de la empresa es: ", self.__nit_empresa)
		print("El Nombre del Proveedor es ", self.nombre_empresa)
		print("El Telefono de la Empresa es: ", self.telefono)
		print("El Correo de la Empresa es: ", self.correo)
		print("El ID del representante es: ", self.__id_representante)
		print("El Nombre del representante es: ", self.nombre_representante)





