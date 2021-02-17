from django.contrib import admin
from products.models import Product, Offer, New


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class NewAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'date')


admin.site.site_header = 'Miran-shop'
admin.site.site_title = 'Miran Admin Area'
admin.site.index_title = 'Welcome to the  Miran Admin Area'

admin.site.register(Product, ProductAdmin),
admin.site.register(Offer, OfferAdmin),
admin.site.register(New, NewAdmin),
