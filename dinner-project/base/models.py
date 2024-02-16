from django.contrib.auth import get_user_model
from django.db import models


class BaseManager(models.Manager):
    def soft_delete(self):
        return self.update(is_deleted=True)


class BaseModel(models.Model):
    """This is base model that can be inherited from other models."""

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        db_column="created_by",
        related_name="%(app_label)s_%(class)s_requests_created",
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(auto_now=True, null=True)
    updated_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        db_column="updated_by",
        related_name="%(app_label)s_%(class)s_requests_updated",
        null=True,
        blank=True,
    )

    is_deleted = models.BooleanField(default=False, blank=True)  # for soft deletion

    objects = BaseManager()

    class Meta:
        abstract = True
