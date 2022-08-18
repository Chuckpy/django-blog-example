from django.contrib import admin
from .models import PostObject, Type, KeyWords


class PostObjectAdmin(admin.ModelAdmin):    
    pass

class KeyWordsAdmin(admin.ModelAdmin):    
    pass

class TypeAdmin(admin.ModelAdmin):    
    pass



admin.site.register(Type, TypeAdmin)
admin.site.register(KeyWords, KeyWordsAdmin)
admin.site.register(PostObject, PostObjectAdmin)

