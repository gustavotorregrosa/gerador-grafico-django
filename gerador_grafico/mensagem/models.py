from django.db import models
from cliente.models import Cliente

# Create your models here.
class Mensagem(models.Model):
    STATUS_CHOICES = [
        ('sucesso', 'Sucesso'),
        ('erro', 'Erro')
    ]

    class Meta:
        db_table = 'mensagens'
        verbose_name_plural = "Mensagens"

    id = models.AutoField(primary_key=True)
    texto = models.TextField()
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, null=True, blank=True)
    entregue_em = models.DateTimeField()
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE)

    def __str__(self):
        return self.texto
