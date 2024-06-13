from django.db import models


class User(models.Model):
    ID = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254)
    fam = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    otc = models.CharField(max_length=255, verbose_name='Отчество')
    phone = models.CharField(max_length=15, verbose_name='Телефон')


class Coord(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    height = models.IntegerField()


class Level(models.Model):

    LEVEL_1 = '1А'
    LEVEL_2 = '1Б'
    LEVEL_3 = '2А'
    LEVEL_4 = '2Б'
    LEVEL_5 = '3А'
    LEVEL_6 = '3Б'

    LEVEL_CHOICES = (
        ('1А', '1А'),
        ('1Б', '1Б'),
        ('2A', '2А'),
        ('2Б', '2Б'),
        ('3A', '3А'),
        ('3Б', '3Б'),
    )

    winter = models.CharField(max_length=2, choices=LEVEL_CHOICES, verbose_name='Зима', default=LEVEL_1)
    spring = models.CharField(max_length=2, choices=LEVEL_CHOICES, verbose_name='Весна', default=LEVEL_1)
    summer = models.CharField(max_length=2, choices=LEVEL_CHOICES, verbose_name='Лето', default=LEVEL_1)
    autumn = models.CharField(max_length=2, choices=LEVEL_CHOICES, verbose_name='Осень', default=LEVEL_1)


class PerevalAdded(models.Model):

    NEW = 'NW'
    PENDING = "PN"
    ACCEPTED = 'AC'
    REJECTED = 'RJ'

    STATUS_CHOICES = (
        ('NW', 'Новый'),
        ('PN', 'Запрос рассматривается'),
        ('AC', 'Запрос успешно принят'),
        ('RJ', 'Запрос не принят'),
    )

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW)
    beauty_title = models.CharField(max_length=255, verbose_name='перевал')
    title = models.CharField(max_length=255, verbose_name='наименование')
    other_title = models.CharField(max_length=255, verbose_name='другие названия')
    connect = models.TextField(verbose_name='соединение')
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    coord = models.OneToOneField(Coord, on_delete=models.CASCADE, verbose_name='координаты')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='уровень сложности')


class Image(models.Model):
    data = models.CharField(max_length=2083)
    title = models.CharField(max_length=255, verbose_name='заголовок')
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.pk} {self.title}'