from rest_framework.serializers import ModelSerializer
from college.models import Course, Discipline
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

class DisciplineSerializer(ModelSerializer):
    class Meta:
        model = Discipline
        fields = (
            'id',
            'name',
            'cod',
        )

class CourseSerializer(ModelSerializer):
    course_discipline = DisciplineSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'cod',
            'course_discipline',
        )


class DisciplineGetSerializer(ModelSerializer):
    course = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Discipline
        fields = (
            'id',
            'name',
            'cod',
            'course',
        )

