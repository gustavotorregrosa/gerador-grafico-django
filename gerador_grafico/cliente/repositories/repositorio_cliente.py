from django.db import connection
from cliente.domain.Cliente import Cliente

class RepositorioCliente:

    def listar_clientes(self) -> list[Cliente]:
        try:
            cursor = connection.cursor()
            cursor.callproc('listar_clientes')

            result = cursor.fetchall()
            cursor.close()
            connection.close()
            clientes = []
            for row in result:
                cliente = Cliente(row[0], row[1])
                clientes.append(cliente)
                
            return clientes
        
        except (Exception) as error:
            print(f"Error while calling listar_clientes: {error}")
            return None