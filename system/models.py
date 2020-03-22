from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group, Permission, AbstractUser
from .utils import *
import logging
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
