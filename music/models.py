import uuid

from django.db import models
from django.utils.translation import ugettext as _


#class Author(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#    name = models.CharField(max_length=400, verbose_name=_('name'))
#    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
#
#    class Meta:
#        verbose_name = _('author')
#        verbose_name_plural = _('authors')
#
#    def __str__(self):
#        return self.name


class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=400, verbose_name=_('name'))
    #author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('author'))
    author = models.CharField(max_length=400, verbose_name=_('author'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    class Meta:
        verbose_name = _('album')
        verbose_name_plural = _('albums')

    def __str__(self):
        return self.name
