from rest_framework import serializers

from common.models import ContactUs, ContactForm


class ContactUsListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = ContactUs
        fields = ['id', 'country', 'city', 'street', 'location', 'email', 'phone']


class ContactFormListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = ContactForm
        fields = ['id', 'name', 'phone', 'email', 'message', ]
