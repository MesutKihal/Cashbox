from django.contrib import admin

from .models import User, Item, Category

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Category)