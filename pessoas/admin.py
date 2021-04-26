from django.contrib import admin

# Register your models here.
from pessoas.models import Pessoa, Telefone

admin.site.register(Pessoa)
admin.site.register( Telefone)
