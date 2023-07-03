from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from course.models import Course
from users.models import User


class CourseResource(resources.ModelResource):
    id = Field(attribute="id", column_name="ID", readonly=True)
    name = Field(attribute="name", column_name="Nomi")
    desc = Field(attribute="desc", column_name="Batafsil ma'lumot")
    price = Field(attribute="price", column_name="Narxi")
    discount = Field(attribute="discount", column_name="Chegirma")
    level = Field(attribute="level", column_name="Daraja")
    author = Field(
        attribute="author",
        column_name="Muallif",
        widget=ForeignKeyWidget(User, field='full_name'),
        readonly=True
    )

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "desc",
            "price",
            "discount",
            "level",
            "author"
        ]
