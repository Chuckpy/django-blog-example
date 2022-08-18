from django.contrib import admin
from .models import CoreUser, StaffUser


class CoreUserAdmin(admin.ModelAdmin):    
    pass

class StaffUserAdmin(admin.ModelAdmin):    
    pass



admin.site.register(StaffUser, StaffUserAdmin)
admin.site.register(CoreUser, CoreUserAdmin)

