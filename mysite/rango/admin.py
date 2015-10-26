from django.contrib import admin

from rango.models import Category
from rango.models import Page
# Register your models here.

admin.site.register(Category)


# To customise the admin interface, you will need to edit rango/admin.py and create a PageAdmin class that inherits from admin.ModelAdmin.
# Within your new PageAdmin class, add list_display = ('title', 'category', 'url').

class PageAdmin(admin.ModelAdmin):
	 list_display = ('title','category','url')


admin.site.register(Page, PageAdmin)