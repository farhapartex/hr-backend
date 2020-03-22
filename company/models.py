from django.db import models
from django.utils.translation import ugettext_lazy as _
from system.models import Base
# Create your models here.

def image_upload_path(instance, filename):
    return "company_{0}/{1}".format(instance.id, filename)

class Company(Base):
    name = models.CharField(_("Company Name"), max_length=100)
    type = models.CharField(_("Company Type"), max_length=50)
    description = models.TextField(_("Description"), blank=True, null=True)
    height = models.IntegerField(_("Height"), blank=True, null=True)
    width = models.IntegerField(_("Width"), blank=True, null=True)
    logo = models.ImageField(
        _("Image"),
        upload_to=image_upload_path,
        height_field="height",
        width_field="width",
        max_length=500,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Branch(Base):
    company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=200)
    division = models.CharField(_("Division"), max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Designation(Base):
    name = models.CharField(_("Name"), max_length=150)
    experience = models.IntegerField(_("Experience"))
    salary = models.DecimalField(_("Salary"), max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
