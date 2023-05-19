from rest_framework import serializers

from common.models import ApplicationForm, Category, ContactUs, ContactForm, Blog


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



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
