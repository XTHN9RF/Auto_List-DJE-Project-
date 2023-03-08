from django.contrib import admin

# Register your models here.
from cats.models import Cat, Breed

admin.register(Cat)
admin.register(Breed)
