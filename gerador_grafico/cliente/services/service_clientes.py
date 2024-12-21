from ..repositories.repositorio_cliente import RepositorioCliente

class ServiceClientes:

    def __init__(self):
        self._repositorio_clientes = RepositorioCliente()

    def listar_clientes(self):
        return self._repositorio_clientes.listar_clientes()