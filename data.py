from methods import Methods
from os import system
from getpass import getpass

from tienda import Tienda
from cliente import Cliente
from proveedor import Proveedor
from user import User
from tendero import Tendero
from sesion import Sesion

class Data:
	def __init__(self):
	   self.methods = Methods()
	   self.sesion = Sesion()
	  


	def crear_tienda(self):
		system("cls")
		self.methods.cuadro_para_mensaje("CREAR TIENDA")

		nit_tienda = input("Ingrese el NIT de la tienda: ")
		nombre_tienda = input("Ingrese el nombre de la tienda: ")
		direccion = input("Ingrese la direccion de la tienda: ")
		telefono = input("Ingrese el telefono de la tienda: ")
		correo = input("Ingrese el correo de la tienda: ") 
		



		tienda = Tienda(nit_tienda, nombre_tienda, direccion, telefono, correo)

		if self.methods.adicionar_tienda(tienda):
			self.methods.cuadro_para_alerta("Info - La tienda se creó correctamente", "info")
		else:
			self.methods.cuadro_para_alerta("Error - La NIT de la tienda ya existe en el sistema", "error")

	def pedir_datos_visualizar_tienda(self):
		system("cls")
		self.methods.cuadro_para_mensaje("VISUALIZAR TIENDA")

		num_tienda = input("Digite el NIT de la tienda: ")
		pos = self.methods.buscar_tienda(num_tienda)

		if pos != -1:
			self.methods.visualizar_tienda(num_tienda)
			input("Presiona ENTER para continuar...")
		else:
			self.methods.cuadro_para_alerta("Error - La tienda no existe en el sistema", "error")
			
	def modificar_datos_tienda(self):
		system("cls")
		self.methods.cuadro_para_mensaje("MODIFICAR TIENDA")
		num_tienda = input("Digite el NIT de la tienda: ")

		if self.methods.modificar_tienda(num_tienda):
			self.methods.cuadro_para_alerta("Info - Los datos de la tienda fueron modificados correctamente", "info")
		
	def pedir_datos_eliminar_tienda(self):
		system("cls")
		self.methods.cuadro_para_mensaje("ELIMINAR TIENDA")
		num_tienda = input("Digite el NIT de la tienda que desea eliminar: ")

		if self.methods.eliminar_tienda(num_tienda):
			self.methods.cuadro_para_alerta("Info - La tienda fue eliminada correctamente del sistema", "info")
		else:
			self.methods.cuadro_para_alerta("Error - La tienda no existe en el sistema", "error")

	def listar_tiendas_en_sistema(self):
		system("cls")
		self.methods.cuadro_para_mensaje("TIENDAS EN SISTEMA")
		self.methods.listar_tiendas()
		input()

	#___________________________________________________________________________________________________________________________________________________________________

	def pedir_datos_crear_cliente(self):
		system("cls")
		self.methods.cuadro_para_mensaje("CREAR CLIENTE")
		id_cliente = input("Ingrese el numero de documento del cliente: ")
		nombre_cliente = input("Ingrese el nombre completo del cliente: ")
		telefono_cliente = input("Ingrese el telefono del cliente: ")
		correo_cliente = input("Ingrese el correo del cliente: ")
		cliente = Cliente(id_cliente, nombre_cliente, telefono_cliente, correo_cliente)
	
		if self.methods.adicionar_cliente(cliente):
			self.methods.cuadro_para_alerta("Info - El cliente se creó correctamente", "info")
		else:
			self.methods.cuadro_para_alerta("Error - El documento del ya existe en el sistema", "error")

		
		# nom = input("Ingrese su usuario: ")
		# pwd = getpass("Ingrese la contraseña: ")
		# rol = "cliente"
		# user = User(nom, pwd, rol)
		
		if self.sesion.registrar_usuario():
			self.methods.cuadro_para_alerta("El usuario fue creado exitosamente", "info")
		else:
			self.methods.cuadro_para_alerta("El nombre de usuario ya existe", "error")



	def pedir_datos_visualizar_cliente(self):
		system("cls")
		self.methods.cuadro_para_mensaje("VISUALIZAR CLIENTE")

		id = input("Ingrese el numero de documento del cliente: ")
		pos = self.methods.buscar_cliente(id)

		if pos != -1:
			self.methods.visualizar_cliente(id)
			input("Presiona ENTER para continuar...")
		else:
			self.methods.cuadro_para_alerta("Error - El cliente no existe en el sistema", "error")

	def pedir_datos_modificar_cliente(self):
		system("cls")
		self.methods.cuadro_para_mensaje("MODIFICAR CLIENTE")

		id_cliente = input("Ingrese el numero de documento del cliente que desea modificar: ")

		if self.methods.modificar_cliente(id_cliente):
			self.methods.cuadro_para_alerta(" Info - Los cambios fueron realizados y guardados correctamente", "info")

	def pedir_datos_eliminar_cliente(self):
		system("cls")
		self.methods.cuadro_para_mensaje("ELIMINAR CLIENTE")

		id_cliente = input("Ingrese el numero de documento del cliente que desea eliminar: ")

		if self.methods.eliminar_cliente(id_cliente):
			self.methods.cuadro_para_alerta(" Info - El cliente fue eliminado del sistema exitosamente", "info")
		else: 
			self.methods.cuadro_para_alerta(" Error - El cliente no existe en el sistema", "error")

	def listar_clientes_del_sistema(self):
		system("cls")
		self.methods.cuadro_para_mensaje("CLIENTES DEL SISTEMA")
		self.methods.listar_clientes()

	#_____________________________________________________________________________________________________________________________________________________________ 

	def pedir_datos_crear_proveedor(self):
		system("cls")
		self.methods.cuadro_para_mensaje("CREAR PROVEEDOR")
		nit_empresa = input("Ingrese el NIT de la empresa proveedora: ")
		nombre_empresa = input("Ingrese el nombre de la empresa: ")
		id_representante = input("Ingrese el numero de identificacion del numero del representante de la empresa: ")
		nombre_representante = input("Ingrese el nombre del representante de la empresa: ")
		telefono = input("Ingrese el numero de telefono de la empresa: ")
		correo = input("Ingrese el correo de la empresa: ")
		proveedor = Proveedor(nit_empresa, nombre_empresa, id_representante, nombre_representante, telefono, correo)

		nom = input("Ingrese el nombre de usuario del proveedor: ")
		pwd = input("Ingrese la contraseña: ")
		rol = ("proveedor")
		user = User(nom, pwd, rol)

		

		if self.methods.adicionar_proveedor(proveedor):
			self.methods.cuadro_para_alerta(" Info - El proveedor fue creado o exitosamente ", "info")
		else:
			self.methods.cuadro_para_alerta(" Error - El provedor no fue creado", "error")

	def pedir_datos_visualizar_proveedor(self):
		system("cls")
		self.methods.cuadro_para_mensaje("VISUALIZAR PROVEEDOR")
		nit_proveedor = input("Ingrese el NIT del proveedor: ")
		pos = self.methods.buscar_proveedor(nit_proveedor)

		if pos != -1:
			self.methods.visualizar_proveedor(nit_proveedor)
			input("Presiona ENTER para continuar...")
		else:
			self.methods.cuadro_para_alerta(" Error - El proveedor no existe en el sistema ", "error")

	def pedir_datos_modificar_proveedor(self):
		self.methods.cuadro_para_mensaje("MODIFICAR PROVEEDOR")
	
		nit_proveedor = input("Ingrese el NIT del proveedor: ")

		if self.methods.modificar_proveedor(nit_proveedor):
			self.methods.cuadro_para_alerta(" Info - Los cambios fueron realizados y guardados exitosamente ", "info")

	def pedir_datos_eliminar_proveedor(self):
		self.methods.cuadro_para_mensaje("ELIMINAR PROVEEDOR")
		num_proveedor = input("Ingrese el NIT del proveedor: ")

		if self.methods.eliminar_proveedor(num_proveedor):
			self.methods.cuadro_para_alerta(" Info - El proveedor se elimino correctamente. ", "info")

		else:
			self.methods.cuadro_para_alerta(" Error - El proveedor no se pudo eliminar." , "error")

			
	def listar_proveedores_del_sistema(self):
		system("cls")
		self.methods.cuadro_para_mensaje("PROVEEDORES DEL SISTEMA")
		self.methods.listar_proveedores()

#_______________________________________________________________________________________


	def crear_tendero(self):
		system("cls")
		self.methods.cuadro_para_mensaje("CREAR TENDERO")
		id_tendero = input("Ingrese la identificacion del tendedero: ")
		nombre_tendero = input("Ingrese Nombre y Apellidos del tendero: ") 
		nit_tienda = input("Ingrese el NIT de la tienda: ")
		nombre_tienda = input("Ingrese el nombre de la tienda: ")
		telefono = input("Ingrese el telefono del tendero: ")
		correo = input("Ingrese el correo del tendero: ")
		horario_trabajo = input("Ingrese el horario de trabajo: ")
		salario = input("Ingrese el salario del tendero: ")
		direccion = input("Ingrese la direccion: ")

		nom = input("Ingrese el nombre de usuario del tendero: ")
		pwd = input("Ingrese la contraseña: ")
		rol = ("tendero")
		user = User(nom, pwd, rol)

		tendero = Tendero(id_tendero, nombre_tendero, nit_tienda, nombre_tienda, telefono, correo, horario_trabajo, salario, direccion)

		if self.methods.adicionar_tendero(tendero):
			self.methods.cuadro_para_alerta(" Info - El tendero se creo correctamente. ", "info")

		else:
			self.methods.cuadro_para_alerta(" Error - No se pudo crear el tendero. ", "error")


	def visualizar_tendero(self):
		system("cls")
		self.methods.cuadro_para_mensaje("VISUALIZAR TENDERO")
		num_tendero = input("Ingrese el ID del tendero: ")
		pos = self.methods.buscar_tendero(num_tendero)

		if pos != -1:
			self.methods.visualizar_tendero(num_tendero)
			input("Presiona ENTER para continuar...")

		else:
			self.methods.cuadro_para_alerta(" Error - No se pudo crear el tendero. ", "error")

	def modificar_tendero(self):
		system("cls")
		self.methods.cuadro_para_mensaje("MODIFICAR TENDERO")
		num_tendero = input("Ingrese el ID del tendero: ")

		if self.methods.modificar_tendero(num_tendero):
			
			self.methods.cuadro_para_alerta(" Info - Los cambios fueron realizados y guardados exitosamente ", "info")


	def eliminar_tendero(self):
		system("cls")
		self.methods.cuadro_para_mensaje("ELIMINAR TENDERO")
		
		num_tendero = input("Ingrese el ID del tendero: ")

		if self.methods.eliminar_tendero(num_tendero):
			self.methods.cuadro_para_alerta(" Info - El tendero se elimino correctamente. ", "info")

		else:
			self.methods.cuadro_para_alerta(" Error - El tendero no se pudo eliminar." , "error")

	def listar_tenderos(self):
		system("cls")
		self.methods.cuadro_para_mensaje("TENDEROS DEL SISTEMA")
		self.methods.listar_tenderos()
		input("Presione ENTER para continuar...")
