from rest_framework.serializers import ModelSerializer
from loan.models import Loan
from collection.models import Item
from collection.api.serializers import ItemGetSerializer
from college.api.serializers import DisciplineGetSerializer
from myauth.models import MyUser
from myauth.api.serializers import MyUserSerializer
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
'''
{
    "student": 1,
    "students": [1,2],
    "professor": 1,
    "official_withdrawn": null,
    "official_deliver": null,
    "removal_planned_date": "2017-09-22",
    "delivery_planned_date": "2017-09-22",
    "terms": false,
    "items": [7,8,9],
    "external": false
}
'''

class LoanPostSerializer(ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Item.objects.filter(loan_items__isnull=True)
    )
    students = serializers.PrimaryKeyRelatedField(
            many=True, queryset=MyUser.objects.all())

    class Meta:
        model = Loan
        fields = (
            'id',
            'student',
            'students',
            'professor',
            'discipline',
            'official_withdrawn',
            'official_deliver',
            'removal_planned_date',
            'delivery_planned_date',
            'terms',
            'status',
            'items',
            'external',
        )

class LoanGetSerializer(ModelSerializer):
    items = ItemGetSerializer(many=True, read_only=True)
    students = MyUserSerializer(many=True, read_only=True)
    student = MyUserSerializer(read_only=True)
    professor = MyUserSerializer(read_only=True)
    official_withdrawn = MyUserSerializer(read_only=True)
    official_deliver = MyUserSerializer(read_only=True)
    status = serializers.SerializerMethodField()
    discipline = DisciplineGetSerializer(read_only=True)

    def get_status(self,obj):
        return obj.get_status_display()

    class Meta:
        model = Loan
        fields = (
            'id',
            'student',
            'students',
            'professor',
            'discipline',
            'official_withdrawn',
            'official_deliver',
            'removal_planned_date',
            'delivery_planned_date',
            'scheduled_date',
            'authorized_date',
            'removal_date',
            'delivery_date',
            'cancel_date',
            'terms',
            'status',
            'items',
            'external',
        )

