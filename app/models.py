from django.db import models
from django.contrib.auth.models import User


class Manufacturer(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class SinglePod(models.Model):
    name = models.CharField(max_length=125)
    count_of_puffs = models.PositiveSmallIntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    images = models.ManyToManyField('SinglePodImages')
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @property
    def cover_image(self):
        return self.images.all().first().file


class SinglePodImages(models.Model):
    file = models.ImageField(upload_to='mediafiles/single-pods/')


class Taste(models.Model):
    name = models.CharField(max_length=125)
    single_pod = models.ForeignKey(
        SinglePod,
        on_delete=models.PROTECT,
        related_name='tastes'
    )

    def __str__(self):
        return f"{self.single_pod}|{self.name}"


class SinglePodStock(models.Model):
    taste = models.ForeignKey(Taste, on_delete=models.PROTECT, related_name='stocks')
    quantity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.taste)


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    address = models.CharField(max_length=255)
    status = models.CharField(
        max_length=125,
        choices=(
            ('В обработке', 'В обработке'),
            ('Принят', 'Принят'),
            ('Достовляется', 'Достовляется'),
            ('Доставлен', 'Доставлен'),
        ),
        default='В обработке'
    )


class OrderDetail(models.Model):
    taste = models.ForeignKey(
        Taste,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    quantity = models.PositiveSmallIntegerField()
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name='order_details'
    )






class ManufacturerLiquid(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class Liquid(models.Model):
    name = models.CharField(max_length=125)
    manufacturer = models.ForeignKey(ManufacturerLiquid, on_delete=models.PROTECT)
    images = models.ManyToManyField('LiquidImages')
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @property
    def cover_image(self):
        return self.images.all().first().file


class LiquidImages(models.Model):
    file = models.ImageField(upload_to='mediafiles/liquid/')


class LiquidTaste(models.Model):
    name = models.CharField(max_length=125)
    liquid = models.ForeignKey(
        Liquid,
        on_delete=models.PROTECT,
        related_name='liquid_tastes'
    )

    def __str__(self):
        return f"{self.liquid}|{self.name}"


class LiquidStock(models.Model):
    taste = models.ForeignKey(LiquidTaste, on_delete=models.PROTECT, related_name='liquid_stocks')
    quantity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.taste)


class OrderLiquid(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='liquid_orders'
    )
    address = models.CharField(max_length=255)
    status = models.CharField(
        max_length=125,
        choices=(
            ('В обработке', 'В обработке'),
            ('Принят', 'Принят'),
            ('Достовляется', 'Достовляется'),
            ('Доставлен', 'Доставлен'),
        ),
        default='В обработке'
    )


class LiquidOrderDetail(models.Model):
    taste = models.ForeignKey(
        LiquidTaste,
        on_delete=models.PROTECT,
        related_name='liquid_orders'
    )
    quantity = models.PositiveSmallIntegerField()
    order = models.ForeignKey(
        OrderLiquid,
        on_delete=models.PROTECT,
        related_name='liquid_order_details'
    )

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reviews')
    single_pod = models.ForeignKey(
        SinglePod,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    maasege = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)






    # git status
    # git init
    # git add (asd.py - выбор файла)- добавить
    # git commit -m 'сюда писать какие изменения были внесены'
    # git log - просмотр
    # git branch (название веткм)- создание ветки
    # git checkout (название ветки) -  перейти к ветке
    # git merge master - соединение
    # .gitignore - игнорим ненужные файлы
    # git clone (ссылка не репозиторий)
    # .ignore - плагин для игнора
    # git remote add origin (ссылка на репозиторий) - отправка файла в гит заб
    # git remote - просмотр удаленных репозитории
    # git push -u (название remote) master - правка
    # git remote add origin2 - новая фигня
    # git branch -M main - переименовка
