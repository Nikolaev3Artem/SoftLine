from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

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
    when_start = models.CharField("Начало курса", max_length=50)
    when_end = models.CharField("Конец курса", max_length=50)

    def __str__(self):
        return self.title

class Request(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = PhoneNumberField(region="UA")
    email = models.EmailField(unique=True, max_length=150)
    course = models.ForeignKey(Course, related_name="requests", on_delete=models.CASCADE)
    comment = models.CharField(max_length=250, blank=True, null=True)



