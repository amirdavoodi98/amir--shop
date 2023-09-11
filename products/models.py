from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=512, verbose_name='نام محصول')
    price = models.IntegerField(verbose_name='قیمت هر کیلو محصول')
    image = models.ImageField(upload_to='products/', verbose_name='تصویر محصول', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='محصول'