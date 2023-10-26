from django.contrib import admin
from .models import Product , Order
# Register your models here.

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Apna Shop"
admin.site.index_title = "Apna Shop Admin"




class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'price','discount_price','category')
    search_fields = ['title','category']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name','email','city','total')
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)