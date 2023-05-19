from rest_framework import serializers

from common.models import ApplicationForm


class ApplicationFormSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField()

    class Meta:
        model = ApplicationForm
        fields = ('id', 'name', 'email', 'course_id',)
        read_only_fields = ("id",)

    def validate(self, attrs):
        name = attrs.get('name')
        email = attrs.get('email')
        course_id = attrs.get('course_id')
        ApplicationForm.objects.update_or_create(name=name, email=email, course_id=course_id, is_answer=True)
        return attrs
