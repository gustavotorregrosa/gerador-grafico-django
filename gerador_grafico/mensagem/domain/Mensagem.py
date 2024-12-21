from datetime import datetime

class Mensagem:

    id: int
    texto: str
    status: str
    entregue_em: datetime
    cliente_id: int

    def __init__(self, id, texto, status, entregue_em, cliente_id):
        self.id = id
        self.texto = texto
        self.status = status
        self.entregue_em = entregue_em
        self.cliente_id = cliente_id


    def to_dict(self):
        return {
            'id': self.id,
            'texto': self.texto,
            'status': self.status,
            'entregue_em': self.entregue_em,
            'cliente_id': self.cliente_id
        }
