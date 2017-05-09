from django.contrib import admin
from .models import FoodTime, FoodPart, Food

# Register your models here.
admin.site.register(FoodTime)


class FoodPartAdmin(admin.ModelAdmin):
    list_display = ['name', 'food_time']


admin.site.register(FoodPart, FoodPartAdmin)


class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'part']


admin.site.register(Food, FoodAdmin)
