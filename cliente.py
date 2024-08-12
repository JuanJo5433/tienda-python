class Cliente:
    def __init__(self, id_cliente, nombre_cliente, telefono_cliente, correo_cliente):
        self.__id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente
        self.telefono_cliente = telefono_cliente
        self.correo_cliente = correo_cliente
		
        

    def get_id_cliente(self):
        return self.__id_cliente

    def visualizar_cliente(self):
        print("El numero de documento del cliente es: ", self.__id_cliente)
        print("El nombre completo del cliente es: ", self.nombre_cliente)
        print("El telefono del cliente es: ", self.telefono_cliente)
        print("El correo del cliente es: ", self.correo_cliente)