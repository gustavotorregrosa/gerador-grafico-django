from typing import List
from mensagem.domain.Mensagem import Mensagem

class Cliente:

    id: int
    messages: List[Mensagem] = []	

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def add_message(self, message: Mensagem):
        self.messages.append(message)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'messages': [message.to_dict() for message in self.messages]
        }
