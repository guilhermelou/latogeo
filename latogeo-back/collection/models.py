from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.


class ItemKind(models.Model):
    """ Model to define the kind of the specification of the item with name,
    description and category"""

    EQUIPAMENT = 0
    ACCESSORY = 1
    CATEGORY = (
        (EQUIPAMENT, _('Scheduled')),
        (ACCESSORY, _('Authorized')),
    )

    name = models.CharField(_('Kind'), max_length=100)
    description = models.TextField(_('Description'), null=True, blank=True)
    category = models.SmallIntegerField(
            _('Category'), default=0, choices=CATEGORY)

    def __unicode__(self):
		return self.name

    class Meta:
        verbose_name = (_('Tipo de Item'))
        verbose_name_plural = (_('Tipos de Item'))


class ItemSpec(models.Model):
    """ Model to define the specifications of the item, with name, description
    and kind"""

    name = models.CharField(_('Spec'), max_length=100)
    description = models.TextField(_('Description'), null=True, blank=True)
    kind = models.ForeignKey(
            ItemKind, verbose_name=_('Kind'), related_name='spec_kind')

    def __unicode__(self):
		return self.name

    class Meta:
        verbose_name = (_('Modelo do Item'))
        verbose_name_plural = (_('Modelos do Item'))


class Item(models.Model):
    """ Model to define the item, with patrimony, intern_id, and spec"""

    patrimony = models.CharField(
            _('Patrimony'), max_length=100, unique=True, null=True, blank=True)
    intern_id = models.CharField(
            _('ID Interno'), max_length=100, unique=True, null=True, blank=True)
    spec = models.ForeignKey(
            ItemSpec, verbose_name=_('Spec'), related_name='item_spec')

    def __unicode__(self):
		return self.patrimony

    class Meta:
        verbose_name = (_('Item'))
        verbose_name_plural = (_('Itens'))

