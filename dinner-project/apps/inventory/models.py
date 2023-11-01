from base.models import BaseModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Ingredient(BaseModel):
    name = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "식재료"
        verbose_name_plural = "식재료 (Ingredients)"

    def __str__(self) -> str:
        return f"[{self.pk}] name: {self.name}"


class Storage(BaseModel):
    name = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "저장소"
        verbose_name_plural = "저장소 (Storages)"

    def __str__(self) -> str:
        return f"[{self.pk}] name: {self.name}"


class Inventory(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    storage = models.ForeignKey("Storage", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", on_delete=models.PROTECT)
    detail = models.CharField(max_length=1000, null=True, blank=True)
    unit = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "식재료 재고"
        verbose_name_plural = "식재료 재고 (Inventories)"

    def __str__(self) -> str:
        return f"[{self.pk}] ingredient: {self.ingredient.name} detail: {self.detail}"


class InventoryLog(BaseModel):
    class Method(models.TextChoices):
        Stock = "ST", _("Stock")
        Consume = "CO", _("Consume")
        Discard = "DI", _("Discard")

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    inventory = models.ForeignKey("Inventory", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    method = models.CharField(max_length=2)

    class Meta:
        verbose_name = "식재료 재고 기록"
        verbose_name_plural = "식재료 재고 기록 (Inventory Logs)"

    def __str__(self) -> str:
        return f"[{self.pk}] inventory: {self.inventory.detail} method: {self.method}"
