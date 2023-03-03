from django.db import models

from app_shop.models import Product


class Action(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название акции:")
    product = models.ManyToManyField(Product, verbose_name="Привязка к продукту:")
    pub_date = models.DateTimeField(verbose_name="Дата публикации:")
    in_stock = models.IntegerField(verbose_name="Количество:", default=0)

    

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"


    def __str__(self) -> str:
        return self.name 

