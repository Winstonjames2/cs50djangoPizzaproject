from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(FoodType)
admin.site.register(Size)
admin.site.register(Feature)
admin.site.register(Food)
admin.site.register(Cart)
admin.site.register(Times)