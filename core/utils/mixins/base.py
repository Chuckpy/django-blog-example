from django.db import models
from django.utils.translation import gettext_lazy as _



class BaseMixin(models.Model):
    class Meta :
        abstract = True
    
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(verbose_name=_("Created at"),auto_now_add=True)
    last_updated = models.DateTimeField(verbose_name=_("Last updated"),auto_now=True)


    