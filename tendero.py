class Tendero():
	def __init__(self, id_tendero, nombre_tendero, nit_tienda, nombre_tienda, telefono, correo, horario_trabajo, salario, direccion):
		self.__id_tendero = id_tendero
		self.nombre_tendero = nombre_tendero 
		self.__nit_tienda = nit_tienda
		self.nombre_tienda = nombre_tienda 
		self.telefono = telefono 
		self.correo = correo 
		self.horario_trabajo = horario_trabajo
		self.salario = salario
		self.direccion = direccion 
	
	def get_id_tendero(self):
		return self.__id_tendero

	def get_nit_tienda(self):
		return self.__nit_tienda 

	def visualizar_tendero(self):
		print("ID del tendero: ",self.__id_tendero)
		print("Nombre del tendero: ",self.nombre_tendero)
		print("NIT de la tienda: ",self.__nit_tienda)
		print("Nombre de la tienda: ",self.nombre_tienda)
		print("Telefono del tendero: ",self.telefono)
		print("Correo del tendero: ",self.correo)
		print("horario de trabajo: ",self.horario_trabajo)
		print("Salario: ",self.salario)
		print("Direccion: ",self.direccion)