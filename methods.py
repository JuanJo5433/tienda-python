from os import system

from tienda import Tienda
from cliente import Cliente
from proveedor import Proveedor
from user import User
from tendero import Tendero




class Methods:
	def __init__(self):
		
		self.__tiendas = []
		self.__clientes = []
		self.__proveedores = []
		self.__tenderos = []
		self.__inventarios = []
		self.__ventas = []
	
		

	def cuadro_para_mensaje(self, texto):
		longitud = len(texto)
		borde = '|' + '-' * (longitud + 20) + '|'
		contenido = '|          ' + texto + '          |'

		print(borde)
		print(contenido)
		print(borde)

	def cuadro_para_alerta(self, alerta, tipo):
		reiniciar = '\033[0m'
		rojo = '\033[91m'
		verde = '\033[92m'
		if tipo == 'info':
			longitud = len(alerta)
			borde = '+' * (longitud + 10) + '+'
			contenido = verde + '     ' + alerta + '     ' + reiniciar 

			print(borde)
			print(contenido)
			print(borde)
			input("Presiona ENTER para continuar...")
		if tipo == 'error':
			longitud = len(alerta)
			borde = '+' * (longitud + 10) + '+'
			contenido = rojo + '     ' + alerta + '     ' + reiniciar 

			print(borde)
			print(contenido)
			print(borde)
			input("Presiona ENTER para continuar...")

	# def listar_usuarios(self):
	# 	for user in self.__users:
	# 		user.visualizar()

	


	def adicionar_tienda(self, tienda):
		pos = self.buscar_tienda(tienda.get_nit_tienda())
		if pos == -1:
			self.__tiendas.append(tienda)
			
			return True
		return False

	def visualizar_tienda(self, num_tienda):
		pos = self.buscar_tienda(num_tienda)
		if pos != -1:
			if self.__tiendas[pos].visualizar_tienda():
				return True
		return False

	def modificar_tienda(self, num_tienda):
		cont = 0
		pos = self.buscar_tienda(num_tienda)
		if pos != -1:
			if self.__tiendas[pos].get_nit_tienda() == num_tienda:
				while True:
					system("cls")
					print("|----------------------------------------------|")
					print("|            OPCIONES PARA MODIFICAR           |")
					print("|----------------------------------------------|")

					try:
						print("|----------------------------------------------|")
						print("|  1 = Modificar nombre de la tienda           |")
						print("|  2 = Modificar direccion de la tienda        |")
						print("|  3 = Modificar telefono de la tienda         |")
						print("|  4 = Modificar correo de la tienda           |")
						print("|  0 = Salir                                   |")
						print("|----------------------------------------------|")

						op = int(input("Ingrese una opcion: "))

						if op == 0:
							if cont > 0:
								return True
								break
							else:
								self.cuadro_para_alerta(" Info - No se realizo ningun cambio ", "info")
								break



						elif op == 1:
							nombre_tienda_nuevo = input("Ingrese el nuevo nombre de la tienda: ") 
							self.__tiendas[pos].nombre_tienda = nombre_tienda_nuevo
							self.cuadro_para_alerta(" Info - El nombre fue modificado exitosamente ", "info")
							cont += 1
						elif op == 2:
							direccion_nueva = input("Ingrese la nueva direccion de la tienda: ")
							self.__tiendas[pos].direccion = direccion_nueva
							self.cuadro_para_alerta(" Info - La direccion fue modificada exitosamente ", "info")
							cont += 1
						elif op == 3:
							telefono_nuevo = input("Ingrese el nuevo telefono de la tienda: ")
							self.__tiendas[pos].telefono = telefono_nuevo
							self.cuadro_para_alerta(" Info - El telefono fue modificado exitosamente ", "info")
							cont += 1
						elif op == 4:
							correo_nuevo = input("Ingrese el nuevo correo de la tienda: ")
							self.__tiendas[pos].correo = correo_nuevo
							self.cuadro_para_alerta(" Info - El correo fue modificado exitosamente ", "info")
							cont += 1
						else:
							self.cuadro_para_alerta(" Error - La opcion no es valida ", "error")
							return False

					except ValueError:
						self.cuadro_para_alerta("Error - El dato debe ser entero.", "error")
						return False
			else:
				return False
		else:
			self.cuadro_para_alerta("Error - El NIT de la tienda no existe", "error")

	def eliminar_tienda(self, num_tienda):
		pos = self.buscar_tienda(num_tienda)

		if pos != -1:
			del(self.__tiendas[pos])
			return True
		return False

	def listar_tiendas(self):
		for tienda in self.__tiendas:
			print("___________________________________________________")
			tienda.visualizar_tienda()
#___________________________________________________________________________________________________________________________#

	def buscar_cliente(self, id_cliente):
		for i in range(len(self.__clientes)):
			if self.__clientes[i].get_id_cliente() == id_cliente:
				return i
		return -1

	def adicionar_cliente(self, cliente):
		pos = self.buscar_cliente(cliente.get_id_cliente())
		if pos == -1:
			self.__clientes.append(cliente)
			return True
		return False

	def visualizar_cliente(self, id_cliente):
		pos = self.buscar_cliente(id_cliente)
		if pos != -1:
			if self.__clientes[pos].visualizar_cliente():
				return True
		return False

	def modificar_cliente(self, id_cliente):
		cont = 0
		pos = self.buscar_cliente(id_cliente)
		if pos != 1:
			if self.__clientes[pos].get_id_cliente() == id_cliente:
				while True:
				

					try:
						system("cls")
						print("|----------------------------------------------|")
						print("|            OPCIONES PARA MODIFICAR           |")
						print("|----------------------------------------------|")
						print("|----------------------------------------------|")
						print("|  1 = Modificar nombre del cliente            |")
						print("|  2 = Modificar telefono del cliente          |")
						print("|  3 = Modificar correo del cliente            |")
						print("|  0 = Salir                                   |")
						print("|----------------------------------------------|")

						op = int(input("Ingrese una opcion: "))

						if op == 0:
							if cont > 0:
								return True
								break
							else:
								self.cuadro_para_alerta(" Info - No se realizo ningun cambio ", "info")
								break

						elif op == 1:
							nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
							self.__clientes[pos].nombre_cliente = nuevo_nombre
							self.cuadro_para_alerta(" Info - El nombre fue modificado exitosamente ", "info")
							cont += 1

						elif op == 2:
							nuevo_telefono = input("Ingrese el nuevo telefono del cliente: ")
							self.__clientes[pos].telefono_cliente = nuevo_telefono
							self.cuadro_para_alerta(" Info - El telefono fue modificado exitosamente ", "info")
							cont += 1
						
						elif op == 3:
							nuevo_correo = input("Ingrese el nuevo correo del cliente: ")
							self.__clientes[pos].correo_cliente = nuevo_correo
							self.cuadro_para_alerta(" Info - El correo fue modificado exitosamente ", "info")
							cont += 1

					except ValueError:
						self.cuadro_para_alerta(" Error - el dato debe ser entero ", "error" )
						return False
			else:
				return False
		else:
			self.cuadro_para_alerta("Error - El documendo del cliente no existe", "error")
	def eliminar_cliente(self, id_cliente):
		pos = self.buscar_cliente(id_cliente)
		if pos != -1:
			del(self.__clientes[pos])
			return True
		else:
			return False
		
	def listar_clientes(self):
		for cliente in self.__clientes:
			print("___________________________________________________")
			cliente.visualizar_cliente()
		input()

#___________________________________________________________________________________________________________________________#
	def buscar_proveedor(self, nit_proveedor):
		for i in range(len(self.__proveedores)):
			self.__proveedores[i].get_nit_proveedor() == nit_proveedor
			return i
		return -1

	def adicionar_proveedor(self, proveedor):
		pos = self.buscar_proveedor(proveedor.get_nit_proveedor())
		if pos == -1:
			self.__proveedores.append(proveedor)
			return True
		return False

	def visualizar_proveedor(self, nit_proveedor):
		pos= self.buscar_proveedor(nit_proveedor)
		if pos != -1:
			if self.__proveedores[pos].visualizar():
				return True
		return False


	def modificar_proveedor(self, nit_proveedor):
		pos = self.buscar_proveedor(nit_proveedor)
		cont = 0
		if pos != -1:
			while True:
				try:
					system("cls")
					print("|----------------------------------------------|")
					print("|            OPCIONES PARA MODIFICAR           |")
					print("|----------------------------------------------|")
					print("|----------------------------------------------|")
					print("|  1 = Modificar nombre del proveedor          |")
					print("|  2 = Modificar nombre del representante      |")
					print("|  3 = Modificar telefono                      |")
					print("|  4 = Modificar correo                        |")
					print("|  0 = Salir                                   |")
					print("|----------------------------------------------|")

					op = int(input("Ingrese una opcion: "))

					if op == 0:
						if cont > 0:
							return True
							break
						else:
							self.cuadro_para_alerta(" Info - No se realizo ningun cambio ", "info")
							break
					elif op == 1:
						nombre_empresa_nuevo = input("Ingrese el nuevo nombre de la empresa: ")
						self.__proveedores[pos].nombre_empresa = nombre_empresa_nuevo
						self.cuadro_para_alerta(" Info - El telefono fue modificado exitosamente ", "info")
						cont += 1
					elif op == 2:
						nombre_representante_nuevo = input("Ingrese el nuevo nombre del representante de la empresa: ")
						self.__proveedores[pos].nombre_representante = nombre_representante_nuevo
						self.cuadro_para_alerta(" Info - El telefono fue modificado exitosamente ", "info")
						cont += 1
					elif op == 3:
						nuevo_telefono = input("Ingrese el telefono nuevo telefono de la empresa: ")
						self.__proveedores[pos].telefono = nuevo_telefono
						self.cuadro_para_alerta(" Info - El telefono fue modificado exitosamente ", "info")
						cont += 1
					elif op == 4:
						nuevo_correo = input("Ingrese el nuevo correo de la empresa: ")
						self.__proveedores[pos].correo = nuevo_correo
						self.cuadro_para_alerta(" Info - El telefono fue modificado exitosamente ", "info")
						cont += 1
					else:
						self.cuadro_para_alerta(" Error - La opcion no es valida ", "error")

				except ValueError:
					self.cuadro_para_alerta(" Error - Ingrese un numero entero ")



	def eliminar_proveedor(self):
		pos = self.buscar_proveedor(num_proveedor)
		if pos != -1:
			del(self.__proveedores[pos])
			return True 
		return False 
	
	def listar_proveedores(self):
		for proveedor in self.__proveedor:
			print("___________________________________________________")
			proveedor.visualizar()
		input()

	def buscar_tendero(self, id_tendero):
		for i in range(len(self.__tenderos)):
			if self.__tenderos[i].get_id_tendero() == id_tendero:
				return i 
		return -1 

	def adicionar_tendero(self, tendero):
		pos = self.buscar_tendero(tendero.get_id_tendero())
		if pos == -1:
			self.__tenderos.append(tendero)
			return True 
		return False 

	def visualizar_tendero(self, num_tendero):
		pos = self.buscar_tendero(num_tendero)
		if pos != -1:
			if self.__tenderos[pos].visualizar_tendero():
				return True 
		return False 

	def modificar_tendero(self, num_tendero):
		pos = self.buscar_tendero(num_tendero)
		cont = 0
		if pos != -1:
			while True:
				try:
					system("cls")
					print("|----------------------------------------------|")
					print("|            OPCIONES PARA MODIFICAR           |")
					print("|----------------------------------------------|")
					print("|----------------------------------------------|")
					print("|  1 = Modificar Nombre del tendero            |")
					print("|  2 = Modificar Telefono                      |")
					print("|  3 = Modificar Correo                        |")
					print("|  4 = Modificar Horario de trabajo            |")
					print("|  5 = Modificar Salario                       |")
					print("|  6 = Modificar Direccion                     |")
					print("|  0 = Salir                                   |")
					print("|----------------------------------------------|")

					op = int(input("Ingrese una opcion: "))

					if op == 0:
						if cont > 0:
							return True
							break
						else:
							self.cuadro_para_alerta(" Info - No se realizo ningun cambio ", "info")
							break
					elif op == 1:
						nombre_tendero_nuevo = input("Ingrese el nuevo nombre de la tendero: ")
						self.__tenderos[pos].nombre_tendero = nombre_tendero_nuevo
						self.cuadro_para_alerta(" Info - El nombre del tendero fue modificado exitosamente ", "info")
						cont += 1
					elif op == 2:
						telefono_nuevo = input("Ingrese el nuevo nombre del representante de la tendero: ")
						self.__tenderos[pos].telefono = telefono_nuevo
						self.cuadro_para_alerta(" Info - El telefono fue modificado exitosamente ", "info")
						cont += 1
					elif op == 3:
						nuevo_correo = input("Ingrese el nuevo correo de la tendero: ")
						self.__tenderos[pos].correo = nuevo_correo
						self.cuadro_para_alerta(" Info - El correo fue modificado exitosamente ", "info")
						cont += 1
					elif op == 4:
						horario_trabajo = input("Ingrese el nuevo correo de la tendero: ")
						self.__tenderos[pos].horario_trabajo = horario_trabajo
						self.cuadro_para_alerta(" Info - El horario de trabajo fue modificado exitosamente ", "info")
						cont += 1
					elif op == 5:
						salario = input("Ingrese el nuevo salario de la tendero: ")
						self.__tenderos[pos].salario = salario
						self.cuadro_para_alerta(" Info - El salario fue modificado exitosamente ", "info")
						cont += 1
					elif op == 6:
						direccion = input("Ingrese el nuevo correo de la tendero: ")
						self.__tenderos[pos].direccion = direccion
						self.cuadro_para_alerta(" Info - La dirrecion fue modificado exitosamente ", "info")
						cont += 1
					else:
						self.cuadro_para_alerta(" Error - La opcion no es valida ", "error")

				except ValueError:
					self.cuadro_para_alerta(" Error - Ingrese un numero entero ")
			else:
				return False
		else: return False

	def eliminar_tendero(self, num_tendero):
		pos = self.buscar_tendero(num_tendero)
		if pos != -1:
			del(self.__tenderos[pos])
			return True 
		return False

	def listar_tenderos(self):
		for tendero in self.__tenderos:
			print("___________________________________________________")
			tendero.visualizar_tendero()