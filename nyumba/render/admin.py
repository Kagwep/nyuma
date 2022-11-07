from django.contrib import admin

# Register your models here.



from .models import SubCategoriesCars,SubCategories,Cars,Category,Property


admin.site.register(SubCategories)
admin.site.register(SubCategoriesCars)
admin.site.register(Category)
admin.site.register(Cars)
admin.site.register(Property)