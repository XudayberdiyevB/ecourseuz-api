from rest_framework import serializers

from common.models import ApplicationForm, AboutUs, Category, ContactUs, ContactForm, Blog, Banner, SocialMedia


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ("type", "name", "urls")


class BannerListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ("title", "description", "image")


class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = ['course', 'name', 'email']


class CategoryListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Category
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ["title", "description", "image"]


class ContactUsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ["country", "city", "street", "location", "email", "phone"]


class ContactFormListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ["name", "phone", "email", "message"]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["title", "slug", "description", "author", "views_count"]
