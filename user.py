class User:
	def __init__(self, username, password, role):
		self.__username = username
		self.__password = password
		self.role = role
		
	
	

	def get_username(self):
		return self.__username

	def get_password(self):
		return self.__password

	# def get_rol(self):
	# 	return self.__rol
	
	# def visualizar(self):
	# 	print("usuario: ", self.__nom)
	# 	print("pwd: ", self.__pwd)
	# 	print("rol: ", self.__rol)

	

	# def comprobar_ingreso(self, nom, pwd):
	# 	for i in range(len(self.__users)):
	# 		if self.__users[i].nom == nom and self.__users[i].pwd == pwd:
	# 			print(self.__users[i, " Bienvenido al sistema!"])
	# 			sleep(3)
	# 			return True
	# 	return False