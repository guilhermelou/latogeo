from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(_('Nome'), max_length=100)
    cod = models.CharField(
            _('Codigo'), max_length=100, unique=True, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = (_('Curso'))
        verbose_name_plural = (_('Cursos'))



class Discipline(models.Model):
    name = models.CharField(_('Nome'), max_length=100)
    cod = models.CharField(
            _('Codigo'), max_length=100, unique=True, null=True, blank=True)
    course = models.ForeignKey(
            Course, verbose_name=_('Curso'), related_name='course_discipline')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = (_('Disciplina'))
        verbose_name_plural = (_('Disciplinas'))

