from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group, Permission, AbstractUser
import logging
from .utils import *
# Create your models here.

logger = logging.getLogger(__name__)

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey("user.User", null=True, editable=False,
                                   related_name="%(app_label)s_%(class)s_created", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey("user.User", null=True, editable=False,
                                   related_name="%(app_label)s_%(class)s_updated", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.updated_by = user
            if self._state.adding:
                self.created_by = user
        super(Base, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Role(models.Model):
    SUPER_ADMIN = 1
    ADMIN = 2
    EMPLOYEE = 3
    BANNED = 4

    ROLE_CHOICES = ((SUPER_ADMIN,'Super Admin'),(ADMIN,'Admin'),(EMPLOYEE,'Employee'),(BANNED,'Banned'))
    id = models.PositiveIntegerField(_("ROLE ID"), choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()

class User(AbstractUser, Base):
    email = models.EmailField(_('email address'),unique=True, blank=True)
    role = models.ForeignKey(Role, verbose_name=_("User Role"), on_delete=models.SET_NULL, null=True)
