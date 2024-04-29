from django.contrib import admin
from .models import *
from django.utils.html import format_html
from ckeditor.fields import RichTextField

# Register your models here.



class ShopAdmin(admin.ModelAdmin):
    # readonly_fields = ('photo_tag' , )
    list_display = ('name', 'image', 'price', 'less_content')
    list_filter =['name']
    search_fields =['name']
    list_display_links = ('name', 'price','less_content' )
    save_on_top = True
    list_per_page = 3

    def less_content(self , obj):
        return obj.description[:200]

    # def photo_tag(self , obj):
    #     return format_html(f'<img src="/media/{obj.image}" style ="height:100px; width:100px;">')


admin.site.register(Shop,ShopAdmin)



class DecorationAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price', 'less_content')
    list_filter =['name']
    search_fields =['name']
    list_display_links = ('name', 'price','less_content' )
    save_on_top = True
    list_per_page = 3

    def less_content(self, obj):
        return obj.description[:200]

admin.site.register(Decoration, DecorationAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    list_filter =['name']
    search_fields =['name']
    save_on_top = True
    list_per_page = 3

    def less_content(self, obj):
        return obj.description[:200]
admin.site.register(Category, CategoryAdmin)



class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    list_filter =['name']
    search_fields =['name']
    save_on_top = True
    list_per_page = 3

    def less_content(self, obj):
        return obj.description[:200]
admin.site.register(SubCategory, SubCategoryAdmin)



class SubSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price', 'less_content')
    list_filter =['name']
    search_fields =['name']
    list_display_links = ('name', 'price','less_content' )
    save_on_top = True
    list_per_page = 3

    def less_content(self, obj):
        return obj.description[:200]

admin.site.register(SubSubCategory, SubSubCategoryAdmin)







# admin.site.register(Cake)
# admin.site.register(Cupcake)
# admin.site.register(Weddingcake)
# admin.site.register(Brownie)



