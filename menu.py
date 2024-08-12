from os import system
from time import sleep
from methods import Methods
from data import Data
from tienda import Tienda
from cliente import Cliente
from proveedor import Proveedor
from user import User
from sesion import Sesion


class Menu:
	def __init__(self):
		self.data = Data()
		self.methods = Methods()
		self.sesion = Sesion()
		self.menu_cliente = Menu_cliente()


	def menu_inicio(self):
		while True:
			system("cls")
			print("|---------------------------|")
			print("|        SISTEMA            |")
			print("|---------------------------|")
			print("|Opciones                   |")
			print("|1 = Iniciar sesion         |")
			print("|2 = Registrarse            |")
			print("|0 = Salir del sistema      |")
			print("|---------------------------|")
			try:
				op = int(input("Digite una opción: "))
				if op == 0:
					print("Has salido del sistema.")
					break
				elif op == 1:
					if self.login():
						break
				elif op == 2:
					if self.sesion.registrar_usuario():
						input()
				else:
					self.methods.cuadro_para_alerta("Error - Opción no válida.", "error")
			except ValueError:
				self.methods.cuadro_para_alerta("Error - El dato debe ser entero", "error")

	def mostrar_menu_tiendas(self):
		while True:
			system("cls")
			print("+---------------------------------+")
			print("|           MENU TIENDAS          |")
			print("+---------------------------------+")
			print("|Opciones                         |")
			print("|1 = Crear tienda                 |")
			print("|2 = Visualizar tienda            |")
			print("|3 = Modificar tienda             |")
			print("|4 = Eliminar tienda              |")
			print("|5 = Listar tiendas               |")
			print("|6 = Regresar al menú principal   |")
			print("|0 = Cerrar sesion                |")
			print("+---------------------------------+")

			try:
				op = int(input("Digite una opción: "))
				if op == 0:
					print("Has salido del sistema.")
					return True
				elif op == 1:
					self.data.crear_tienda()
				elif op == 2:
					self.data.pedir_datos_visualizar_tienda()
				elif op == 3:
					self.data.modificar_datos_tienda()
				elif op == 4:
					self.data.pedir_datos_eliminar_tienda()
				elif op == 5:
					self.data.listar_tiendas_en_sistema()
				elif op == 6:
					return
				else:
					self.methods.cuadro_para_alerta("Error - Opción no válida.", "error")
			except ValueError:
				self.methods.cuadro_para_alerta("Error - El dato debe ser entero", "error")

	def mostrar_menu_clientes(self):
		while True:
			system("cls")
			print("|---------------------------------|")
			print("|           MENU CLIENTES         |")
			print("|---------------------------------|")
			print("|Opciones                         |")
			print("|1 = Crear Cliente                |")
			print("|2 = Visualizar Cliente           |")
			print("|3 = Modificar Cliente            |")
			print("|4 = Eliminar Cliente             |")
			print("|5 = Listar Clientes              |")
			print("|6 = Regresar al menú principal   |")
			print("|0 = Cerrar sesion                |")
			print("|---------------------------------|")

			try:
				op = int(input("Digite una opción: "))

				if op == 0:
					print("Has salido del sistema.")
					return True
				elif op == 1:
					self.data.pedir_datos_crear_cliente()
				elif op == 2:
					self.data.pedir_datos_visualizar_cliente()
				elif op == 3:
					self.data.pedir_datos_modificar_cliente()
				elif op == 4:
					self.data.pedir_datos_eliminar_cliente()
				elif op == 5:
					self.data.listar_clientes_del_sistema() 
				elif op == 6:
					return
				else:
					self.methods.cuadro_para_alerta("Error - Opción no válida.", "error")
			except ValueError:
				self.methods.cuadro_para_alerta("Error - El dato debe ser entero", "error")

	def mostrar_menu_proveedores(self):
		while True:
			system("cls")
			print("|------------------------------------|")
			print("|           MENU PROVEEDORES         |")
			print("|------------------------------------|")
			print("|Opciones                            |")
			print("|1 = Crear Proveedor                 |")
			print("|2 = Visualizar Proveedor            |")
			print("|3 = Modificar Proveedor             |")
			print("|4 = Eliminar Proveedor              |")
			print("|5 = Listar Proveedores              |")
			print("|6 = Regresar al menú principal      |")
			print("|0 = Cerrar sesion                   |")
			print("|------------------------------------|")
			try:
				op = int(input("Ingrese una opcion: "))

				if op == 0:
					self.methods.cuadro_para_alerta("Has salido del sistema", "info")
					return True
				elif op == 1:
					self.data.pedir_datos_crear_proveedor()
				elif op == 2:
					self.data.pedir_datos_visualizar_proveedor()
				elif op ==3:
					self.data.pedir_datos_modificar_proveedor()
				elif op == 4:
					self.data.pedir_datos_eliminar_proveedor()
				elif op == 5:
					self.data.listar_proveedores_del_sistema()
				elif op == 6:
					return
				else:
					self.methods.cuadro_para_alerta(" Error - La opcion no es valida", "error")
			
			except ValueError:
				self.methods.cuadro_para_alerta(" Error - El dato debe ser tipo entero ", "error")

	def mostar_menu_tenderos(self):
		while True:
			system("cls")
			print("|--------------------------------|")
			print("|          MENU TENDERO          |")
			print("|--------------------------------|")
			print("|1 = Crear tendero               |")
			print("|2 = Visualizar tendero          |")
			print("|3 = Modificar tendero           |")
			print("|4 = Eliminar tendero            |")
			print("|5 = Listar tenderos             |")
			print("|6 = Regresar al menú principal  |")
			print("|0 = Cerrar sesion               |")
			print("|--------------------------------|")
			try:
				op = int(input("Digite la opcion: "))
				
				if op == 0:
					self.methods.cuadro_para_alerta("Has salido del sistema", "info")
					return True

				elif op == 1:
					self.data.crear_tendero()
				elif op == 2: 
					self.data.visualizar_tendero()
				elif op == 3:
					self.data.modificar_tendero()
				elif op == 4:
					self.data.eliminar_tendero()
				elif op == 5:
					self.data.listar_tenderos()

				elif op == 6: 
					return 

				else:
					self.methods.cuadro_para_alerta(" Error - La opcion no es valida", "error")
			
			except ValueError:
				self.methods.cuadro_para_alerta(" Error - El dato debe ser tipo entero ", "error")

	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("|---------------------------|")
			print("|      MENU PRINCIPAL       |")
			print("|---------------------------|")
			print("|Opciones                   |")
			print("|1 = Menu de Tiendas        |")
			print("|2 = Menu de Clientes       |")
			print("|3 = Menu de Proveedores    |")
			print("|4 = Menu de Tenderos       |")
			print("|0 = Cerrar sesion          |")
			print("|---------------------------|")
			try:
				op = int(input("Digite una opción: "))
				if op == 0:
				
					return
				elif op == 1:
					if self.mostrar_menu_tiendas():
						break
				elif op == 2:
					if self.mostrar_menu_clientes():
						break
				elif op == 3:
					if self.mostrar_menu_proveedores():
						break
				elif op == 4:
					if self.mostar_menu_tenderos():
						break

				else:
					self.methods.cuadro_para_alerta("Error - Opción no válida.", "error")
			except ValueError:
				self.methods.cuadro_para_alerta("Error - El dato debe ser entero", "error")

	def login(self):
		
		system("cls")
		self.methods.cuadro_para_mensaje("INICIO DE SESION")
		nom = str(input("Ingrese su usuario: "))
		pwd = str(input("Ingrese la contraseña: "))

		if self.sesion.comprobar_ingreso(nom, pwd) == 1:
			rol = self.sesion.comprobar_ingreso_rol(nom)
			if rol == "admin":
				print(nom, "Bienvenido al sistema!")
				sleep(1)
				self.mostrar_menu_principal()
			elif rol == "cliente":
				print(nom, "Bienvenido al sistema!")
				sleep(2)
				self.menu_cliente.menu_cliente()
			elif rol == "proveedor":
				print(nom, "Bienvenido al sistema!")
				sleep(2)
				self.menu_proveedor.mostrar_menu_principal()
			else:
				self.methods.cuadro_para_alerta("Error - Rol no identificado", "error")
		else:
			self.methods.cuadro_para_alerta("Error - El usuario no existe", "error")






class Menu_admin:
	def __init__(self):
		self.data = Data()
		self.methods = Methods()
	
class Menu_cliente:
	def __init__(self):
		self.data = Data()
		self.methods = Methods()
	def menu_cliente(self):
		system("cls")
		print("|------------------------------------|")
		print("|           MENU CLIENTE             |")
		print("|------------------------------------|")
		print("|Opciones                            |")
		print("|1 = Visualizar compras              |")
		print("|2 = Listar compras                  |")
		print("|3 = Regresar al menú principal      |")
		print("|0 = Cerrar sesion                   |")
		print("|------------------------------------|")
		input()

if __name__ == '__main__':
	menu = Menu()
	menu.menu_inicio()
