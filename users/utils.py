from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

phone_re = "\\+?[1-9][0-9]{7,14}$"
phone_validator = RegexValidator(
    phone_re,
    _("Enter a valid phone number."),
)
