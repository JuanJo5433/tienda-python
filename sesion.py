from os import system
from user import User
from getpass import getpass

class Sesion:
	def __init__(self):

		admin = User("admin", "admin", "admin")
		self.__users = [admin]
		
	def buscar_usuario(self, username):
		for i in range(len(self.__users)):
			if self.__users[i].get_username() == username:
				return i
		return -1

	
	def registrar_usuario(self):
		system("cls")
		print("REGISTRAR")
		nom = input("Ingrese su usuario: ")
		pwd = getpass("Ingrese la contraseña: ")
		rol = input("Ingrese el tipo de usuario: ")

		user = User(nom, pwd, rol)
		pos = self.buscar_usuario(user.get_username())
		if pos == -1:
			self.__users.append(user)
			input()
			return True


	def comprobar_ingreso(self, username, password):
		pos = self.buscar_usuario(username)
		if pos != -1:
			if self.__users[pos].get_username() == username and self.__users[pos].get_password() == password:
				return 1
		return False


	def comprobar_ingreso_rol(self, username):
		for user in self.__users:
			if user.get_username() == username:
				return user.role
		return False