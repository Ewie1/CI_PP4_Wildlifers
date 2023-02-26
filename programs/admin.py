from django.contrib import admin
from .models import Animal, Country, Survival_cateogory, Program

# Register your models here.
admin.site.register(Animal)
admin.site.register(Country)
admin.site.register(Survival_cateogory)
admin.site.register(Program)
