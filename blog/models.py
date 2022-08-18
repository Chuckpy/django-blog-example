from django.db import models
from core.utils.mixins.base import BaseMixin
from django.utils.translation import gettext_lazy as _
from users.models import CoreUser



class KeyWords(BaseMixin):
    class Meta :
        verbose_name = _("Key Word")
        verbose_name_plural = _("Key Words")

    name = models.CharField(max_length=255)

    def __str__(self) :
        return f"Keyword {self.name}"

class Type(BaseMixin):
    class Meta :
        verbose_name = _("Type")
        verbose_name_plural = _("Types")

    name = models.CharField(max_length=255)

    def __str__(self) :
        return f"Type {self.name}"

class PostObject(BaseMixin): 
    class Meta :
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    author = models.ForeignKey(CoreUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=5000)
    status = models.BooleanField()
    keywords_set = models.ManyToManyField(KeyWords)

    def __str__(self) :
        return f"Post {self.title}"

