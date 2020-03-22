from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group, Permission, AbstractUser
import logging
from system.models import Base
from company.models import *
# Create your models here.

logger = logging.getLogger(__name__)

def image_upload_path(instance, filename):
    return "user_{0}/{1}".format(instance.id, filename)


class User(AbstractUser, Base):
    email = models.EmailField(_('email address'),unique=True, blank=True)
    height = models.IntegerField(_("Height"), blank=True, null=True)
    width = models.IntegerField(_("Width"), blank=True, null=True)
    image = models.ImageField(
        _("Image"),
        upload_to=image_upload_path,
        height_field="height",
        width_field="width",
        max_length=500,
        null=True
    )


PROBATION_CHOICES = ((0, 'No Probation'),(1, '1 Month'), (3, '3 Months'), (6, '6 Months'), (8, '8 Months'), (12, '1 Year'), (18, '1.5 years'))
class Employee(Base):
    user = models.OneToOneField(User, related_name="employee", on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, related_name="employees", on_delete=models.SET_NULL, blank=True, null=True)
    designation = models.ForeignKey(Designation, related_name="d_employees", on_delete=models.SET_NULL, blank=True, null=True)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    probation_period = models.IntegerField(choices=PROBATION_CHOICES, default=3)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
