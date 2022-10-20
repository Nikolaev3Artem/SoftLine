from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Course(models.Model):
    title = models.CharField("Заголовок курса", max_length=200)
    language = models.CharField("Язык программирования", max_length=50)
    direction = models.CharField("Направление курса", max_length=100)
    certification = models.CharField("Информация об сертификате", max_length=250)
    description = models.TextField("Описание курса")
    price = models.IntegerField("Стоимость курса")
    hours = models.IntegerField("Сколько часов курс займёт")
    lections = models.IntegerField("Количество лекций в курсе")
    skill = models.CharField("Необходимый уровень знаний", max_length=50)
    when_start = models.DateTimeField("Начало курса")
    when_end = models.DateTimeField("Конец курса")

    def __str__(self):
        return self.title

class Student(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=150)
    password = models.CharField(max_length=20)
    Avatar = models.ImageField()
    age = models.IntegerField()
    courses = models.ManyToManyField(Course, related_name="students")

    USERNAME_FIELD = "email"

