# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models
from datetime import datetime
from myauth.models import MyUser
from collection.models import Item
from college.models import Discipline
# Create your models here.
class Loan(models.Model):
    """ Model used of the Loan table
    """
    SCHEDULED = 0
    AUTHORIZED = 1
    WITHDRAWN = 2
    DELIVERED = 3
    CANCELED = 4
    STATUS = (
        (SCHEDULED, _('Agendado')),
        (AUTHORIZED, _('Autorizado')),
        (WITHDRAWN, _('Retirado')),
        (DELIVERED, _('Entregue')),
        (CANCELED, _('Cancelado')),
    )
    # Student sponsored of the loan
    student = models.ForeignKey(
            MyUser, verbose_name=_('Student'), related_name='loan_student')
    # Students that participate the loan
    students = models.ManyToManyField(
            MyUser, verbose_name=_('Students'), related_name='loan_students')
    # Professor sponsored the students
    professor = models.ForeignKey(
            MyUser, verbose_name=_('Professor'), related_name='loan_professor')
    # Discipline that the loan will be used
    discipline = models.ForeignKey(Discipline, verbose_name='Disciplina',
            related_name='loan_discipline')
    # Official sponsored to withdrawn the equipments
    official_withdrawn = models.ForeignKey(
            MyUser, verbose_name=_('Official Withdrawn'),
            related_name='loan_official_withdrawn',
            null=True,
            blank=True)
    # Official sponsored to receive
    official_deliver = models.ForeignKey(
            MyUser, verbose_name=_('Official Deliver'),
            related_name='loan_official_deliver',
            null=True,
            blank=True)
    # Date scheduled to student retrieve the objects
    removal_planned_date = models.DateField(_('Removal planned date'))
    # Date scheduled to student delivery the objects
    delivery_planned_date = models.DateField(_('Delivery planned date'))
    # Date that the object was scheduled by the student
    scheduled_date = models.DateTimeField(
            _('Scheduled date'), editable=False, null=True, blank=True)
    # Date that the object was authorized by the professor
    authorized_date = models.DateTimeField(
            _('Authorized date'), editable=False, null=True, blank=True)
    # Actualy date that the object was retrieved by the student
    removal_date = models.DateTimeField(
            _('Removal date'), editable=False, null=True, blank=True)
    # Actualy date that the object was delivered by the student
    delivery_date = models.DateTimeField(
            _('Delivery date'), editable=False, null=True, blank=True)
    # Date that the object was canceled
    cancel_date = models.DateTimeField(
            _('Cancel date'), editable=False, null=True, blank=True)
    # Reservations of something
    reservation = models.TextField(_('Reservation'), null=True, blank=True)
    # Terms on this loan
    terms = models.BooleanField(_('Terms'), default=False,
        help_text=_('Designates if the user accepted the terms of use'))
    # Status of this Loan, Scheduled = 0, Withdrawn = 1, Delivered = 2
    status = models.SmallIntegerField(_('Status'), default=0, choices=STATUS)
    # Itens of this Loan
    items = models.ManyToManyField(
            Item, verbose_name=_('Items'), related_name='loan_items')
    # Boolean that indicates if this loan will be outside of campus
    external = models.BooleanField(_('External'), default=False)

    class Meta:
        verbose_name = (u'Empréstimo')
        verbose_name_plural = (u'Empréstimos')

    # Overwriting the save to update the dates when the status change
    def save(self, *args, **kwargs):
        old_status = False
        if self.pk:
            old_status = Loan.objects.get(id=self.pk).status
        if self.pk and old_status != self.status:
            if self.status == Loan.WITHDRAWN:
                self.removal_date = datetime.now().date()
            if self.status == Loan.DELIVERED:
                self.delivery_date = datetime.now().date()
        super(Loan, self).save(*args, **kwargs)

