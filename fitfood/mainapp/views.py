from django.shortcuts import render
import random
from .models import FoodTime, FoodPart, Food

# Create your views here.
def index(request):
    food_list = []
    food_times = FoodTime.objects.all()
    for ft in food_times:
        time_dict = {}
        food_parts = FoodPart.objects.filter(food_time=ft)
        part_list = []
        for fp in food_parts:
            part_dict = {}
            foods = Food.objects.filter(part=fp)
            random_food = random.choice(foods)
            val = random_food
            part_dict[fp] = val
            part_list.append(part_dict)
        time_dict[ft] = part_list
        food_list.append(time_dict)
    return render(request,'index.html',{'food_list':food_list})