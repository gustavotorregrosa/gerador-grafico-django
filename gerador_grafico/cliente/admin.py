from django.contrib import admin
from .models import Cliente
from mensagem.models import Mensagem

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Mensagem)
