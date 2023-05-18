from rest_framework import serializers

from common.models import ApplicationForm, Category, ContactUs, ContactForm


class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = ['course', 'name', 'email', 'category']


class CategoryListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Category
        fields = '__all__'


class ContactUsListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = ContactUs
        fields = '__all__'


class ContactFormListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = ContactForm
        fields = '__all__'
