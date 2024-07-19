from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('phone_number' , 'address')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(About_company)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Massage)
admin.site.register(Office)
admin.site.register(Banner)
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(Block_category)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Material)
admin.site.register(Product)
admin.site.register(Logo)
